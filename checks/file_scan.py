import hashlib
import os

def scan_file(file_path):

    try:
        # File exists?
        if not os.path.exists(file_path):
            return "[!] File not found"

        # Read file safely
        try:
            with open(file_path, "r", errors="ignore") as f:
                content = f.read()
        except:
            return "[!] Unable to read file"

        content_lower = content.lower()

        # Safe signature handling
        matches = []

        if os.path.exists("signatures.txt"):
            try:
                with open("signatures.txt", "r") as sig_file:
                    signatures = sig_file.read().splitlines()

                for sig in signatures:
                    if sig.lower() in content_lower:
                        matches.append(sig)
            except:
                pass

        if matches:
            return f"[!] Suspicious patterns detected: {', '.join(set(matches))}"

        # Hash check (safe)
        try:
            with open(file_path, "rb") as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()

            if os.path.exists("hash_signatures.txt"):
                with open("hash_signatures.txt", "r") as h:
                    hashes = h.read().splitlines()

                if file_hash in hashes:
                    return "[!] Known malicious file detected (SHA256 match)"
        except:
            pass

        return "[+] No known malware signatures detected"

    except:
        return "[!] Scan failed (restricted environment)"
