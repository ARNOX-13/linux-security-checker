def scan_file(file_path):

    try:
        with open("signatures.txt", "r") as sig_file:
            signatures = sig_file.read().splitlines()

        with open(file_path, "r", errors="ignore") as target:
            content = target.read()

        for sig in signatures:
            if sig in content:
                return f"[!] Malware signature detected: {sig}"

        return "[✓] No known malware signatures detected"

    except:
        return "[!] Could not scan file"
