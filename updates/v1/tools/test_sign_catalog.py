"""ARTEFAKT Update Center signing regression tests. Uses ephemeral keys only."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

SCRIPT = Path(__file__).with_name("sign_catalog.py")


class SignCatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.catalog = self.base / "catalog.json"
        self.catalog.write_text(json.dumps({
            "schemaVersion": 1, "catalogVersion": 1,
            "generatedAt": "2026-11-06T00:00:00Z",
            "issuer": "ARTEFAKT-LAB", "apps": []
        }), encoding="utf-8")
        private = Ed25519PrivateKey.generate()
        public = private.public_key()
        self.private_file = self.base / "private.pem"
        self.public_file = self.base / "public.pem"
        self.private_file.write_bytes(private.private_bytes(
            serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption()))
        self.public_file.write_bytes(public.public_bytes(
            serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo))

    def command(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args], capture_output=True, text=True)

    def signed(self):
        return self.command("sign", "--catalog", str(self.catalog),
                            "--private-key", str(self.private_file))

    def verified(self):
        return self.command("verify", "--catalog", str(self.catalog),
                            "--public-key", str(self.public_file))

    def test_sign_then_verify(self):
        self.assertEqual(self.signed().returncode, 0)
        self.assertEqual((self.base / "catalog.json.sig").stat().st_size, 64)
        self.assertEqual(self.verified().returncode, 0)

    def test_tamper_rejected(self):
        self.assertEqual(self.signed().returncode, 0)
        self.catalog.write_bytes(self.catalog.read_bytes() + b" ")
        self.assertNotEqual(self.verified().returncode, 0)

    def test_wrong_key_rejected(self):
        self.assertEqual(self.signed().returncode, 0)
        other = Ed25519PrivateKey.generate().public_key()
        self.public_file.write_bytes(other.public_bytes(
            serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo))
        self.assertNotEqual(self.verified().returncode, 0)

    def test_bad_schema_rejected_before_signing(self):
        self.catalog.write_text('{"schemaVersion":2,"catalogVersion":1,"issuer":"ARTEFAKT-LAB","apps":[]}')
        self.assertNotEqual(self.signed().returncode, 0)
        self.assertFalse((self.base / "catalog.json.sig").exists())

    def test_export_x509_spki(self):
        import base64
        result = self.command("export-public-key", "--public-key", str(self.public_file))
        self.assertEqual(result.returncode, 0)
        self.assertGreater(len(base64.b64decode(result.stdout.strip())), 32)


if __name__ == "__main__":
    unittest.main()
