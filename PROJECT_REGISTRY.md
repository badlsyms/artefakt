# ARTEFAKT-LAB — Centrální registr verzí

> Poslední kontrola: 9. 11. 2026, 06:11 Europe/Prague.
> Rozsah: všech 10 repozitářů dostupných přes připojený GitHub účet; stránkování seznamu dokončeno.
> Stav kontroly: ČÁSTEČNÁ — všech 10 dostupných repozitářů bylo zkontrolováno; produkční webové adresy nebyly dostupné přes webový přístup. Tag refs a Releases byly zkontrolovány u 7 neprázdných repozitářů; 3 repozitáře zůstávají prázdné.
> Tento registr rozlišuje zdrojový kód, úspěšné sestavení, podepsaný artefakt, testování a skutečné produkční nasazení. Neověřený údaj se nikdy nedoplňuje odhadem.

## Pravidla evidence

- Rozlišovat **rozpracovanou**, **sestavenou**, **podepsanou**, **otestovanou** a **produkčně nasazenou** verzi.
- Číslo verze se nesmí odvozovat z názvu PR, data commitu ani požadovaného cíle.
- APK a AAB evidovat odděleně; kontrolovat applicationId/package, versionName, versionCode, podpisový certifikát a SHA-256.
- Web evidovat podle manifestu/build metadat a skutečného produkčního nasazení.
- „Nejnovější commit“ není automaticky „nejnovější vydání“.
- SHA-256 ZIP artefaktu GitHub Actions není SHA-256 samotného APK.
- Debug podpis není produkční podpis. U debug klíče může být fingerprint závislý na prostředí sestavení.
- Chybějící důkaz se zapisuje jako NEOVĚŘENO, nikdy se nedoplňuje odhadem.

## Souhrn projektů

| Projekt | Verze z papírové evidence | Nejnovější ověřený zdroj / sestavení | Stav vydání a ověření |
|---|---:|---|---|
| 0L8 Suite | 0.32.7 | NEOVĚŘENO – mezi dostupnými repozitáři nebyl jednoznačný zdroj 0L8 | Zdroj, APK/AAB, podpis, testy a produkce NEOVĚŘENO |
| XYQ Next | 0.17? | Android main: 0.14.0 / versionCode 17; web manifest: 0.10.0. PR #9 uvádí 0.18.1, ale je draft a není sloučen | Main CI vytvořilo 0.14 unsigned APK; 0.18.1 není vydání; produkce a fyzický test NEOVĚŘENO |
| MV-1 Studio Pro | 1.78 | Android main: 1.65 / versionCode 165. PR #4 uvádí 1.83, ale je draft a není sloučen | Úspěšný main build vytvořil unsigned APK 1.65; žádné ověřené produkční podepsané vydání |
| PSYCHON 2 | 1.4.1 | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| PSYCHON 3 | 0.7.2 | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| FOR+BEZ | 1.0.0 | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| ASHfall | — | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| CAMERA HUNT AR | 10.0.0? | NEOVĚŘENO | Číslo z fotografie nejisté; bez přiřazeného repozitáře |
| sWEEDS | 2.11 | NEOVĚŘENO | V dostupných repozitářích nebyl nalezen jednoznačný zdroj sWEEDS |
| MAJTELAB / MAJTELAB? | 2.80 | NEOVĚŘENO | V repozitáři existuje samostatný artefakt MASTER LAB 3.0.0 debug; vazba na tento název není potvrzena |
| XYQ + RXTX NEXT | 0.17 + 0.19? | XYQ main Android 0.14.0 / code 17; RXTX samostatně NEOVĚŘENO | Vyšší verze XYQ v PR jsou rozpracované, nikoli vydané |
| ARTEFAKT AGENT | 0.3.2 | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| OCB Device Manager | 0.3.0 | NEOVĚŘENO | Název z fotografie ověřit; OCCO Studio nelze bez důkazu ztotožnit s tímto projektem |
| OCB EventOps | 3.6.0 | NEOVĚŘENO | Název z fotografie ověřit; OCCO Studio nelze bez důkazu ztotožnit s tímto projektem |
| 4UD10 | — | NEOVĚŘENO | Název/verze z fotografie nejasné |
| ASV BODECH | 2.0.0 | NEOVĚŘENO | Název z fotografie nejasný |
| TRACE (CAT) | 1.3.0 | Zdroj: 1.3-ci / versionCode 13; úspěšný debug APK build 6. 11. 2026 | APK je debug-signed, nikoli produkčně podepsané vydání; fyzický test a produkce NEOVĚŘENO |
| SCAFFXGRAM | 1.22 | NEOVĚŘENO | Název z fotografie nejasný |
| RXTX | 0.3 | NEOVĚŘENO | Samostatný repozitář/verze nebyly v dostupných zdrojích potvrzeny |
| SPEQTR + HALO | 1.1.0-1 | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| IN MASTER-SAVE | 1.8.1? | NEOVĚŘENO | Název/verze z fotografie nejasné |
| WHIQ (WHISTLER) | 1.1.1 | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| Legorider | 0.3.0 | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| Music 2073 | 0.12 | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| SLYPH LAB | 2.1.0 | NEOVĚŘENO | Název z fotografie nejasný |
| REIN/TENT | — | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| 4BO Replay | — | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| SIGNAL BELOW | — | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| TROL8 Synthlab | — | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| EventLog | — | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| FIQ | — | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| OCCO + OpenDAW | — | NEOVĚŘENO | Existuje samostatný OCCO Studio Android 4.7.1; jeho vztah k tomuto projektu není potvrzen |
| FREQ Terapeut / Frekvenční Terapie V4+ | — | Electron a Capacitor package metadata: 1.0.0; web manifest nemá číslo verze | PR #1 má úspěšné webové testy, ale zůstává otevřený; bez APK/AAB a bez fyzického testu |
| ROK Včas | — | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| Triton Taktile Editor V1/V2 | — | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| QIP | — | NEOVĚŘENO | Bez přiřazeného zdrojového repozitáře a artefaktu |
| OCCO Studio Android (repo-derived; vazba na řádky OCB/OCCO nepotvrzena) | — | 4.7.1 / versionCode 471 / applicationId cz.occo.mv1 | Úspěšný podepsaný release APK build 14. 8. 2026; APK SHA-256 a certifikát doloženy v CI logu; AAB, fyzický test a produkční nasazení NEOVĚŘENO |
| Můj Nucleus 2.0 (repo-derived) | — | package.json 2.2.0 | Zdrojová verze doložena; běh Cloud Run a skutečná produkční verze NEOVĚŘENO |
| MASTER LAB (repo-derived; vazba na MAJTELAB nepotvrzena) | — | Artefakt pojmenován 3.0.0 Android signed debug na ne-main větvi | Debug artefakt existuje; zdrojová main verze, produkční podpis a produkce NEOVĚŘENO |

