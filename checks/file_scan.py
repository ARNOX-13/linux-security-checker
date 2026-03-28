import hashlib
import os

def scan_file(file_path):

    if not os.path.exists(file_path):
        return "[!] File not found"

    try:
        # -------- Signature Detection -------- #
        with open("signatures.txt", "r") as sig_file:
            signatures = sig_file.read().splitlines()

        with open(file_path, "r", errors="ignore") as target:
            content = target.read()

        content_lower = content.lower()
        matches = []

        for sig in signatures:
            sig_lower = sig.lower()
            if sig_lower in content_lower:
                matches.append(sig)

        if matches:
            matches = list(set(matches))  # remove duplicates
            return f"[!] Suspicious patterns detected: {', '.join(matches)}"

        # -------- Hash Detection -------- #
        with open(file_path, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()

        if os.path.exists("hash_signatures.txt"):
            with open("hash_signatures.txt", "r") as hash_file:
                hashes = hash_file.read().splitlines()

            if file_hash in hashes:
                return "[!] Known malicious file detected (SHA256 match)"

        return "[✓] No known malware signatures detected"

    except Exception as e:
        return "[!] File scan failed (unable to read file or signatures)"
