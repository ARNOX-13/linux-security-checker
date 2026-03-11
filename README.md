# Linux Security Checker

Linux Security Checker is a simple CLI tool that scans basic security settings on a Linux system and provides a security score.

## Features

- Detect firewall status
- List open network ports
- Check SSH root login configuration
- Calculate a basic security score

## Usage

Run:

python3 security_checker.py

Example Output:

=== Linux Security Checker ===

Firewall: Not detected
Open Ports: 5353
SSH root login: ENABLED

Security Score: 4/10

## Why this project?

Many Linux beginners do not know how to check if their system is secure. This tool helps users quickly audit basic security settings.

## License

MIT License