## Detailní ověření — 7. 11. 2026

### MV-1 Studio a XYQ — badlsyms/mv1-lab

**Main branch**
- Poslední dohledaný main commit: 8fdad22371061908329cca816d36ae3e6a8adac6, 19. 10. 2026.
- MV-1 Android: applicationId cz.artefaktlab.mv1lab, versionName 1.65, versionCode 165, minSdk 26, targetSdk 35. Zdroj: https://github.com/badlsyms/mv1-lab/blob/main/android-project/app/build.gradle
- XYQ Android: release applicationId cz.artefakt.xyq, preview applicationId cz.artefakt.xyq.preview, versionName 0.14.0, versionCode 17, minSdk 29, targetSdk 36. Zdroj: https://github.com/badlsyms/mv1-lab/blob/main/suite/xyq/android/app/build.gradle
- XYQ web manifest: version 0.10.0. Zdroj: https://github.com/badlsyms/mv1-lab/blob/main/suite/xyq/web/manifest.webmanifest

**Poslední ověřený main build**
- GitHub Actions run 39200811788, 19. 10. 2026: https://github.com/badlsyms/mv1-lab/actions/runs/39200811788
- UX job: success; prošly responzivní UI, audio, projekty, poznámky, checklist a privátní účet/sync API.
- Android job: success; MV-1 a XYQ sestavení dokončena; XYQ unit tests dokončeny.
- Artefakty: MV1_1.65_XYQ_0.14_ANDROID a MV1_1.65_XYQ_0.14_UX.
- Důležité: workflow výslovně kopíruje app-release-unsigned.apk pro MV-1 i XYQ. Jde o unsigned APK, nikoli o podepsané produkční balíčky. Workflow nevytváří AAB. APK SHA-256 nebylo z dostupného výpisu logu samostatně potvrzeno; SHA-256 ZIP artefaktu se za APK hash nepovažuje.
- Fyzická instalace a test na skutečném Android zařízení: NEOVĚŘENO.
- Produkční webová verze a produkční nasazení: NEOVĚŘENO.

**Rozpracované změny — nezaměňovat za vydání**
- PR #4 „MV1 Studio Pro 1.83“ je otevřený draft, není sloučen do main: https://github.com/badlsyms/mv1-lab/pull/4
- PR #9 „XYQ 0.18.1“ je otevřený draft na větvi xyq/next-consolidation, není sloučen do main: https://github.com/badlsyms/mv1-lab/pull/9
- PR #10 „XYQ: pilot bezpečné kontroly aktualizací ARTEFAKT UPDATE CENTER“ je otevřený draft: https://github.com/badlsyms/mv1-lab/pull/10
- Pilot PR #10 obsahuje fail-closed klienta, ale konfigurace katalogu a veřejného klíče je prázdná; klient je záměrně vypnutý. Nestahuje ani neinstaluje APK.
- CI pilotu: poslední dohledaný run 42209053542 skončil success, předchozí pokusy v téže sérii selhaly. Úspěšný běh nevytvořil distribuční artefakt. Fyzický Android test chybí.
- README_CZ.md stále popisuje MV-1 LAB 1.64, zatímco Gradle a main build artefakt dokládají 1.65. Dokumentace je tedy opožděná.
- Tagy a GitHub Releases: v tomto repozitáři nebyly nalezeny.

### Frekvenční Terapie V4+ — badlsyms/Frekvencni_Terapie_App

- Main branch má pouze počáteční commit z 9. 9. 2025: https://github.com/badlsyms/Frekvencni_Terapie_App/commit/6c9a1cccfcccc6607ed81f03fb80320bc89107c7
- Electron package version: 1.0.0. Capacitor package version: 1.0.0.
- Web manifest neobsahuje pole version: https://github.com/badlsyms/Frekvencni_Terapie_App/blob/main/web/manifest.webmanifest
- PR #1 „Frekvenční terapie: mobilní výběr, motivy a offline kontrola“ je otevřený, není sloučen: https://github.com/badlsyms/Frekvencni_Terapie_App/pull/1
- CI na PR větvi 31. 10. 2026 skončilo success: https://github.com/badlsyms/Frekvencni_Terapie_App/actions/runs/41227310293
- Testy se týkají webového UI, výběru frekvencí, audio Start/Stop, motivů a offline shellu. PR výslovně uvádí, že fyzický Android ani skutečný poslech nebyly ověřeny.
- APK, AAB, desktop instalační balíčky a produkční deployment: NEOVĚŘENO.
- Tagy a GitHub Releases: nenalezeny.

