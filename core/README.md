# Artefakt Lab Core — pilot

Tato větev zavádí základní registr projektů a automatickou validaci. **Nejde o hotový autonomní vývojový systém.**

- `projects.json`: strojově čitelný registr; `discovered` potvrzuje jen existenci repozitáře, ne funkčnost aplikace.
- Workflow kontroluje validitu registru a vytváří auditní výstup. Neprovádí placená API volání ani publikaci.
- Produkční publikace, mazání dat, změny přístupových práv a podepisování release APK vyžadují samostatné schválení.
- Existující Supabase `WorkLog Cloud Core` patří WorkLogu; bez dalšího návrhu schématu do něj nezapisujeme.

Další kroky: doplnit skutečné zdroje projektů, stav sestavení, testovací výsledky a následně zabezpečenou frontu agentních úloh.
