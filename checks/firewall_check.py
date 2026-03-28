import subprocess

def check_firewall():
    try:
        firewall = subprocess.check_output("ufw status", shell=True).decode()

        if "Status: active" in firewall:
            return "[+] Firewall Status      : ACTIVE", 0
        else:
            return "[!] Firewall Status      : INACTIVE", 0

    except:
        return "[!] Firewall tool not detected on system", 0
