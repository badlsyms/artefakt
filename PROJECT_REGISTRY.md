# ARTEFAKT-LAB — Centrální registr verzí

> Poslední kontrola: 7. 11. 2026, 06:43 Europe/Prague.
> Rozsah: všech 10 repozitářů, které byly v této kontrole dostupné přes připojený GitHub účet.
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
