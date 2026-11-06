# Integrating ARTEFAKT UPDATE CENTER

## 1. Web and PWA

1. Host the catalog and detached signature on the public HTTPS origin.
2. Add a service worker with a versioned cache strategy and an explicit message handler for `SKIP_WAITING`.
3. Include `web-update-client.js` and call `startArtefaktWebUpdateCheck()`.
4. Show a clear update prompt; save user work before activating the new worker.
5. Test offline launch, interrupted downloads, cache migration, and rollback before production.

The helper in this repository is a reference integration, not a complete service worker and not yet deployed.

## 2. Android

Each app must be rebuilt with an updater integration. The updater should:

- fetch catalog and detached signature over HTTPS;
- verify Ed25519 signature against a public key embedded in the app;
- match exact applicationId, platform, channel, OS constraints and build;
- verify APK SHA-256 and Android package signing certificate;
- route Play-distributed builds to Google Play's in-app update API / Play Store;
- for sideloaded APKs, download to app-private storage and invoke the Android package installer, leaving user confirmation to Android;
- never request broad storage access just to update itself;
- pause/abort on network loss and retain the current installed version;
- expose update notes and allow deferral unless a justified mandatory security update is approved.

An ordinary app cannot silently install arbitrary APKs on standard Android devices. Do not promise unattended installation.

## 3. Desktop

Use each operating system's signed installer/update framework. Verify publisher identity and artifact hash before applying. Support staged rollout and rollback.

## 4. iOS

Use App Store distribution and Apple's supported update mechanisms. Do not attempt third-party silent installation.

## 5. Release publishing pipeline

For every release:

1. Build from a tagged, reviewed commit.
2. Run automated tests and platform packaging checks.
3. Sign the artifacts with the platform's release identity.
4. Calculate SHA-256 and record exact byte size.
5. Verify the artifact by downloading it and checking signature, package identity and installability.
6. Publish notes and artifacts.
7. Generate the catalog and detached signature from the release metadata.
8. Validate the catalog against `catalog.schema.json`.
9. Publish to the public HTTPS endpoint.
10. Start at a small rollout percentage, monitor failures, then expand.

Do not publish a release record until all required checks pass. Keep the prior known-good release available for rollback.
