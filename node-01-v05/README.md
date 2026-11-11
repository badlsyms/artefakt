# Artefakt Node 01 v0.5 – remote foundation (design stage)
## Verified
Supabase project **WorkLog Cloud Core** (eu-central-1) is available. Existing public tables are WorkLog business data. No schema changes have been applied.
## Architecture
Redmi v0.3 worker + v0.4 watchdog → bounded local spool (future) → HTTPS edge ingestion endpoint (future) → isolated `artefakt_nodes` / `artefakt_node_heartbeats` tables → owner-authenticated dashboard (future).
## Security gate
1. Use device enrollment with a randomly generated per-device secret stored only on Redmi, hashed server-side.
2. Validate authorization at the edge; bind device identity to a registered node and enforce request size, rate limits, and replay resistance.
3. Edge function alone may use privileged database access; never distribute service_role/secret to phone or browser.
4. Public tables use RLS and owner-only SELECT. No anonymous writes.
5. Disable remote shell and arbitrary commands. Remote job queue requires a separate allowlist and approvals.
## Costs
No paid AI API is introduced. Verify current Supabase quota before enabling ingestion. Local worker continues even if cloud fails.
## Next steps
- [ ] Approve isolation and ownership model
- [ ] Deploy SQL after review and run security advisors
- [ ] Implement edge ingestion and enrollment
- [ ] Implement local bounded retry spool
- [ ] Dashboard + offline detection + 24-hour soak test
