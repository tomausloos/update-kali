#!/bin/bash
set -Eeuo pipefail
trap "echo -e \"\033[1;31m[!] \e[0m Script error occured.\"" ERR

GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

# Function to check if a package is installed
is_installed() {
  dpkg -l | grep -q "$1"
}

# Install Terminator if not installed
if ! is_installed "terminator"; then
  echo "Terminator is not installed. Installing now..."
  sudo apt update
  sudo apt install -y terminator
else
  echo "Terminator is already installed."
fi

# Add Terminator to GNOME favorites (main bar)
if ! gsettings get org.gnome.shell favorite-apps | grep -q "terminator.desktop"; then
  echo "Adding Terminator to the main bar..."
  current_apps=$(gsettings get org.gnome.shell favorite-apps)
  new_apps=$(echo "$current_apps" | sed "s/]$/, 'terminator.desktop']/")
  gsettings set org.gnome.shell favorite-apps "$new_apps"
else
  echo "Terminator is already in the main bar."
fi

# Configure specific keyboard shortcuts for Terminator
echo "Configuring keyboard shortcuts for Terminator..."

# Set custom keybindings
# Split horizontally: Shift + Super + Right Arrow
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybindings "['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom2/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom3/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom4/']"

# Split vertically: Shift + Super + Down Arrow
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ name "Split Horizontally"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ command "terminator -e 'python -c \"import time; time.sleep(0.2);\"'"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ binding "<Shift><Super>Right"

# Open new tab: Shift + Alt + T
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ name "Open New Tab"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ command "terminator -e 'tab'"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ binding "<Shift><Alt>T"

# Move between tabs: Shift + Tab + Arrow Direction
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom2/ name "Move between tabs"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom2/ command "terminator --move-tab-to-direction"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom2/ binding "<Shift><Tab>Arrow"

echo "Keyboard shortcuts configured successfully."

echo "Setup complete. You may need to log out and log back in for some changes to take effect."
