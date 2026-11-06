# ARTEFAKT UPDATE CENTER — deployment to Webzdarma

Prepared web page: `updates/v1/site/update-center.html`

## Target URL

`https://artefakt-lab.wz.cz/update-center.html`

This URL is **NOT live until the HTML file is uploaded to Webzdarma**. The existing live index is `https://artefakt-lab.wz.cz/download.html`.

## Publish the public page (no secret keys)

1. Open the Webzdarma administration/FTP for the **actual site** `artefakt-lab.wz.cz` using an authorized hosting account.
2. Upload `updates/v1/site/update-center.html` to the site's web-root as `update-center.html` (same directory as `download.html`).
3. Optionally add the anchor snippet in `navigation-snippet.html` to the site's existing `download.html` navigation. Do not replace the page or its current links.
4. Visit `https://artefakt-lab.wz.cz/update-center.html`, test phone/desktop layouts, and verify each product link.
5. If cache is enabled, invalidate the old HTML on publishing.

## Publish signed catalogs ONLY after release validation

The separate signed catalog endpoint is intended to be
`https://artefakt-lab.wz.cz/updates/v1/catalog.json` with raw detached
`catalog.json.sig`. It currently returned HTTP 404 during deployment inspection
on 2026-11-06. Do **not** upload the unsigned template as a live updater manifest.

Before enabling clients:
- sign the exact raw bytes using a securely kept Ed25519 signing key;
- verify the signature with the pinned public key;
- check signed APK metadata, Android signing identity, versionCode and SHA-256;
- run Android client tests and a physical-device pilot;
- obtain host deployment access and verify both URLs from another network;
- only then set the Android pilot's explicitly empty `CONFIG` fields.

## Operational caveat

The website HTML can be published safely as an informational download hub,
even while the updater backend is disabled. A link to an existing product page
is not proof of a newly signed release. No private signing key belongs in the
web root, GitHub commit history, or a client APK.
