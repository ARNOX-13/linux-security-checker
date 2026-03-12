import subprocess

def check_firewall():
    try:
        firewall = subprocess.check_output("ufw status", shell=True).decode()
        if "Status: active" in firewall:
            return "[✓] Firewall: ACTIVE", 3
        else:
            return "[!] Firewall: INACTIVE", 0
    except:
        return "[✓] Firewall: Not detected", 0
