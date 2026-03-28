import subprocess

def check_ports():
    try:
        ports = subprocess.check_output("ss -tuln", shell=True).decode()
        port_list = []

        for line in ports.split("\n")[1:]:
            parts = line.split()
            if len(parts) > 4:
                port = parts[4].split(":")[-1]
                port_list.append(port)

        if port_list:
            message = "[+] Open Ports           : " + ", ".join(port_list)
        else:
            message = "[+] Open Ports           : None detected"

        return message, 0

    except:
        return "[!] Port check not available in this environment", 0
