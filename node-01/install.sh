#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail
pkg update -y
pkg install -y python git
BASE="$HOME/artefakt-node-01"
mkdir -p "$BASE" "$HOME/.termux/boot"
cp node.py config.json "$BASE/"
cat > "$HOME/.termux/boot/20-artefakt-node" <<'BOOT'
#!/data/data/com.termux/files/usr/bin/bash
export PATH="/data/data/com.termux/files/usr/bin:$PATH"
BASE="$HOME/artefakt-node-01"
if [ -f "$BASE/worker.pid" ] && kill -0 "$(cat "$BASE/worker.pid")" 2>/dev/null; then exit 0; fi
nohup python "$BASE/node.py" >> "$BASE/worker.log" 2>&1 </dev/null &
echo $! > "$BASE/worker.pid"
BOOT
chmod 700 "$HOME/.termux/boot/20-artefakt-node"
echo "Installed. Open Termux:Boot once and run ~/.termux/boot/20-artefakt-node"
