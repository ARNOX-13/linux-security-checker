import argparse
import json
import os

from checks.firewall_check import check_firewall
from checks.port_check import check_ports
from checks.ssh_check import check_ssh
from checks.file_scan import scan_file
from checks.process_check import check_processes
from checks.privilege_check import check_privileges
from checks.env_check import detect_environment


# ---------------- CLI Arguments ---------------- #

parser = argparse.ArgumentParser(
    description="Linux Security Checker - CLI Tool"
)

parser.add_argument("--scan-file", help="Scan a file for malware")
parser.add_argument("--export-json", action="store_true", help="Export scan results as JSON")

args = parser.parse_args()


# ---------------- Root Check (Polished) ---------------- #

if os.geteuid() != 0:
    print("[!] Running without root privileges — some checks may be limited")


# ---------------- Scoring System ---------------- #

def calculate_score(issues):
    score = 10
    reasons = []

    severity_map = {
        "low": 0.5,
        "medium": 1,
        "high": 2,
        "critical": 3
    }

    for issue, severity in issues:
        deduction = severity_map.get(severity, 0)
        score -= deduction
        reasons.append(f"- {issue} ({severity.capitalize()} impact)")

    if score < 0:
        score = 0

    return round(score, 1), reasons


# ---------------- Core Scan ---------------- #

def run_scan(env):
    results = {}
    issues = []

    # ===== Network Security =====
    network_output = []

    msg, _ = check_firewall()
    network_output.append(msg)

    if "INACTIVE" in msg and env == "local":
        issues.append(("Firewall is inactive", "high"))

    msg, _ = check_ports()
    network_output.append(msg)

    if "Open Ports" in msg and env == "local":
        issues.append(("Open ports detected", "low"))

    msg, _ = check_ssh()
    network_output.append(msg)

    if "ENABLED" in msg and env == "local":
        issues.append(("SSH root login enabled", "critical"))

    results["Network Security"] = "\n".join(network_output)

    # ===== Process Analysis =====
    msg, _ = check_processes()
    results["Process Analysis"] = msg

    if "Suspicious Processes" in msg:
        issues.append(("Suspicious processes detected", "high"))

    if "Root Processes" in msg and "(High)" in msg:
        issues.append(("High number of root processes", "low"))

    # ===== Privilege Analysis =====
    msg, _ = check_privileges()
    results["Privilege Analysis"] = msg

    if "Current User" in msg and "root" in msg:
        issues.append(("Running as root user", "medium"))

    if "Sudo Privileges" in msg and "ENABLED" in msg:
        issues.append(("User has sudo privileges", "low"))

    # ===== Final Score =====
    score, reasons = calculate_score(issues)

    summary = "\n".join(reasons)

    if not reasons:
        summary = "[+] System shows no immediate critical threats"

    results["Final Security Score"] = (
        f"Score: {score}/10\n\n"
        "Reason:\n"
        f"{summary}"
    )

    return results


# ---------------- JSON Report ---------------- #

def generate_report(env):
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

    report["environment"] = env

    return report


# ---------------- Execution ---------------- #

env = detect_environment()

if args.export_json:
    report = generate_report(env)

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("[+] Report saved as report.json")
    exit()


if args.scan_file:
    print("\n=== File Scan ===\n")
    print(scan_file(args.scan_file))
    exit()


print("=== Linux Security Checker ===")

if env == "restricted":
    print("\n[!] Running in restricted environment (Cloud/Container detected)")
    print("[!] Some checks may be unavailable or limited\n")

results = run_scan(env)

for section, content in results.items():
    print(f"\n=== {section} ===")
    print(content)
