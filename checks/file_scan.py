import hashlib
import os

def scan_file(file_path):

    # Check if file exists
    if not os.path.exists(file_path):
        return "[!] File not found"

    try:
        # -------- Signature Detection -------- #
        with open("signatures.txt", "r") as sig_file:
            signatures = sig_file.read().splitlines()

        with open(file_path, "r", errors="ignore") as target:
            content = target.read()

        matches = []
        for sig in signatures:
            if sig in content:
                matches.append(sig)

        if matches:
            return f"[!] Malware signatures detected: {', '.join(matches)}"

        # -------- Hash Detection -------- #
        with open(file_path, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()

        with open("hash_signatures.txt", "r") as hash_file:
            hashes = hash_file.read().splitlines()

        if file_hash in hashes:
            return "[!] Known malicious file detected (SHA256 match)"

        return "[✓] No known malware signatures detected"

    except Exception as e:
        return f"[!] Scan error: {str(e)}"