### TRACE — badlsyms/artefaktlab/TRACE

- Zdroj: versionName 1.3-ci, versionCode 13, applicationId cz.artefaktlab.trace.
- Gradle: https://github.com/badlsyms/artefaktlab/blob/main/TRACE/app/build.gradle
- README výslovně označuje APK za debug-signed, nikoli za produkční release certifikát: https://github.com/badlsyms/artefaktlab/blob/main/TRACE/README.md
- Main CI run 42210300364, 6. 11. 2026, success: https://github.com/badlsyms/artefaktlab/actions/runs/42210300364
- Artefakt: TRACE-1.3-signed-debug-APK, ID 13498826863: https://github.com/badlsyms/artefaktlab/actions/runs/42210300364/artifacts/13498826863
- apksigner ověřil APK v2 podpis. Certifikát je Android Debug, SHA-256 fingerprint 85cb61295dd4e3407f933537397e1469192ecc5b55b67c9b587435842c1a3191.
- Tento fingerprint je debug certifikát, nikoli produkční identita vydavatele. APK SHA-256 samostatně NEOVĚŘENO; digest 0834047e5017bc3200c4583fdf1ee15b48a212e6af28f500fdcaf20fd820b46e patří ZIP artefaktu.
- AAB, fyzický test a produkční nasazení: NEOVĚŘENO.

### OCCO Studio Android — badlsyms/occo-studio-v471-signed-20260814-235417

- Gradle source: applicationId cz.occo.mv1, versionName 4.7.1, versionCode 471.
- Zdroj: https://github.com/badlsyms/occo-studio-v471-signed-20260814-235417/blob/main/app/build.gradle
- Úspěšný workflow run 31844439451, 14. 8. 2026: https://github.com/badlsyms/occo-studio-v471-signed-20260814-235417/actions/runs/31844439451
- Artefakt: OCCO-Studio-v4.7.1-signed-release-apk, ID 9235432909: https://github.com/badlsyms/occo-studio-v471-signed-20260814-235417/actions/runs/31844439451/artifacts/9235432909
- apksigner v CI ověřil v1 a v2 podpis; jeden signer, CN=OCCO Studio Release.
- Podpisový certifikát SHA-256: 5ef0b002c93d4f54e764adf9491484b8b61e0214518b0009eb1f2b74297210f3.
- APK SHA-256 z CI logu: 96a97f4e6d3070139b4373e00058a7acabf0df7415e18b0539310e2f2e0b9339.
- Digest 49439e66fc82a654e518fd9f29b7c67e74ce46a68830a2ff80029f46dfa4274a patří ZIP artefaktu GitHub Actions, nikoli APK.
- Workflow vytváří APK, nikoli AAB. Fyzický Android test a skutečná produkční instalace: NEOVĚŘENO.
- GitHub artifact měl při kontrole expiraci 12. 11. 2026.
- Build log upozorňuje, že META-INF/com/android/build/gradle/app-metadata.properties a META-INF/version-control-info.textproto nejsou chráněny podpisem. Podpis APK jako celek byl ověřen, tato upozornění je vhodné posoudit.
- BUILD_CZ.txt stále uvádí OCCO v4.0.0, přestože Gradle, workflow a artefakt dokládají 4.7.1: https://github.com/badlsyms/occo-studio-v471-signed-20260814-235417/blob/main/BUILD_CZ.txt
- AAB, produkční webová verze a nasazení: NEOVĚŘENO.

### Můj Nucleus 2.0 — badlsyms/artefaktlab/nucleus-cloudrun

- README označuje repozitář za zdrojovou zálohu produkční aplikace Můj Nucleus pro Google Cloud Run.
- Zdroj package.json: version 2.2.0, name muj-nucleus-cloudrun.
- Soubor: https://github.com/badlsyms/artefaktlab/blob/main/nucleus-cloudrun/package.json
- README uvádí Cloud Run service remix-m-j-ai-asistent, region europe-west2: https://github.com/badlsyms/artefaktlab/blob/main/README.md
- Skutečný stav běžící služby, veřejná URL a nasazená verze nebyly v této kontrole ověřeny.
- APK/AAB a produkční testy: NEOVĚŘENO.

### MASTER LAB — artefakt pouze z ne-main větve

- GitHub Actions run 42211163271, 6. 11. 2026, success: https://github.com/badlsyms/artefaktlab/actions/runs/42211163271
- Artefakt MASTER-LAB-3.0.0-ANDROID-SIGNED-DEBUG, ID 13498842925, vytvořen na větvi masterlab-android-v2-1-build.
- Jde o debug artefakt z ne-main větve; jeho název není důkazem produkčního vydání ani potvrzením zdrojové verze na main.
- Vazba na papírový řádek MAJTELAB není potvrzena. Produkční podpis, fyzický test a nasazení NEOVĚŘENO.

## Inventura dostupných GitHub repozitářů

V této kontrole bylo dostupných 10 repozitářů:

