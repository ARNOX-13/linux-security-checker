import subprocess

def check_privileges():
    try:
        result = []
        score = 0

        # -------- Current User -------- #
        user = subprocess.check_output("whoami", shell=True).decode().strip()
        result.append(f"Current User: {user}")

        # -------- Groups -------- #
        groups = subprocess.check_output("groups", shell=True).decode().strip()
        result.append(f"Groups: {groups}")

        # -------- Check sudo access -------- #
        try:
            sudo_check = subprocess.check_output("sudo -l", shell=True, stderr=subprocess.DEVNULL).decode()

            if "may run the following commands" in sudo_check:
                result.append("[!] User has sudo privileges")
                score -= 2
            else:
                result.append("[✓] No sudo privileges detected")
                score += 2

        except:
            result.append("[✓] No sudo privileges detected")
            score += 2

        # -------- Dangerous groups -------- #
        dangerous_groups = ["root", "sudo", "wheel", "admin"]

        user_groups = groups.split()
        risky = []

        for g in user_groups:
            if g in dangerous_groups:
                risky.append(g)

        if risky:
            result.append(f"[!] Dangerous group membership: {', '.join(risky)}")
            score -= 2
        else:
            result.append("[✓] No dangerous group memberships")

        return "\n".join(result), score

    except Exception as e:
        return f"[!] Privilege check failed: {str(e)}", 0
