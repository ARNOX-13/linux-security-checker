import subprocess


def check_processes():
    try:
        output = subprocess.check_output("ps aux", shell=True).decode()
        lines = output.split("\n")[1:]

        total = 0
        root_processes = 0
        suspicious = []

        suspicious_keywords = [
            "nc", "netcat", "bash -i", "sh -i",
            "meterpreter", "payload", "reverse", "shell"
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
                    suspicious.append(command)
                    break

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

        score = 0

        if root_processes < total * 0.3:
            score += 2

        if not suspicious:
            score += 2

        return "\n".join(result), score

    except:
        return "[!] Process inspection limited (restricted environment)", 0
