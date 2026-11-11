-- REVIEW ONLY. Do not execute until device identity/auth design is approved.
-- Separate tables; existing WorkLog tables untouched.
create table if not exists public.artefakt_nodes (
 id uuid primary key default gen_random_uuid(),
 owner_id uuid not null references auth.users(id) on delete cascade,
 label text not null,
 created_at timestamptz not null default now(),
 last_seen_at timestamptz
);
create table if not exists public.artefakt_node_heartbeats (
 id bigint generated always as identity primary key,
 node_id uuid not null references public.artefakt_nodes(id) on delete cascade,
 received_at timestamptz not null default now(),
 payload jsonb not null default '{}'::jsonb,
 constraint payload_object check (jsonb_typeof(payload)='object')
);
create index if not exists artefakt_heartbeats_node_time on public.artefakt_node_heartbeats(node_id,received_at desc);
alter table public.artefakt_nodes enable row level security;
alter table public.artefakt_node_heartbeats enable row level security;
revoke all on public.artefakt_nodes from anon, authenticated;
revoke all on public.artefakt_node_heartbeats from anon, authenticated;
grant select on public.artefakt_nodes to authenticated;
grant select on public.artefakt_node_heartbeats to authenticated;
create policy "owner reads nodes" on public.artefakt_nodes
 for select to authenticated using (owner_id=(select auth.uid()));
create policy "owner reads heartbeats" on public.artefakt_node_heartbeats
 for select to authenticated using (exists (
 select 1 from public.artefakt_nodes n where n.id=node_id and n.owner_id=(select auth.uid())
 ));
-- Ingestion only via verified server-side endpoint with per-device credentials,
-- NOT via browser/anon insert grants or a service-role key on the phone.
