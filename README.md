# 🔐 Linux Security Checker

A lightweight cybersecurity auditing tool that performs basic Linux security checks through a CLI interface, with an optional web-based file scanner.

Designed for beginners and security enthusiasts, this tool provides insights into system security, process behavior, and privilege risks in a simple and understandable format.

---

## 🚀 Project Overview

Linux Security Checker is a modular security auditing tool that analyzes a system across multiple layers:

- Network security configuration
- Running processes and suspicious activity
- User privileges and potential risks
- File-based malware detection

The tool is built with a CLI-first approach for full system analysis, while the web interface provides a simplified file scanning demo.

---

## 🏗️ Architecture

### 🔹 CLI Tool (Core System)
- Main entry point: security_checker.py
- Executes all system-level checks
- Provides detailed analysis and scoring
- Designed for real Linux environments

---

### 🌐 Web Interface (Flask)
- File: app.py
- Purpose: File scanning only
- Runs in restricted environments (e.g., cloud)
- Does NOT perform system-level checks

---

### 📦 Modular Design (checks/)

Each security component is isolated:

checks/
├── firewall_check.py
├── port_check.py
├── ssh_check.py
├── process_check.py
├── privilege_check.py
├── file_scan.py
├── env_check.py

---

## ⚙️ How It Works

The tool performs multi-layer security analysis:

🔐 Network Security
- Firewall status
- Open ports
- SSH root login configuration

⚙️ Process Analysis
- Total running processes
- Root-owned processes
- Detection of suspicious commands (reverse shells, payloads)

🧑‍💻 Privilege Analysis
- Current user privileges
- Group memberships
- Sudo access
- Dangerous group detection

🦠 File Scanning
- Signature-based detection
- SHA256 hash matching
- Detection of suspicious patterns (e.g., encoded payloads)

---

## ✨ Features

- Modular architecture
- Signature + hash-based malware detection
- Process-level behavioral analysis
- Privilege escalation risk detection
- Environment-aware execution
- Balanced and explainable scoring system
- Clean CLI output (audit-style)
- Minimal web UI for file scanning

---

## 📊 Scoring System

The tool uses a severity-based scoring model (0–10):

Low      → -0.5  
Medium   → -1  
High     → -2  
Critical → -3  

Example:

Score: 6.5/10

Reason:
- Firewall is inactive (High impact)
- Open ports detected (Medium impact)
- SSH root login enabled (Critical impact)

✔ Prevents unfair scoring  
✔ Provides clear reasoning  
✔ Reflects real-world risk levels  

---

## 🌍 Environment Awareness

The tool detects whether it is running in:

- Local system (full access)
- Restricted environment (cloud/container)

Behavior:
- Skips unsupported checks  
- Avoids misleading errors  
- Displays informative messages  

---

## ⚠️ Limitations

- Some checks require root privileges  
- Cloud environments may restrict system access  
- Detection is signature-based (not AI/behavioral)  
- False positives possible in process detection  

---

## 🛠️ Installation

git clone https://github.com/ARNOX-13/linux-security-checker.git  
cd linux-security-checker  

---

## ▶️ Usage

Run full system scan:
sudo python3 security_checker.py  

Scan a file:
python3 security_checker.py --scan-file <filename>  

Export report:
python3 security_checker.py --export-json  

Run web interface:
python3 app.py  

Open:
http://127.0.0.1:5000  

---

## 📌 Example Output

=== Linux Security Checker ===

=== Network Security ===
[!] Firewall Status      : INACTIVE
[✗] SSH Root Login      : ENABLED

=== Process Analysis ===
[+] Total Processes     : 406
[!] Root Processes      : 299 (High)

[!] Suspicious Processes Detected: 21
    → nc -lvp 4444
    → bash -i
    → sh -i

=== Privilege Analysis ===
[✗] Current User        : root
[✗] Sudo Privileges     : ENABLED

=== Final Security Score ===
Score: 6.5/10

Reason:
- SSH root login enabled (Critical impact)
- Suspicious processes detected (High impact)

---

## 🎯 Future Improvements

- Advanced behavioral analysis  
- Whitelisting to reduce false positives  
- Integration with real threat intelligence feeds  
- Dashboard-based UI  

---

## 📜 License

MIT License  

---

## 👤 Author

Arnav  
Cybersecurity Enthusiast | Developer  

---

## ⭐ Final Note

This project focuses on making basic Linux security auditing accessible and understandable, while maintaining a structure inspired by real-world security tools.
