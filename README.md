# Steam Link VR Boundary Recovery Utility for Linux

An automated, lightweight background service for Linux PCVR enthusiasts. This utility resolves the open issue where the Meta Quest headset drops or pauses its video stream upon exiting the Guardian boundary, causing the backend host processes (`vrserver`, `vrcompositor`, etc.) to enter an unrecoverable zombie state on Linux.

By deploying a native micro-webserver on your local runtime, you can instantly flush and clear the stuck streaming pipeline entirely inside VR using the native Meta Horizon Browser.

## Features
* **Zero-Interruption Cleanup:** Wipe frozen backend processes without leaving VR, restarting Steam, or taking off the headset.
* **Native Systemd Integration:** Runs completely headless as an isolated background user service.
* **Themed UX Dashboard:** Features a custom, dark-themed confirmation interface stylized to match the native Steam ecosystem.
* **Completely Portable:** Dynamically scales to fit any user context and home environment out of the box.

## Architecture Layout
~/.local/bin/reset-vr             # Bash cleanup script handling process execution
~/.local/bin/vr-web-trigger.py    # Python micro-web server processing webhooks
~/.config/systemd/user/           # Background daemon configuration environment


## Installation

1. Clone the repository to your local Linux machine:
bash
git clone [https://github.com/yourusername/steamlink-linux-recovery.git](https://github.com/yourusername/steamlink-linux-recovery.git)
cd steamlink-linux-recovery




2. Execute the included script installation binary:
```bash
chmod +x install.sh
./install.sh 
```



3. Verify that the background user execution daemon is active and green:
```bash
systemctl --user status vr-trigger.service
```





## Wireless Quest 3 Setup

1. Put on your Meta Quest headset and open the **Meta Horizon Browser**.
2. Determine your computer's internal network IP address (e.g., `192.168.0.XXX`) and navigate to:
`http://<YOUR_PC_IP>:8082/reset`
3. Once the stylized verification screen displays, open the browser options and select **Add page to library**.
4. Drag and drop the newly created app icon directly onto your universal bottom navigation dock for instant access.

---

## Credits & Attribution

* **Concept & Architecture:** Engineered in collaboration with **Gemini**, an AI companion by Google.
* **Active Bug Tracking Reference:** Solves community-reported edge behaviors relating to Valve's upstream SteamVR-for-Linux distribution engine.



