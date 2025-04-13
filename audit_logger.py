import subprocess
import os

def add_audit_watch_recursive(base_path):
    for root, _, files in os.walk(base_path):
        for f in files:
            path = os.path.join(root, f)
            try:
                subprocess.run(["auditctl", "-w", path, "-p", "rwxa", "-k", "forensic_watch"], check=True)
                print(f"[AUDIT] Watching {path}")
            except Exception:
                continue

