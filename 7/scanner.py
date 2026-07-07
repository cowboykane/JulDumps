import argparse, logging
from pathlib import Path

# What connects these three libraries? 
# argparse collects what the user wants 
# pathlib turns path strings into Path objects you can validate/manipulate
# logging reports what the script is doing, verbosity is controlled by argparse flags



# --- 1. Set up the parser ---
parser = argparse.ArgumentParser(description="Scan a directory and report on files.")
parser.add_argument("path", type=Path, help="Directory to scan")
parser.add_argument("--pattern", default="*", help="Glob pattern, e.g. *.log")
parser.add_argument(
    "-v", "--verbose",
    action="store_true",  
    help="Enable debug-level logging"
)
parser.add_argument("--logfile", type=Path, help="Optional file to write logs to")

args = parser.parse_args()

# --- 2. Configure logging BASED ON the parsed args ---
log_level = logging.DEBUG if args.verbose else logging.INFO

logging.basicConfig(
    level=log_level,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename=args.logfile if args.logfile else None,  # None = prints to console
)

logger = logging.getLogger(__name__)

# --- 3. Use pathlib to validate and act on the path ---
target = args.path

if not target.exists():
    logger.error(f"Path does not exist: {target}")
    raise SystemExit(1)

if not target.is_dir():
    logger.error(f"Not a directory: {target}")
    raise SystemExit(1)

logger.debug(f"Scanning {target.resolve()} with pattern '{args.pattern}'")

matches = list(target.glob(args.pattern))

logger.info(f"Found {len(matches)} matching file(s)")

for f in matches:
    logger.debug(f"  {f.name} ({f.stat().st_size} bytes)")

print(f"\nDone. {len(matches)} file(s) matched '{args.pattern}' in {target}")