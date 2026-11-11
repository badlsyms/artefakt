# Artefakt Node 01 — Redmi 15C pilot
Read-only monitoring node. Checks public Artefakt Lab and GitHub HTTPS URLs every 15 minutes, writes local status.json and events.jsonl. No credentials, no paid APIs, no remote command execution.
## Installation
Install Termux and Termux:Boot from F-Droid (same signing source). Open Termux:Boot once.
In Termux:
```sh
pkg install git -y
git clone -b feature/node-01-redmi15c https://github.com/badlsyms/artefakt.git
cd artefakt/node-01
bash install.sh
~/.termux/boot/20-artefakt-node
cat ~/artefakt-node-01/status.json
```
Reboot and check status. Disable battery restrictions/autostart limits for Termux and Termux:Boot as needed. Android may still kill background processes.
Stop with `kill "$(cat ~/artefakt-node-01/worker.pid)"`; remove boot script to disable.
This does not access private GitHub repos or sync Supabase. Future authenticated integration requires a low-privilege API and device enrollment. Do not store Supabase service-role tokens on the phone.