| Repozitář | Zjištěný obsah | Výsledek |
|---|---|---|
| badlsyms/artefakt | Centrální registr a návrh Update Center | PR #1 je open draft; katalog zatím není nasazen |
| badlsyms/mv1-lab | MV-1, XYQ, Android a webové zdroje | Aktivní zdroj; žádné tagy ani GitHub Releases |
| badlsyms/artefaktlab | TRACE a Můj Nucleus; MasterLab artefakt na jiné větvi | Aktivní zdroj; žádné tagy ani GitHub Releases |
| badlsyms/Frekvencni_Terapie_App | Web, Electron, Capacitor | Aktivní zdroj a otevřený PR; žádné tagy ani GitHub Releases |
| badlsyms/occo-studio-v471-signed-20260814-235417 | OCCO Studio 4.7.1 | Doložený podepsaný release APK artefakt |
| badlsyms/occo-studio-v460-build-20260814-115954 | OCCO Studio 4.6.0 / versionCode 460 | Starší zdrojový snapshot |
| badlsyms/occo-mv1-android-build-20260814-041816 | OCCO Android 2.3.1 / versionCode 231 | Starší zdrojový snapshot |
| badlsyms/QO | Prázdný repozitář | Bez zdrojů a verzí |
| badlsyms/freqTherapy | Prázdný repozitář | Bez zdrojů a verzí |
| badlsyms/freq | Prázdný repozitář | Bez zdrojů a verzí |

Kontrola Git tagů a GitHub Releases v aktivních repozitářích mv1-lab, Frekvencni_Terapie_App, artefaktlab a OCCO v4.7.1 nevrátila žádné tagy ani releases. U starších OCCO snapshotů nebyla kompletní kontrola tagů/releases provedena.

## Produkční weby a aktualizační služba

- Kontrolované adresy: https://artefakt-lab.wz.cz, https://artefakt-lab.wz.cz/projects a https://artefakt-lab.wz.cz/updates/v1/catalog.json
- Tyto adresy nebylo možné v této kontrole načíst přes dostupný webový přístup. To samo o sobě nedokazuje, že server nefunguje; stav je NEOVĚŘENO.
- Aktualizační katalog a integrační podklady jsou pouze v otevřeném draft PR #1 v repozitáři badlsyms/artefakt: https://github.com/badlsyms/artefakt/pull/1
- PR #1 není sloučený a katalog není nasazený na Webzdarma. Žádná aplikace proto zatím nemá potvrzenou aktivní globální automatickou aktualizaci.
- XYQ pilot PR #10 je také draft a klient je záměrně vypnutý, dokud nebude existovat ověřený veřejný HTTPS katalog, produkční veřejný klíč a otestovaný instalační tok.

## Kontrola — 8. 11. 2026

### Souhrn změn proti předchozí kontrole

- Seznam připojených repozitářů byl znovu načten včetně dokončení stránkování: stále 10 repozitářů, žádný další výsledek.
- Hlavní zdroj MV-1/XYQ v `badlsyms/mv1-lab` zůstává na posledním doloženém main commitu `8fdad22371061908329cca816d36ae3e6a8adac6`; zdrojové verze se podle main manifestů nezměnily.
- `badlsyms/artefaktlab` má main commit `26bc2efe334add10236e9c0d5b3194c88b0fdc30` z 6. 11. 2026: oprava instalace Android SDK v TRACE workflow. Změna je v CI workflow, nikoli v Gradle metadatech aplikace. Commit: https://github.com/badlsyms/artefaktlab/commit/26bc2efe334add10236e9c0d5b3194c88b0fdc30
- TRACE zdroj zůstává `1.3-ci` / versionCode 13 / applicationId `cz.artefaktlab.trace`: https://github.com/badlsyms/artefaktlab/blob/main/TRACE/app/build.gradle
- Po opravě SDK proběhl TRACE main push run `42210300364` dne 6. 11. 2026 a skončil success; předchozí run `42210196648` skončil failure. V úspěšném běhu prošly instalace SDK, sestavení debug APK, ověření APK podpisu a upload artefaktu. Run: https://github.com/badlsyms/artefaktlab/actions/runs/42210300364
- TRACE artefakt `TRACE-1.3-signed-debug-APK`, ID `13498826863`, velikost 9 698 bajtů, je stále dostupný; expirace 4. 2. 2027. Jde výslovně o debug-signed APK, ne produkční vydání: https://github.com/badlsyms/artefaktlab/actions/runs/42210300364/artifacts/13498826863
- `badlsyms/artefakt` main zůstává na registru z 7. 11.; návrh Update Center je stále pouze otevřený draft PR #1, nikoli součást main: https://github.com/badlsyms/artefakt/pull/1

### ARTEFAKT UPDATE CENTER — nově ověřený stav PR #1

PR #1 je stále **open / draft / not merged**. Aktuální větev obsahuje 12 změněných souborů, včetně:
- offline nástroje `updates/v1/tools/sign_catalog.py` pro oddělený Ed25519 podpis a ověření katalogu;
- regresních testů `test_sign_catalog.py`, které používají pouze dočasné/ephemeral klíče;
- CI workflow pro podpisové testy a samostatné JSON Schema + JavaScript validace;
- návodu pro Webzdarma a připravené informační stránky `update-center.html`;
- navigačního snippet souboru.

Důkazy z aktuální PR větve:
- PR #1: https://github.com/badlsyms/artefakt/pull/1
- podpisový nástroj: https://github.com/badlsyms/artefakt/blob/feature/update-center-v1/updates/v1/tools/sign_catalog.py
- testy: https://github.com/badlsyms/artefakt/blob/feature/update-center-v1/updates/v1/tools/test_sign_catalog.py
- deployment návod: https://github.com/badlsyms/artefakt/blob/feature/update-center-v1/updates/v1/site/DEPLOY-WEBZDARMA.md
- připravená stránka: https://github.com/badlsyms/artefakt/blob/feature/update-center-v1/updates/v1/site/update-center.html
- katalog: https://github.com/badlsyms/artefakt/blob/feature/update-center-v1/updates/v1/catalog.json

