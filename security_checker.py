import sys
import subprocess

score = 0
report_data = []

print("=== Linux Security Checker ===\n")

# Firewall check
try:
    firewall = subprocess.check_output("ufw status", shell=True).decode()
    if "Status: active" in firewall:
        msg = "[✓] Firewall: ACTIVE"
        score += 3
    else:
        msg = "[!] Firewall: INACTIVE"
except:
    msg = "[✓] Firewall: Not detected"

print(msg)
report_data.append(msg)


# Open ports check
try:
    ports = subprocess.check_output("ss -tuln", shell=True).decode()
    port_list = []

    for line in ports.split("\n")[1:]:
        parts = line.split()
        if len(parts) > 4:
            port = parts[4].split(":")[-1]
            port_list.append(port)

    port_msg = "Open Ports: " + ", ".join(port_list)
    print("\n" + port_msg)
    report_data.append(port_msg)

    if len(port_list) <= 5:
        score += 4

except:
    msg = "[!] Could not check ports"
    print(msg)
    report_data.append(msg)


# SSH root login check
try:
    with open("/etc/ssh/sshd_config", "r") as file:
        config = file.read()

        if "PermitRootLogin no" in config:
            msg = "[✓] SSH root login: DISABLED"
            score += 3
        else:
            msg = "[!] SSH root login: ENABLED"

except:
    msg = "[!] Could not read SSH config"

print("\n" + msg)
report_data.append(msg)


# Final score
result = f"\nSecurity Score: {score}/10"
print(result)
report_data.append(result)


# Report generation
if "--report" in sys.argv:
    with open("security_report.txt", "w") as f:
        f.write("Linux Security Checker Report\n\n")
        for line in report_data:
            f.write(line + "\n")

    print("Report saved to security_report.txt")
