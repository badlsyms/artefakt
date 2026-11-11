# Artefakt Node 01 v0.3
Local, read-only Termux worker. HTTPS checks every 15 minutes, heartbeat every ~60 seconds, delay tracking, single-instance lock. No credentials, Supabase writes, paid AI API, or remote shell.
## Upgrade
Install Termux and Termux:Boot from same trusted source. Open Termux:Boot once.
```sh
pkg install git -y
git clone -b feature/node-01-v03 https://github.com/badlsyms/artefakt.git ~/artefakt-v03
cd ~/artefakt-v03/node-01-v03
bash install.sh
~/.termux/boot/20-artefakt-node
sleep 5
cat ~/artefakt-node-01/heartbeat.json
```
If already cloned: `cd ~/artefakt-v03 && git pull`.
Note: Android may still delay background tasks. This version does not yet include independent watchdog or authenticated remote monitoring. It retains old history. Verify `pgrep -af node.py` to ensure the previous v0.1 worker stopped.
