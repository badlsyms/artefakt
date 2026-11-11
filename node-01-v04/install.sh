#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail
pkg install -y python
BASE="$HOME/artefakt-node-01"
SRC="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$BASE" "$HOME/.termux/boot"
cp "$SRC/watchdog.py" "$BASE/watchdog.py"
python -m py_compile "$BASE/watchdog.py"
# Keep v0.3 worker intact; replace boot hook to start only independent watchdog.
cat > "$HOME/.termux/boot/20-artefakt-node" <<'BOOT'
#!/data/data/com.termux/files/usr/bin/bash
export PATH="/data/data/com.termux/files/usr/bin:$PATH"
BASE="$HOME/artefakt-node-01"
nohup python -u "$BASE/watchdog.py" >> "$BASE/watchdog.log" 2>&1 </dev/null &
BOOT
chmod 700 "$HOME/.termux/boot/20-artefakt-node"
echo "v0.4 watchdog installed; existing v0.3 worker remains running."
echo "Start watchdog now: ~/.termux/boot/20-artefakt-node"
