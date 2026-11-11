# Artefakt Node 01 v0.4 – independent local watchdog

Adds a **separate Python watchdog** to existing v0.3 worker. It checks `heartbeat.json` modification time every 120 seconds; if older than 300 seconds or PID is missing, it restarts the worker, subject to a 10-minute cooldown and at most four restarts per hour. A file lock prevents duplicate watchdog loops.

This does **not** provide Supabase sync, remote control, APK tests, or 24/7 guarantees. Android can suspend both processes. For production reliability, use a platform scheduler / Android foreground service and an external heartbeat observer.

## Install on Redmi 15C
```sh
cd ~
git clone -b feature/node-01-v04-watchdog https://github.com/badlsyms/artefakt.git artefakt-v04
cd ~/artefakt-v04/node-01-v04
bash install.sh
~/.termux/boot/20-artefakt-node
sleep 5
pgrep -af 'node.py|watchdog.py'
tail -n 5 ~/artefakt-node-01/watchdog.jsonl
```

Termux:Boot must be installed and opened once. Existing worker is intentionally not restarted by installer. No secrets, no paid API calls.

**Caveat:** watchdog identifies worker by PID file; a stale/reused PID can cause false identification. For a future release validate process identity before sending SIGTERM. Do not use this version for critical infrastructure.
