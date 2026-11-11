#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail
pkg install -y python git
BASE="$HOME/artefakt-node-01"
mkdir -p "$BASE" "$HOME/.termux/boot"
cp "$(dirname "$0")/node.py" "$BASE/node.py.new"
python -m py_compile "$BASE/node.py.new"
if [ -f "$BASE/worker.pid" ]; then
 PID="$(cat "$BASE/worker.pid")"
 if [ -n "$PID" ] && kill -0 "$PID" 2>/dev/null; then
  kill "$PID" || true
  sleep 3
 fi
fi
mv "$BASE/node.py.new" "$BASE/node.py"
if [ ! -f "$BASE/config.json" ]; then cp "$(dirname "$0")/config.json" "$BASE/config.json"; fi
cat > "$HOME/.termux/boot/20-artefakt-node" <<'BOOT'
#!/data/data/com.termux/files/usr/bin/bash
export PATH="/data/data/com.termux/files/usr/bin:$PATH"
BASE="$HOME/artefakt-node-01"
if [ -f "$BASE/worker.pid" ]; then
 PID="$(cat "$BASE/worker.pid")"
 if [ -n "$PID" ] && kill -0 "$PID" 2>/dev/null; then exit 0; fi
fi
nohup python -u "$BASE/node.py" >> "$BASE/worker.log" 2>&1 </dev/null &
echo $! > "$BASE/worker.pid"
BOOT
chmod 700 "$HOME/.termux/boot/20-artefakt-node"
echo "Installed v0.3"
