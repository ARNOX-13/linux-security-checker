# Linux Security Checker

Linux Security Checker is a Python-based tool that performs basic security auditing on Linux systems.
It provides both a **Command Line Interface (CLI)** and a **Web Interface**, making it easy for users to analyze system security and scan files for potential malware.

---

## Features

* Check firewall status
* Detect open network ports
* Verify SSH root login configuration
* Calculate a basic security score
* Scan files using signature-based malware detection
* Detect malware using SHA256 hash comparison
* Modular architecture for easy scalability
* Web-based interface using Flask

---

## Project Structure

```
linux-security-checker
│
├── app.py
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
├── templates
│   └── index.html
│
├── static
│   └── style.css
│
├── README.md
├── LICENSE
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ARNOX-13/linux-security-checker.git
cd linux-security-checker
```

Install dependencies:

```bash
pip install flask colorama
```

---

## Usage

### CLI Mode

Run system security checks:

```bash
python3 security_checker.py
```

Scan a file:

```bash
python3 security_checker.py --scan-file example.txt
```

View help:

```bash
python3 security_checker.py --help
```

---

### Web Interface

Run the Flask app:

```bash
python3 app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

You can:

* Run system security scans
* Upload files for malware scanning
* View results in a clean interface

---

## Malware Detection

### Signature-Based Detection

The tool checks file content against known signatures stored in:

```
signatures.txt
```

---

### Hash-Based Detection (SHA256)

The tool calculates the SHA256 hash of files and compares it against:

```
hash_signatures.txt
```

This method is commonly used in antivirus systems.

---

## Why This Project?

Many Linux users are unaware of basic system security risks.
This tool provides a simple way to:

* audit system configurations
* detect insecure settings
* identify potentially malicious files

It also demonstrates core cybersecurity concepts such as system auditing and malware detection.

---

## Future Improvements

* JSON report export
* Colored CLI output
* Additional security checks
* Integration with larger malware signature databases
* Online deployment of web interface

---

## License

This project is licensed under the MIT License.
