# ARTEFAKT UPDATE CENTER — catalog v1

This directory defines the public update-catalog contract.

## Public endpoint

After deployment, publish this directory under:

`https://artefakt-lab.wz.cz/updates/v1/`

The catalog URL is:

`https://artefakt-lab.wz.cz/updates/v1/catalog.json`

The initial catalog intentionally contains no release entries. Do not invent releases or point users at unverified binaries.

## Release record

Each app entry must include:

- `appId`: stable reverse-domain identifier (must match the installed app's package/bundle identity).
- `name`, `platform`, `channel`, `version`, `build`.
- `minimumUpdaterVersion` and supported OS/device constraints where relevant.
- `publishedAt`, `releaseNotesUrl`, `mandatory` (normally false).
- `artifacts`: platform-specific download URL, byte size, SHA-256, media type, and signing identity.
- `rollout`: percentage and optional start/end timestamps.
- `revokedBuilds`: build identifiers that must no longer be offered.

Never put private signing keys, passwords, API tokens, or user data in the catalog.

## Trust model

HTTPS protects transport, but is not the release trust root. Before production rollout:

1. Create an offline Ed25519 release-signing keypair.
2. Keep the private key offline or in a tightly permissioned CI secret/HSM; never commit it.
3. Publish a detached signature for the exact catalog bytes (for example `catalog.json.sig`) and pin the public key in updater clients.
4. Verify the signature before parsing or acting on a catalog.
5. For Android APK updates, also verify package identity and Android signing certificate continuity; SHA-256 alone is not proof of publisher identity.
6. For Google Play apps, send users to Play's supported update flow rather than sideloading.
7. Roll out gradually and keep a tested rollback build.

The initial JSON is an unsigned template and MUST NOT be used by production clients until the signature workflow and pinned public key are implemented and tested.

## Compatibility and safety

- Unknown schema versions: fail closed and keep the installed version.
- Missing or invalid signature/hash/package identity: reject the update.
- Never silently downgrade; only accept an explicitly authorized rollback.
- Mandatory updates require a documented security/compatibility reason and a safe migration path.
- Back up app data before migrations; migrations must be backward-safe where practical.
- Respect platform rules and user consent for installation.
- Do not transmit device identifiers or personal data for ordinary update checks.

## Integration status

A catalog does not update already-installed apps by itself. Each application must integrate an updater or the platform's official update mechanism and receive a new tested release. Web/PWA clients can use normal service-worker update lifecycle after their deployment is verified.
