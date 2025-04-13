from inotify_simple import INotify, flags
import os
from datetime import datetime

EXCLUDE_DIRS = ["/proc", "/sys", "/dev", "/run", "/tmp", "/boot", "/snap", "/var/lib", "/var/run"]

def start_monitoring(base_path):
    inotify = INotify()
    watches = {}

    def add_watch(path):
        try:
            if any(path.startswith(excl) for excl in EXCLUDE_DIRS):
                return
            wd = inotify.add_watch(path, flags.MODIFY | flags.CREATE | flags.DELETE)
            watches[wd] = path
        except Exception:
            pass

    # Add watches for each directory
    for root, dirs, _ in os.walk(base_path):
        add_watch(root)

    print("Monitoring started. Press Ctrl+C to stop.")
    try:
        while True:
            for event in inotify.read():
                full_path = os.path.join(watches.get(event.wd, ""), event.name)
                time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                readable_flags = flags.from_mask(event.mask)
                for flag in readable_flags:
                    print(f"[{time_str}] {flag.name}: {full_path}")
    except KeyboardInterrupt:
        print("Monitoring stopped.")