CI na draft PR větvi:
- Run `42210773201` — Update catalog validation: success; prošla JSON Schema validace a kontrola syntaxe webového updateru. https://github.com/badlsyms/artefakt/actions/runs/42210773201
- Run `42210772928` — Signed Update Catalog tests: success; dokončil se Python unittest běh podpisových regresních testů. https://github.com/badlsyms/artefakt/actions/runs/42210772928
- Oba běhy jsou PR checks na vývojové větvi, nikoli důkaz nasazení nebo vydání.
- Katalog stále obsahuje prázdné pole `apps: []`; žádná aplikace v něm není publikována. Větev neobsahuje produkční soukromý klíč; testy používají dočasné klíče.
- Deployment dokumentace v PR uvádí, že `/updates/v1/catalog.json` v kontrole 6. 11. 2026 vracel HTTP 404 a že stránka `/update-center.html` není živá, dokud nebude nahrána na Webzdarma. Dne 8. 11. 2026 se nepodařilo přes dostupný webový přístup načíst ani homepage, ani katalog; aktuální stav serveru proto zůstává NEOVĚŘENO. To samo o sobě není důkaz, že server nefunguje.
- Automatické aktualizace koncových aplikací zůstávají NEAKTIVNÍ / NEPOTVRZENÉ.

### Stav hlavních PR a rozpracovaných verzí

- `badlsyms/mv1-lab`: PR #1, #2, #3, #4, #5, #6, #7, #8, #9 a #10 byly znovu načteny; všechny zůstávají otevřené a nesloučené. PR #4 (MV-1 1.83), #9 (XYQ 0.18.1) a #10 (XYQ updater pilot) jsou draft. PR #1/#2/#5 nejsou draft, ale také nejsou sloučené. Žádný z těchto PR nemění oficiální main verzi, dokud nebude sloučen a znovu sestaven.
- Ověření stavů PR: https://github.com/badlsyms/mv1-lab/pulls
- `badlsyms/artefaktlab`: PR #1 „Nucleus: ochrana soukromého přístupu a mobilní motivy“ zůstává otevřený, nesloučený: https://github.com/badlsyms/artefaktlab/pull/1
- `badlsyms/Frekvencni_Terapie_App`: PR #1 zůstává otevřený, nesloučený. Dřívější push run `41227305855` i PR run `41227310293` skončily success; jde o webové testy na vývojové větvi, nikoli o APK/AAB nebo fyzický Android test: https://github.com/badlsyms/Frekvencni_Terapie_App/actions/runs/41227305855 a https://github.com/badlsyms/Frekvencni_Terapie_App/actions/runs/41227310293

### Tagy, releases a produkční ověření

- Veřejné repozitáře `badlsyms/artefakt`, `badlsyms/artefaktlab` a `badlsyms/Frekvencni_Terapie_App`: GitHub API vrátilo prázdné seznamy Releases; namespace Git tagů vrátil 404 (žádné tag refs). Releases: https://api.github.com/repos/badlsyms/artefakt/releases, https://api.github.com/repos/badlsyms/artefaktlab/releases, https://api.github.com/repos/badlsyms/Frekvencni_Terapie_App/releases
- Soukromý repozitář `badlsyms/mv1-lab` a soukromé OCCO snapshoty: úplný seznam tagů/releases nebylo možné v tomto běhu přes veřejný endpoint ověřit; předchozí hodnoty zůstávají zachované, aktuální kontrola této položky je NEÚPLNÁ.
- Tři repozitáře `badlsyms/QO`, `badlsyms/freqTherapy` a `badlsyms/freq` stále nemají Git obsah; GitHub API vrací chybu 409 „Git Repository is empty“ při výpisu commitů.
- Produkční homepage a aktualizační katalog na Webzdarma nebylo možné 8. 11. 2026 načíst přes dostupný webový přístup. Produkční verze webů, Cloud Run runtime a skutečné nasazení aplikací zůstávají NEOVĚŘENO.

### Nezměněné verze a neověřené projekty

- MV-1 main: 1.65 / versionCode 165; main build unsigned. MV-1 1.83 a 1.72 zůstávají v nesloučených PR.
- XYQ main: Android 0.14.0 / versionCode 17; web manifest 0.10.0. XYQ 0.18.1 zůstává v nesloučeném draft PR.
- TRACE: 1.3-ci / code 13; úspěšný debug APK build po opravě CI, nikoli produkční podpis.
- OCCO Studio: poslední doložený release APK zůstává 4.7.1 / code 471; nový AAB, fyzický test ani produkční deployment nebyly doloženy.
- Frekvenční Terapie: package metadata 1.0.0; CI webové testy úspěšné, žádný ověřený APK/AAB.
- 0L8, PSYCHON 2/3, FOR+BEZ, ASHfall, CAMERA HUNT AR, sWEEDS, MAJTELAB, ARTEFAKT AGENT, OCB Device Manager/EventOps, 4UD10, ASV BODECH, SCAFFXGRAM, RXTX, SPEQTR/HALO, IN MASTER-SAVE, WHIQ, Legorider, Music 2073, SLYPH LAB, REIN/TENT, 4BO Replay, SIGNAL BELOW, TROL8 Synthlab, EventLog, FIQ, OCCO+OpenDAW, ROK Včas, Triton Taktile Editor a QIP zůstávají bez nové ověřitelné vazby na zdrojový repozitář nebo vydávací artefakt; jejich stav je NEOVĚŘENO.

## Blokery a rizika

