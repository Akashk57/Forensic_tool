import argparse

def main():
    parser = argparse.ArgumentParser(description="🛡 Forensic CLI Tool - Track File Changes, Analyze Tampering")
    parser.add_argument("command", choices=["scan", "monitor", "yara-scan", "audit", "analyze"],
                        help="What action do you want to perform?")
    args = parser.parse_args()

    # Default path: entire system (safe folders only, actual exclusion handled in each module)
    default_path = "/"

    if args.command == "scan":
        from hashing import compute_hashes
        compute_hashes(default_path)

    elif args.command == "monitor":
        from monitor import start_monitoring
        start_monitoring(default_path)

    elif args.command == "yara-scan":
        from yara_scanner import scan_all_with_yara
        scan_all_with_yara()  # Defaults to scanning from "/"

    elif args.command == "audit":
        from audit_logger import add_audit_watch_recursive
        add_audit_watch_recursive(default_path)

    elif args.command == "analyze":
        from ai_analysis import analyze_all_files
        analyze_all_files(default_path)

if __name__ == "__main__":
    main()

