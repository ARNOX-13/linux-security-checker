import subprocess
import subprocess


def check_processes():
    try:
        output = subprocess.check_output("ps aux", shell=True).decode()
        lines = output.split("\n")[1:]

        total = 0
        root_processes = 0
        suspicious = []

        # 🔥 Improved detection (real attack patterns only)
        suspicious_keywords = [
            "nc -e",
            "netcat -e",
            "bash -i",
            "sh -i",
            "python -c",
            "perl -e",
            "php -r",
            "meterpreter",
            "/dev/tcp"
        ]

        # 🔥 Whitelist (avoid false positives)
        safe_processes = [
            "systemd",
            "kworker",
            "dbus",
            "timesyncd",
            "NetworkManager",
            "gnome",
            "Xorg"
        ]

        for line in lines:
            if not line.strip():
                continue

            total += 1

            parts = line.split()
            user = parts[0]
            command = " ".join(parts[10:])

            if user == "root":
                root_processes += 1

            cmd_lower = command.lower()

            for keyword in suspicious_keywords:
                if keyword in cmd_lower:

                    # skip safe processes
                    if any(safe.lower() in cmd_lower for safe in safe_processes):
                        continue

                    suspicious.append(command)
                    break

        # -------- Output -------- #
        result = []

        result.append(f"[+] Total Processes     : {total}")

        if root_processes > total * 0.5:
            result.append(f"[!] Root Processes      : {root_processes} (High)")
        else:
            result.append(f"[+] Root Processes      : {root_processes}")

        if suspicious:
            result.append(f"\n[!] Suspicious Processes Detected: {len(suspicious)}")

            for proc in suspicious[:3]:
                short_proc = proc[:60] + "..." if len(proc) > 60 else proc
                result.append(f"    → {short_proc}")
        else:
            result.append("[+] No suspicious processes found")

        return "\n".join(result), 0

    except:
        return "[!] Process inspection limited (restricted environment)", 0
