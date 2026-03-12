# Linux Security Checker

Linux Security Checker is a simple command-line tool that audits basic security settings on a Linux system.
It helps beginners quickly identify common security issues such as open ports, insecure SSH configuration, and missing firewall protection.

The tool also includes a basic **signature-based malware scanner** that checks files against known malware signatures.

---

## Features

* Check firewall status
* Detect open network ports
* Verify SSH root login configuration
* Calculate a basic security score
* Scan files for known malware signatures
* Modular architecture for easy extension
* Command-line interface with help support

---

## Project Structure

```
linux-security-checker
│
├── security_checker.py
├── signatures.txt
│
├── checks
│   ├── __init__.py
│   ├── firewall_check.py
│   ├── port_check.py
│   ├── ssh_check.py
│   └── file_scan.py
│
├── README.md
├── LICENSE
└── .gitignore
```

Each module inside the `checks` directory performs a specific security check, making the project easier to maintain and extend.

---

## Installation

Clone the repository:

```
git clone https://github.com/ARNOX-13/linux-security-checker.git
```

Move into the project directory:

```
cd linux-security-checker
```

Run the tool:

```
python3 security_checker.py
```

---

## Usage

### Run system security checks

```
python3 security_checker.py
```

Example output:

```
=== Linux Security Checker ===

Firewall: Not detected
Open Ports: 5353
SSH root login: ENABLED

Security Score: 4/10
```

---

### Scan a file for malware signatures

```
python3 security_checker.py --scan-file example.txt
```

Example output:

```
Scanning file: example.txt
[!] Malware signature detected: EICAR
```

---

### View help menu

```
python3 security_checker.py --help
```

---

## Malware Signature Detection

The project uses a simple **signature-based detection system**.
Known malware signatures are stored inside:

```
signatures.txt
```

When scanning a file, the program compares its contents against the stored signatures and alerts the user if a match is found.

This concept is similar to how real antivirus tools perform basic malware detection.

---

## Why This Project?

Many Linux beginners are unfamiliar with basic system security checks.
This tool provides a simple way to quickly audit important security settings and understand potential vulnerabilities on their system.

The modular design also allows developers to easily add additional security checks in the future.

---

## License

This project is licensed under the MIT License.
