#!/usr/bin/env python3
import http.server
import subprocess
import os

PORT = 8082

class VRTriggerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/reset':
            # Dynamically resolve the local user's home path for portability
            script_path = os.path.expanduser('~/.local/bin/reset-vr')
            subprocess.run(["/bin/bash", script_path])

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>SteamVR Link Pipeline Reset</title>
                <style>
                    body {
                        background-color: #171d25;
                        color: #c7d5e0;
                        font-family: "Motiva Sans", "Arial", "Helvetica", sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        overflow: hidden;
                    }
                    .steam-container {
                        background: radial-gradient(circle at top left, #2a475e 0%, #1b2838 80%);
                        border: 1px solid #3b6484;
                        border-radius: 4px;
                        padding: 40px;
                        text-align: center;
                        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.7), 0 0 15px rgba(102, 192, 244, 0.1);
                        max-width: 420px;
                        width: 85%;
                    }
                    .icon-box { margin-bottom: 25px; }
                    .pulse-ring {
                        width: 75px;
                        height: 75px;
                        background: #a3cf06;
                        border-radius: 50%;
                        display: inline-flex;
                        justify-content: center;
                        align-items: center;
                        box-shadow: 0 0 20px rgba(163, 207, 6, 0.6);
                        animation: pulse 2s infinite alternate ease-in-out;
                    }
                    .checkmark { color: #171d25; font-size: 36px; font-weight: bold; line-height: 75px; user-select: none; }
                    @keyframes pulse {
                        0% { box-shadow: 0 0 12px rgba(163, 207, 6, 0.4); transform: scale(0.97); }
                        100% { box-shadow: 0 0 28px rgba(163, 207, 6, 0.9); transform: scale(1.03); }
                    }
                    h1 { color: #66c0f4; font-size: 20px; font-weight: 500; letter-spacing: 1.5px; margin: 0 0 12px 0; text-transform: uppercase; }
                    p { color: #8f98a0; font-size: 13px; line-height: 1.6; margin: 0 0 28px 0; }
                    .status-pill {
                        background: rgba(102, 192, 244, 0.08); color: #66c0f4; border: 1px solid rgba(102, 192, 244, 0.2);
                        padding: 8px 20px; border-radius: 2px; font-size: 11px; text-transform: uppercase; letter-spacing: 2px; display: inline-block; font-weight: bold;
                    }
                </style>
            </head>
            <body>
                <div class="steam-container">
                    <div class="icon-box"><div class="pulse-ring"><span class="checkmark">✓</span></div></div>
                    <h1>Pipeline Reset Complete</h1>
                    <p>Zombie VR processes have been forcefully cleared. Your host computer is primed for a fresh session.</p>
                    <div class="status-pill">Ready to Reconnect</div>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, VRTriggerHandler)
    print(f"Quest VR Trigger listening on port {PORT}...")
    httpd.serve_forever()