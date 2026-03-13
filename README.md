# Linux Security Checker

Linux Security Checker is a simple command-line tool that audits basic security settings on a Linux system.
It helps users quickly identify common security issues such as open ports, insecure SSH configuration, and missing firewall protection.

The tool also includes **basic malware detection** using both **signature-based** and **hash-based scanning**.

---

## Features

* Check firewall status
* Detect open network ports
* Verify SSH root login configuration
* Calculate a basic security score
* Scan files for malware using text signatures
* Detect malware using SHA256 hash comparison
* Modular architecture for easier maintenance and scalability
* Command-line interface with help support

---

## Project Structure

```
linux-security-checker
│
├── security_checker.py
├── signatures.txt
├── hash_signatures.txt
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
├── .gitignore
└── test.txt
```

Each module inside the `checks` directory performs a specific security check, which improves maintainability and scalability.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ARNOX-13/linux-security-checker.git
```

Move into the project directory:

```bash
cd linux-security-checker
```

Run the program:

```bash
python3 security_checker.py
```

---

## Usage

### Run system security checks

```bash
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

## Malware Detection

The tool performs **two types of malware detection**.

### Signature-Based Detection

The program checks file contents against known malware signatures stored in:

```
signatures.txt
```

If a match is found, the file is flagged as potentially malicious.

---

### Hash-Based Detection

The tool also calculates the **SHA256 hash** of scanned files and compares it against known malicious hashes stored in:

```
hash_signatures.txt
```

This technique is commonly used by antivirus software to detect known malware samples.

---

## Why This Project?

Many Linux beginners are unfamiliar with basic system security checks.
This project aims to provide a simple tool that helps users audit important security settings and understand potential vulnerabilities on their system.

The modular design also allows developers to easily extend the tool with additional security checks.

---

## Future Improvements

Possible enhancements include:

* Colored CLI output for better readability
* Additional security checks (system updates, weak passwords, etc.)
* JSON or HTML report export
* Integration with larger malware signature databases

---

## License

This project is licensed under the MIT License.
