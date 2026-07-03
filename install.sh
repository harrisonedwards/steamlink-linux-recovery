#!/usr/bin/env bash
set -e

echo "📦 Installing Steam Link Linux Recovery Tool..."

# Create necessary local paths
mkdir -p "$HOME/.local/bin"
mkdir -p "$HOME/.config/systemd/user"

# Copy utilities into place
cp bin/reset-vr "$HOME/.local/bin/"
cp bin/vr-web-trigger.py "$HOME/.local/bin/"
cp vr-trigger.service "$HOME/.config/systemd/user/"

# Permissions management
chmod +x "$HOME/.local/bin/reset-vr"
chmod +x "$HOME/.local/bin/vr-web-trigger.py"

# Sanitize potential web carriage returns
sed -i 's/\r//g' "$HOME/.local/bin/reset-vr"
sed -i 's/\r//g' "$HOME/.local/bin/vr-web-trigger.py"

# Reload and enable the systemd daemon
echo "⚙️  Configuring background systemd service..."
systemctl --user daemon-reload
systemctl --user enable --now vr-trigger.service

# Automatically grab the primary active local IP address
LOCAL_IP=$(ip route get 1.1.1.1 2>/dev/null | grep -oP 'src \K\S+' || hostname -I | awk '{print $1}')

# Automatically grab the primary active local IP address
LOCAL_IP=$(ip route get 1.1.1.1 2>/dev/null | grep -oP 'src \K\S+' || hostname -I | awk '{print $1}')

echo ""
echo "======================================================="
echo "🎉       INSTALLATION COMPLETELY SUCCESSFUL!        🎉"
echo "======================================================="
echo ""
echo "  The background recovery daemon is running perfectly.   "
echo "  Put on your headset, open the Horizon Browser, and     "
echo "  navigate directly to this generated URL:               "
echo ""
echo "  👉   http://$LOCAL_IP:8082/reset   👈"
echo ""
echo "======================================================="
echo ""