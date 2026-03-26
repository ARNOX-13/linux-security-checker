import argparse
import json

from checks.firewall_check import check_firewall
from checks.port_check import check_ports
from checks.ssh_check import check_ssh
from checks.file_scan import scan_file
from checks.process_check import check_processes
from checks.privilege_check import check_privileges

# ---------------- CLI Arguments ---------------- #

parser = argparse.ArgumentParser(
    description="Linux Security Checker - CLI Tool"
)

parser.add_argument(
    "--scan-file",
    help="Scan a file for malware"
)

parser.add_argument(
    "--export-json",
    action="store_true",
    help="Export scan results as JSON"
)

args = parser.parse_args()


# ---------------- Core Functions ---------------- #

def run_scan():
    score = 0
    results = []

    msg, pts = check_firewall()
    results.append(msg)
    score += pts

    msg, pts = check_ports()
    results.append(msg)
    score += pts

    msg, pts = check_ssh()
    results.append(msg)
    score += pts

    msg, pts = check_processes()
    results.append(msg)
    score += pts
    
    msg, pts = check_privileges()
    results.append(msg)
    score += pts

    results.append(f"Security Score: {score}/10")

    return results



def generate_report():
    report = {}

    msg, _ = check_firewall()
    report["firewall"] = msg

    msg, _ = check_ports()
    report["ports"] = msg

    msg, _ = check_ssh()
    report["ssh"] = msg

    msg, _ = check_processes()
    report["processes"] = msg
   
    msg, _ = check_privileges()
    report["privileges"] = msg
 
    return report


# ---------------- Execution Logic ---------------- #

# JSON Export
if args.export_json:
    report = generate_report()

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("Report saved as report.json")
    exit()


# File Scan
if args.scan_file:
    print("\nScanning file:", args.scan_file)
    print(scan_file(args.scan_file))
    exit()


# Default System Scan
print("=== Linux Security Checker ===\n")

results = run_scan()
for r in results:
    print(r)
