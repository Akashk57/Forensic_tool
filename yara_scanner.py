import yara
import os

EXCLUDE_DIRS = ["/proc", "/sys", "/dev", "/run", "/snap", "/tmp", "/var/lib", "/var/run", "/boot"]

def scan_all_with_yara(base_path="/"):
    try:
        rules = yara.compile(filepath='rules.yar')
    except Exception as e:
        print(f"[ERROR] Failed to compile rules: {e}")
        return

    print(f"🔍 Starting YARA scan from: {base_path}")
    print("========================================\n")

    for root, _, files in os.walk(base_path):
        # Skip dangerous or noisy system dirs
        if any(root.startswith(excl) for excl in EXCLUDE_DIRS):
            continue
        for f in files:
            path = os.path.join(root, f)
            try:
                matches = rules.match(filepath=path)
                if matches:
                    print(f"[YARA MATCH] {path}")
                    for match in matches:
                        print(f"  Rule: {match.rule}")
                        for string in match.strings:
                            # Print the matched string and its position in the file
                            print(f"    Match at byte offset {string[0]}: {string[1]}")
            except Exception as e:
                continue

