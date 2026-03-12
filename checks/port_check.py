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

        message = "Open Ports: " + ", ".join(port_list)

        if len(port_list) <= 5:
            return message, 4
        else:
            return message, 0

    except:
        return "[!] Could not check ports", 0
