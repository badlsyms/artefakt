#!/usr/bin/env python3
"""Offline Ed25519 detached-signature tool for ARTEFAKT-LAB catalog JSON.

No private keys are generated or stored in this repository.
Install dependency: python -m pip install 'cryptography>=42,<47'
"""
import argparse
import base64
import json
import os
from pathlib import Path
import sys
import tempfile

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)

MAX_BYTES = 256 * 1024


def catalog_bytes(path):
    data = Path(path).read_bytes()
    if not data or len(data) > MAX_BYTES:
        raise ValueError("Catalog missing or exceeds 256 KiB")
    obj = json.loads(data)
    if not isinstance(obj, dict) or obj.get("schemaVersion") != 1:
        raise ValueError("Unsupported schemaVersion")
    if obj.get("issuer") != "ARTEFAKT-LAB":
        raise ValueError("Unexpected catalog issuer")
    if type(obj.get("catalogVersion")) is not int or obj["catalogVersion"] < 1:
        raise ValueError("catalogVersion must be positive integer")
    if not isinstance(obj.get("apps"), list):
        raise ValueError("apps must be an array")
    return data


def write_atomically(path, data):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".signature-", dir=str(target.parent))
    try:
        with os.fdopen(fd, "wb") as out:
            out.write(data)
            out.flush()
            os.fsync(out.fileno())
        os.replace(tmp, target)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    cmd = p.add_subparsers(dest="command", required=True)
    sign = cmd.add_parser("sign")
    sign.add_argument("--catalog", required=True)
    sign.add_argument("--private-key", required=True, help="PEM Ed25519 private key on trusted signing host")
    sign.add_argument("--signature", help="Output binary signature; defaults to <catalog>.sig")
    verify = cmd.add_parser("verify")
    verify.add_argument("--catalog", required=True)
    verify.add_argument("--public-key", required=True, help="PEM Ed25519 public key")
    verify.add_argument("--signature", help="Binary signature; defaults to <catalog>.sig")
    export = cmd.add_parser("export-public-key")
    export.add_argument("--public-key", required=True)
    args = p.parse_args()

    if args.command == "export-public-key":
        key = serialization.load_pem_public_key(Path(args.public_key).read_bytes())
        if not isinstance(key, Ed25519PublicKey):
            raise ValueError("Expected Ed25519 public key")
        der = key.public_bytes(serialization.Encoding.DER,
                               serialization.PublicFormat.SubjectPublicKeyInfo)
        print(base64.b64encode(der).decode("ascii"))
        return

    data = catalog_bytes(args.catalog)
    signature_path = args.signature or args.catalog + ".sig"
    if args.command == "sign":
        key = serialization.load_pem_private_key(Path(args.private_key).read_bytes(), password=None)
        if not isinstance(key, Ed25519PrivateKey):
            raise ValueError("Expected Ed25519 private key")
        signature = key.sign(data)
        if len(signature) != 64:
            raise ValueError("Unexpected Ed25519 signature length")
        write_atomically(signature_path, signature)
        print("Signed catalog raw bytes. Keep private key off web and git.")
    else:
        key = serialization.load_pem_public_key(Path(args.public_key).read_bytes())
        if not isinstance(key, Ed25519PublicKey):
            raise ValueError("Expected Ed25519 public key")
        signature = Path(signature_path).read_bytes()
        if len(signature) != 64:
            raise ValueError("Invalid signature length")
        try:
            key.verify(signature, data)
        except InvalidSignature as exc:
            raise ValueError("Signature verification failed") from exc
        print("OK: trusted catalog signature, format and issuer verified")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as error:
        print("ERROR: " + str(error), file=sys.stderr)
        raise SystemExit(1)
