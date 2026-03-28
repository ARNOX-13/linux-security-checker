def check_ssh():
    try:
        with open("/etc/ssh/sshd_config", "r") as file:
            config = file.read()

            if "PermitRootLogin no" in config:
                return "[+] SSH Root Login      : DISABLED", 0
            else:
                return "[✗] SSH Root Login      : ENABLED", 0

    except:
        return "[!] SSH configuration not accessible (service not present)", 0
