import argparse

from checks.firewall_check import check_firewall
from checks.port_check import check_ports
from checks.ssh_check import check_ssh
from checks.file_scan import scan_file

parser = argparse.ArgumentParser(
    description="Linux Security Checker - Basic Linux security auditing tool"
)

parser.add_argument(
    "--scan-file",
    help="Scan a file for known malware signatures"
)

args = parser.parse_args()

score = 0

print("=== Linux Security Checker ===\n")

# Firewall
msg, pts = check_firewall()
print(msg)
score += pts

# Ports
msg, pts = check_ports()
print("\n" + msg)
score += pts

# SSH
msg, pts = check_ssh()
print("\n" + msg)
score += pts

# File scan
if args.scan_file:
    print("\nScanning file:", args.scan_file)
    print(scan_file(args.scan_file))

# Final score
print(f"\nSecurity Score: {score}/10")
