# Linux Security Checker

Linux Security Checker is a simple CLI tool that scans basic security settings on a Linux system and provides a security score.

It helps beginners quickly audit important security configurations on their Linux machine.

---

## Features

- Detect firewall status
- List open network ports
- Check SSH root login configuration
- Calculate a basic security score
- Generate a security report

---

## Usage

Run the security check:

```bash
python3 security_checker.py
```

### Example Output

```
=== Linux Security Checker ===

Firewall: Not detected
Open Ports: 5353
SSH root login: ENABLED

Security Score: 4/10
```

---

## Generate Security Report

Run:

```bash
python3 security_checker.py --report
```

View the report:

```bash
cat security_report.txt
```

---

## Project Structure

```
linux-security-checker
│
├── security_checker.py
├── README.md
├── LICENSE
└── security_report.txt
```

---

## Why this project?

Many Linux beginners do not know how to check if their system is secure.  
This tool helps users quickly audit basic security settings and understand potential risks.

---

## License

MIT License
