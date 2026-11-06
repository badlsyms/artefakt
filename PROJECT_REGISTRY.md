# ARTEFAKT-LAB — Centrální registr verzí

> Založeno 6. 11. 2026. Toto je počáteční inventura, nikoli tvrzení, že všechny verze jsou aktuálně vydané.
> „Nejnovější známá“ znamená poslední dohledaný údaj v dostupných podkladech. Bez ověřitelného artefaktu, tagu, manifestu nebo nasazení zůstává stav NEOVĚŘENO.

## Pravidla evidence

- Rozlišovat **rozpracovanou**, **sestavenou**, **podepsanou**, **otestovanou** a **produkčně nasazenou** verzi.
- Číslo verze se nesmí odvozovat z názvu PR, data commitu ani požadovaného cíle.
- APK a AAB evidovat odděleně; kontrolovat applicationId/package, versionName, versionCode, podpisový certifikát a SHA-256.
- Web evidovat podle manifestu/build metadat a skutečného produkčního nasazení.
- „Nejnovější commit“ není automaticky „nejnovější vydání“.
- Chybějící důkaz se zapisuje jako NEOVĚŘENO, nikdy se nedoplňuje odhadem.

## Souhrn

| Projekt | Verze z papírové evidence | Nejnovější dohledaný údaj | Stav ověření |
|---|---:|---:|---|
| 0L8 Suite | 0.32.7 | 0.32.7 (evidence uživatele) | Čeká na kontrolu repozitáře a produkce |
| XYQ Next | 0.17 (fotografie nejednoznačná) | 0.18.1, versionCode 22 v PR #9 | Rozpracovaný/preview; podpis a produkce nepotvrzeny |
| MV-1 Studio Pro | 1.78 | 1.83 v PR #4 | PR popisuje ověřené sestavení; produkční instalace samostatně nepotvrzena |
| PSYCHON 2 | 1.4.1 | — | NEOVĚŘENO |
| PSYCHON 3 | 0.7.2 | — | NEOVĚŘENO |
| FOR+BEZ | 1.0.0 | — | NEOVĚŘENO |
| ASHfall | — | — | NEOVĚŘENO |
| CAMERA HUNT AR | 10.0.0? | — | Číslo z fotografie nejisté; NEOVĚŘENO |
| sWEEDS | 2.11 | — | NEOVĚŘENO |
| MAJTELAB / MAJTELAB? | 2.80 | — | Název z fotografie nejasný; NEOVĚŘENO |
| XYQ + RXTX NEXT | 0.17 + 0.19? | XYQ 0.18.1 v PR #9 | RXTX samostatně NEOVĚŘENO |
| MV-1 Studio Pro | 1.78 | 1.83 v PR #4 | Viz hlavní záznam výše; možná duplicitní řádek |
| ARTEFAKT AGENT | 0.3.2 | — | NEOVĚŘENO |
| OCB Device Manager | 0.3.0 | — | NEOVĚŘENO; název z fotografie ověřit |
| OCB EventOps | 3.6.0 | — | NEOVĚŘENO; název z fotografie ověřit |
| 4UD10 | — | — | Název/verze z fotografie nejasné |
| ASV BODECH | 2.0.0 | — | Název z fotografie nejasný |
| TRACE (CAT) | 1.3.0 | — | NEOVĚŘENO |
| SCAFFXGRAM | 1.22 | — | NEOVĚŘENO; název z fotografie nejasný |
| RXTX | 0.3 | — | NEOVĚŘENO |
| SPEQTR + HALO | 1.1.0-1 | — | NEOVĚŘENO |
| IN MASTER-SAVE | 1.8.1? | — | Název/verze z fotografie nejasné |
| WHIQ (WHISTLER) | 1.1.1 | — | NEOVĚŘENO |
| Legorider | 0.3.0 | — | NEOVĚŘENO |
| Music 2073 | 0.12 | — | NEOVĚŘENO |
| SLYPH LAB | 2.1.0 | — | NEOVĚŘENO; název z fotografie nejasný |
| REIN/TENT | — | — | NEOVĚŘENO |
| 4BO Replay | — | — | NEOVĚŘENO |
| SIGNAL BELOW | — | — | NEOVĚŘENO |
| TROL8 Synthlab | — | — | NEOVĚŘENO |
| EventLog | — | — | NEOVĚŘENO |
| FIQ | — | — | NEOVĚŘENO |
| OCCO + OpenDAW | — | — | NEOVĚŘENO |
| FREQ Terapeut | — | — | NEOVĚŘENO |
| ROK Včas | — | — | NEOVĚŘENO |
| Triton Taktile Editor V1/V2 | — | — | NEOVĚŘENO |
| QIP | — | — | NEOVĚŘENO |

## Doložené podklady

- MV-1 Studio Pro 1.83: https://github.com/badlsyms/mv1-lab/pull/4
- XYQ 0.18.1 / versionCode 22: https://github.com/badlsyms/mv1-lab/pull/9
- XYQ Next sjednocení s RXTX: https://github.com/badlsyms/mv1-lab/pull/6
- XYQ bezpečná synchronizace a offline vydání: https://github.com/badlsyms/mv1-lab/pull/5

## Povinná pole při každé aktualizaci

| Pole | Význam |
|---|---|
| project_id | Stabilní interní ID projektu |
| display_name | Kanonický název |
| repository | GitHub owner/repo nebo jiný zdroj |
| source_version | Verze z manifestu/zdrojového kódu |
| latest_build | Poslední úspěšné sestavení |
| web_version | Verze webové aplikace |
| apk_version / apk_versionCode | Android APK |
| aab_version / aab_versionCode | Android App Bundle |
| signing_status / certificate_sha256 | Podpis a identita klíče; nikdy neukládat soukromý klíč ani heslo |
| test_status | Automatické a fyzické testy odděleně |
| production_version | Verze skutečně nasazená na produkci |
| production_url | Veřejná adresa |
| last_verified_at | Čas posledního ověření |
| evidence | Odkaz na commit, release, CI běh, artefakt nebo server |
| notes | Blokery a neověřené body |

## Další kroky

1. Přiřadit ke každému projektu kanonický repozitář a produkční URL.
2. Prohledat repozitáře, tagy/releases, manifests, package metadata a poslední CI artefakty.
3. Ověřit produkční server zvlášť od GitHubu.
4. Doplnit SHA-256 a podpis APK/AAB pouze z dostupných binárních artefaktů.
5. Zapnout pravidelnou aktualizaci a uchovávat historii změn.

