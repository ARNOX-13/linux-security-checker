import subprocess

def check_privileges():
    try:
        result = []

        user = subprocess.check_output("whoami", shell=True).decode().strip()
        result.append(f"[✗] Current User        : {user}")

        groups = subprocess.check_output("groups", shell=True).decode().strip()
        result.append(f"[!] Group Membership    : {groups}")

        try:
            sudo_check = subprocess.check_output("sudo -l", shell=True, stderr=subprocess.DEVNULL).decode()

            if "may run the following commands" in sudo_check:
                result.append("[✗] Sudo Privileges     : ENABLED")
            else:
                result.append("[+] Sudo Privileges     : DISABLED")

        except:
            result.append("[+] Sudo Privileges     : DISABLED")

        dangerous_groups = ["root", "sudo", "wheel", "admin"]
        user_groups = groups.split()

        risky = [g for g in user_groups if g in dangerous_groups]

        if risky:
            result.append(f"[✗] Dangerous Groups    : {', '.join(risky)}")
        else:
            result.append("[+] Dangerous Groups    : None")

        return "\n".join(result), 0

    except:
        return "[!] Privilege analysis not fully available in this environment", 0
