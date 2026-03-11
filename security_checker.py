import subprocess

score = 0

print("=== Linux Security Checker ===\n")

# Firewall check
try:
    firewall = subprocess.check_output("ufw status", shell=True).decode()
    if "Status: active" in firewall:
        print("[✓] Firewall: ACTIVE")
        score += 3
    else:
        print("[!] Firewall: INACTIVE")
except:
    print("[✓] Firewall: Not detected")


# Open ports check
try:
    ports = subprocess.check_output("ss -tuln", shell=True).decode()
    port_list = []

    for line in ports.split("\n")[1:]:
        parts = line.split()
        if len(parts) > 4:
            port = parts[4].split(":")[-1]
            port_list.append(port)

    print("\nOpen Ports:", ", ".join(port_list))

    if len(port_list) <= 5:
        score += 4

except:
    print("[!] Could not check ports")


# SSH root login check
try:
    with open("/etc/ssh/sshd_config", "r") as file:
        config = file.read()

        if "PermitRootLogin no" in config:
            print("\n[✓] SSH root login: DISABLED")
            score += 3
        else:
            print("\n[!] SSH root login: ENABLED")

except:
    print("\n[!] Could not read SSH config")


print(f"\nSecurity Score: {score}/10")