1. Chybí potvrzené produkční nasazení veřejného katalogu na HTTPS.
2. Chybí produkční Ed25519 podpisový klíč a ověřený podepsaný katalog.
3. XYQ update pilot je vypnutý; nepodporuje zatím automatickou instalaci a nemá dokončenou kompatibilitu Ed25519 pro Android API 29–32.
4. Pro MV-1 a XYQ je poslední dohledaný main build unsigned; pro TRACE je dostupný pouze debug podpis.
5. U většiny projektů chybí podepsané APK/AAB, certifikátová kontinuita, fyzické testy a potvrzené produkční nasazení.
6. U OCCO 4.7.1 je doložený release APK a podpis, ale není doložen AAB, fyzická instalace ani aktuální produkční nasazení.
7. Dokumentace MV-1 a OCCO obsahuje zastaralé údaje (MV-1 README 1.64 vs. Gradle/build 1.65; OCCO BUILD_CZ 4.0.0 vs. Gradle/build 4.7.1).
8. Tři dostupné repozitáře QO, freqTherapy a freq jsou prázdné; pro ostatní projekty není v dostupných repozitářích jednoznačná vazba.
9. U několika názvů z fotografie není potvrzeno, zda jde o stejný projekt jako některý nalezený repozitář.

## Historie změn registru

### 2026-11-08 — ranní kontrola
- Aktualizován auditní stav registru; všech 10 dostupných repozitářů znovu zkontrolováno a stránkování dokončeno.
- Potvrzena oprava TRACE Android SDK workflow na main a úspěšný debug APK build 42210300364; verze aplikace zůstává 1.3-ci / code 13.
- Ověřeny aktuální stavy PR: Update Center #1 stále draft; MV-1/XYQ PR #1–#10 stále otevřené a nesloučené; Nucleus a Frekvenční Terapie PR #1 otevřené.
- Na draft větvi Update Center potvrzeny Ed25519 signovací nástroj, ephemeral-key testy, Webzdarma deployment návod a připravená informační stránka; CI validace i podpisové testy úspěšné. Katalog je stále prázdný a nic není nasazeno.
- Veřejné repozitáře artefakt, artefaktlab a Frekvencni_Terapie_App nemají GitHub Releases ani tag refs; soukromé repozitáře nebylo možné v tomto běhu úplně ověřit přes veřejný endpoint.
- Produkční web a katalog se nepodařilo načíst; stav produkčního nasazení zůstává NEOVĚŘENO. Žádné vydání, deployment ani změna v jiném repozitáři nebyly provedeny.

### 2026-11-07 — ranní kontrola
- Prohlédnuto všech 10 repozitářů dostupných přes připojený GitHub účet.
- XYQ main potvrzen jako Android 0.14.0 / code 17 a web manifest 0.10.0; 0.18.1 zůstává draft PR.
- MV-1 main potvrzen jako 1.65 / code 165; 1.83 zůstává draft PR. Main build je unsigned.
- TRACE potvrzen jako 1.3-ci / code 13; úspěšný debug-signed APK build z 6. 11. 2026.
- Frekvenční Terapie má package metadata 1.0.0; testovací PR je otevřený a bez distribučních artefaktů.
- OCCO Studio 4.7.1 / code 471 má doložený úspěšný podepsaný release APK build včetně APK SHA-256 a podpisového certifikátu SHA-256.
- Přidán Můj Nucleus 2.2.0 jako repo-derived projekt; běžící Cloud Run verze zůstává neověřena.
- Zaznamenán MASTER LAB 3.0.0 debug artefakt z ne-main větve; vazba na MAJTELAB nepotvrzena.
- Sloučen přesný duplicitní řádek MV-1 Studio Pro v původní tabulce; ostatní nejasné názvy zachovány.
- Potvrzeny dokumentační nesrovnalosti MV-1 a OCCO.
- Produkční web a katalog nebyly dostupným webovým přístupem ověřeny; žádné nasazení ani změny v jiných repozitářích nebyly provedeny.

## Povinná pole při dalších aktualizacích

| Pole | Význam |
|---|---|
| project_id | Stabilní interní ID projektu |
| display_name | Kanonický název |
| repository | GitHub owner/repo nebo jiný zdroj |
| source_version | Verze z manifestu/zdrojového kódu |
| latest_build | Poslední úspěšné sestavení, větev a commit |
| web_version | Verze webové aplikace/PWA |
| apk_version / apk_versionCode | Android APK |
| aab_version / aab_versionCode | Android App Bundle |
| artifact_sha256 | SHA-256 samotného souboru APK/AAB, ne ZIP obalu |
| signing_status / certificate_sha256 | Podpis a identita klíče; nikdy neukládat soukromý klíč ani heslo |
| test_status | Automatické a fyzické testy odděleně |
| production_version | Verze skutečně nasazená na produkci |
| production_url | Veřejná adresa |
| last_verified_at | Čas posledního ověření |
| evidence | Odkaz na commit, release, CI běh, artefakt nebo server |
| notes | Blokery a neověřené body |

## Další kroky

1. Přiřadit ke každému projektu kanonický repozitář a produkční URL.
2. Doplnit chybějící repozitáře a zdrojové manifesty pro projekty označené NEOVĚŘENO.
3. Ověřit produkční weby a Cloud Run runtime zvlášť od GitHubu.
4. U každé aplikace ověřit APK/AAB, package ID, versionCode, podpisový certifikát a SHA-256 přímo z binárního artefaktu.
5. Doložit fyzické testy a skutečnou produkční instalaci.
6. Teprve poté označit konkrétní verzi jako vydanou nebo produkční.


## Kontrola — 9. 11. 2026, 06:11 Europe/Prague

### Výsledek běhu

**Nebyla zjištěna žádná nová vydaná verze ani nový produkční release proti kontrole 8. 11. 2026.** Změny od poslední kontroly se týkají pouze předchozího zápisu registru v repozitáři `badlsyms/artefakt`; ostatní zdrojové repozitáře nemají novější main commit. Všechny verze níže zůstávají oddělené od otevřených PR, preview a debug buildů.

