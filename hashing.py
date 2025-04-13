EXCLUDE_DIRS = ["/proc", "/sys", "/dev", "/run", "/snap", "/tmp"]

def compute_hashes(base_path):
    for root, _, files in os.walk(base_path):
        if any(root.startswith(excl) for excl in EXCLUDE_DIRS):
            continue
        for f in files:
            path = os.path.join(root, f)
            try:
                h = hashlib.sha256()
                with open(path, 'rb') as file:
                    while chunk := file.read(4096):
                        h.update(chunk)
                print(f"[HASH] {path}: {h.hexdigest()}")
            except Exception as e:
                print(f"[ERROR] {path}: {e}")

