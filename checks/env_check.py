import os

def detect_environment():
    restricted = False

    # Check container indicators
    try:
        with open("/proc/1/cgroup", "r") as f:
            data = f.read()
            if "docker" in data or "kubepods" in data or "container" in data:
                restricted = True
    except:
        pass

    # Check missing SSH config (common in containers)
    if not os.path.exists("/etc/ssh/sshd_config"):
        restricted = True

    return "restricted" if restricted else "local"
