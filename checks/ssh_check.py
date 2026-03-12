def check_ssh():
    try:
        with open("/etc/ssh/sshd_config", "r") as file:
            config = file.read()

            if "PermitRootLogin no" in config:
                return "[✓] SSH root login: DISABLED", 3
            else:
                return "[!] SSH root login: ENABLED", 0

    except:
        return "[!] Could not read SSH config", 0