### Inventura repozitářů a poslední main commit

Seznam repozitářů dostupných přes připojený GitHub účet byl načten znovu. Celkem 10:

| Repozitář | Nejnovější commit / stav |
|---|---|
| `badlsyms/artefakt` | `ea70a943b782db5ce83acdcc3f5ff88baa65fd89`, 8. 11. 2026 06:00:29 UTC — předchozí aktualizace tohoto registru. [Commit](https://github.com/badlsyms/artefakt/commit/ea70a943b782db5ce83acdcc3f5ff88baa65fd89) |
| `badlsyms/mv1-lab` | `8fdad22371061908329cca816d36ae3e6a8adac6`, 19. 10. 2026 04:51:09 UTC. [Commit](https://github.com/badlsyms/mv1-lab/commit/8fdad22371061908329cca816d36ae3e6a8adac6) |
| `badlsyms/artefaktlab` | `26bc2efe334add10236e9c0d5b3194c88b0fdc30`, 6. 11. 2026 11:26:43 UTC — oprava instalace Android SDK v TRACE CI. [Commit](https://github.com/badlsyms/artefaktlab/commit/26bc2efe334add10236e9c0d5b3194c88b0fdc30) |
| `badlsyms/Frekvencni_Terapie_App` | `6c9a1cccfcccc6607ed81f03fb80320bc89107c7`, 9. 9. 2025 21:40:01 UTC — Initial commit. [Commit](https://github.com/badlsyms/Frekvencni_Terapie_App/commit/6c9a1cccfcccc6607ed81f03fb80320bc89107c7) |
| `badlsyms/occo-studio-v471-signed-20260814-235417` | `2ab626ff1e2b3d00f2e2d9a93e733fb5ea3e50e9`, 14. 8. 2026 21:54:17 UTC. [Commit](https://github.com/badlsyms/occo-studio-v471-signed-20260814-235417/commit/2ab626ff1e2b3d00f2e2d9a93e733fb5ea3e50e9) |
| `badlsyms/occo-studio-v460-build-20260814-115954` | `6463ecf1d84fb72760b46266ef021d5824e775ba`, 14. 8. 2026 09:59:54 UTC. [Commit](https://github.com/badlsyms/occo-studio-v460-build-20260814-115954/commit/6463ecf1d84fb72760b46266ef021d5824e775ba) |
| `badlsyms/occo-mv1-android-build-20260814-041816` | `5131617aec2202c159321723e550cd22b090b991`, 14. 8. 2026 02:18:15 UTC. [Commit](https://github.com/badlsyms/occo-mv1-android-build-20260814-041816/commit/5131617aec2202c159321723e550cd22b090b991) |
| `badlsyms/QO` | Prázdný Git repozitář; API vrací HTTP 409 při výpisu commitů. |
| `badlsyms/freqTherapy` | Prázdný Git repozitář; API vrací HTTP 409 při výpisu commitů. |
| `badlsyms/freq` | Prázdný Git repozitář; API vrací HTTP 409 při výpisu commitů. |

### Git tagy a GitHub Releases

- GitHub Releases: prázdné seznamy v repozitářích `artefakt`, `artefaktlab`, `Frekvencni_Terapie_App`, `mv1-lab` a ve třech OCCO snapshot repozitářích.
- Git tag refs: prázdné seznamy u všech 7 neprázdných repozitářů.
- `QO`, `freqTherapy` a `freq` jsou prázdné repozitáře; nelze z nich doložit tag, release ani zdrojovou verzi.
- Nebyl nalezen žádný nový tag ani GitHub Release. Stav zdrojových verzí z předchozího oddílu zůstává beze změny.

### GitHub Actions — poslední ověřené běhy

| Repozitář / aplikace | Poslední relevantní běh | Výsledek a interpretace |
|---|---|---|
| `artefaktlab` / TRACE | [Run 42210300364](https://github.com/badlsyms/artefaktlab/actions/runs/42210300364), main push, 6. 11. 2026 | Success. TRACE 1.3-ci / code 13; artefakt je debug-signed APK, ne produkční vydání. Předchozí run [42210196648](https://github.com/badlsyms/artefaktlab/actions/runs/42210196648) skončil failure. |
| `artefaktlab` / MASTER LAB | [Run 42211163271](https://github.com/badlsyms/artefaktlab/actions/runs/42211163271), větev `masterlab-android-v2-1-build`, 6. 11. 2026 | Success, ale pouze Android signed-debug artefakt z ne-main větve. Není to důkaz produkčního vydání ani potvrzení vazby na MAJTELAB. |
| `mv1-lab` / MV-1 + XYQ main | [Run 39200811788](https://github.com/badlsyms/mv1-lab/actions/runs/39200811788), main push, 19. 10. 2026 | Success. MV-1 1.65 a XYQ Android 0.14.0; workflow vytvořilo unsigned APK. Následující main run [39200598058](https://github.com/badlsyms/mv1-lab/actions/runs/39200598058) skončil failure, ale novější úspěšný main run 39200811788 zůstává platným posledním úspěšným sestavením. |
| `mv1-lab` / XYQ update pilot | [Run 42209053542](https://github.com/badlsyms/mv1-lab/actions/runs/42209053542), PR větev, 6. 11. 2026 | Success po několika neúspěšných pokusech. Je to pouze CI kontrola draft PR #10; nevytvořila produkční distribuční release a pilot je vypnutý. |
| `artefakt` / Update Center | [Run 42210773201](https://github.com/badlsyms/artefakt/actions/runs/42210773201) a [run 42210772928](https://github.com/badlsyms/artefakt/actions/runs/42210772928), PR větev, 6. 11. 2026 | Obě kontroly success: katalogové schéma/JS syntaxe a testy podpisu katalogu. PR #1 je stále draft; katalog má `apps: []` a není nasazen. |
| `Frekvencni_Terapie_App` | [Run 41227310293](https://github.com/badlsyms/Frekvencni_Terapie_App/actions/runs/41227310293), PR větev, 31. 10. 2026 | Success, ale pouze webové testy na nesloučené PR větvi. Žádné nové main buildy, APK/AAB ani fyzický Android test. |
| OCCO Studio 4.7.1 | [Run 31844439451](https://github.com/badlsyms/occo-studio-v471-signed-20260814-235417/actions/runs/31844439451), main, 14. 8. 2026 | Success; doložené podepsané release APK 4.7.1 / code 471. Od poslední kontroly žádný nový build. |
| OCCO Studio 4.6.0 | [Run 31790415967](https://github.com/badlsyms/occo-studio-v460-build-20260814-115954/actions/runs/31790415967), master, 14. 8. 2026 | Success; starší APK snapshot. |
| OCCO MV-1 Android 2.3.1 | [Run 31763323107](https://github.com/badlsyms/occo-mv1-android-build-20260814-041816/actions/runs/31763323107), master, 14. 8. 2026 | Success; starší APK snapshot. |

### Stav otevřených Pull Requests

- `badlsyms/artefakt`: PR #1 „ARTEFAKT UPDATE CENTER v1“ zůstává open/draft, naposledy aktualizován 6. 11. 2026. [PR #1](https://github.com/badlsyms/artefakt/pull/1)
- `badlsyms/mv1-lab`: PR #1–#10 zůstávají open a nesloučené. #1, #2 a #5 nejsou draft; #3, #4, #6, #7, #8, #9 a #10 jsou draft. Zejména MV-1 1.83 v PR #4, XYQ 0.18.1 v PR #9 a XYQ updater pilot v PR #10 nejsou vydané verze. [Otevřené PR](https://github.com/badlsyms/mv1-lab/pulls)
- `badlsyms/artefaktlab`: PR #1 pro Můj Nucleus zůstává open, nesloučený. [PR #1](https://github.com/badlsyms/artefaktlab/pull/1)
- `badlsyms/Frekvencni_Terapie_App`: PR #1 zůstává open, nesloučený. [PR #1](https://github.com/badlsyms/Frekvencni_Terapie_App/pull/1)

### Produkční web a aktualizační katalog

Přes webový přístup nebylo možné načíst:
- https://artefakt-lab.wz.cz/
- https://artefakt-lab.wz.cz/projects
- https://artefakt-lab.wz.cz/updates/v1/catalog.json

Výsledek je **NEOVĚŘENO / webový přístup nedostupný**; nelze z toho vyvozovat, že server je vypnutý. Veřejný katalog Update Center zůstává pouze v nesloučeném draft PR #1. Není doložen produkční podepsaný katalog, nasazení, aktivní updater ani aktualizace koncových zařízení.

### Závěr a neověřené projekty

- Proti 8. 11. nebyla zjištěna nová zdrojová verze, nový úspěšný main build, nový tag ani nový release.
- MV-1 main zůstává 1.65 / code 165; XYQ main Android 0.14.0 / code 17 a web 0.10.0; TRACE 1.3-ci / code 13; OCCO Studio 4.7.1 / code 471; Frekvenční Terapie package 1.0.0.
- Žádný nový AAB, produkční podpis, fyzický test nebo produkční deployment nebyl doložen.
- Bez nové ověřitelné vazby na zdrojový repozitář nebo artefakt zůstávají: 0L8, PSYCHON 2/3, FOR+BEZ, ASHfall, CAMERA HUNT AR, sWEEDS, MAJTELAB, ARTEFAKT AGENT, OCB Device Manager, OCB EventOps, 4UD10, ASV BODECH, SCAFFXGRAM, RXTX, SPEQTR/HALO, IN MASTER-SAVE, WHIQ, Legorider, Music 2073, SLYPH LAB, REIN/TENT, 4BO Replay, SIGNAL BELOW, TROL8 Synthlab, EventLog, FIQ, OCCO+OpenDAW, ROK Včas, Triton Taktile Editor V1/V2 a QIP.
- Žádné vydání, nasazení, mazání ani změny v jiném repozitáři nebyly provedeny.

### Historie změn registru

#### 2026-11-09 — ranní kontrola
- Znovu načteno všech 10 repozitářů dostupných přes připojený GitHub účet; tři repozitáře zůstávají prázdné.
- Potvrzeny poslední main commity; od předchozí kontroly se změnil pouze commit registru v `badlsyms/artefakt`, nikoli zdrojové repozitáře aplikací.
- U 7 neprázdných repozitářů potvrzeny prázdné seznamy Git tag refs a GitHub Releases.
- Znovu ověřeny relevantní GitHub Actions běhy; TRACE main build success, MV-1/XYQ main build z 19. 10. stále poslední úspěšný, XYQ updater a Update Center zůstávají jen PR CI kontroly.
- Znovu ověřeny otevřené PR; všechny zůstávají nesloučené, žádná rozpracovaná verze nebyla označena za vydanou.
- Produkční Webzdarma homepage, projects stránka a aktualizační katalog nebyly přes webový přístup dostupné; produkční stav zůstává NEOVĚŘENO.
- Nebyla provedena žádná změna mimo tento soubor registru; nebylo provedeno vydání ani deployment.
