import subprocess

def check_processes():
    try:
        output = subprocess.check_output("ps aux", shell=True).decode()

        lines = output.split("\n")[1:]  # skip header

        total = 0
        root_processes = 0
        suspicious = []

        # basic suspicious keywords
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

            # count root processes
            if user == "root":
                root_processes += 1

            # detect suspicious patterns
            cmd_lower = command.lower()
            for keyword in suspicious_keywords:
                if keyword in cmd_lower:
                    suspicious.append(command)
                    break

        result = []
        result.append(f"Total Processes: {total}")
        result.append(f"Root Processes: {root_processes}")

        if suspicious:
            result.append(f"[!] Suspicious Processes Detected: {len(suspicious)}")
        else:
            result.append("[✓] No suspicious processes found")

        score = 0

        if root_processes < total * 0.3:
            score += 2
        if not suspicious:
            score += 2

        return "\n".join(result), score

    except Exception as e:
        return f"[!] Process check failed: {str(e)}", 0
