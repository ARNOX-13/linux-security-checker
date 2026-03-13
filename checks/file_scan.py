import hashlib

def scan_file(file_path):

    try:
        with open("signatures.txt", "r") as sig_file:
            signatures = sig_file.read().splitlines()

        with open(file_path, "r", errors="ignore") as target:
            content = target.read()

        for sig in signatures:
            if sig in content:
                return f"[!] Malware signature detected: {sig}"

        # --- HASH CHECK ---
        with open(file_path, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()

        with open("hash_signatures.txt", "r") as hash_file:
            hashes = hash_file.read().splitlines()

        if file_hash in hashes:
            return f"[!] Known malicious file detected (SHA256 match)"

        return "[✓] No known malware signatures detected"

    except:
        return "[!] Could not scan file"
