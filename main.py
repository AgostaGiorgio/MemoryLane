from datetime import datetime
import os
import re
import sys
import argparse
from argparse import RawTextHelpFormatter
from memorylane.date_extractor import DATE_PATTERN, get_creation_date
from memorylane.organizer import check_dates, organize_files, validate_dir
from memorylane.logger import logger
from memorylane.utils import get_filename_from_path

def main():

    # Parsing command-line arguments
    parser = argparse.ArgumentParser(description="Organize photos and videos by date", formatter_class=RawTextHelpFormatter)
    parser.add_argument('--input', '-i', type=str, required=True, help="Directory containing the photos and videos")
    parser.add_argument('--output', '-o', type=str, help="Directory to store organized files")
    parser.add_argument('--date-format', type=str, default="%Y/%B", 
                        help=(
                            "Date format for organizing files (default: '%%Y/%%B').\n"
                            "You can use the following syntax:\n"
                            "  %%Y - Year with 4 digits (e.g., 2021)\n"
                            "  %%y - Year with 2 digits (e.g., 21)\n"
                            "  %%m - Month in numbers (01-12)\n"
                            "  %%B - Full month name (e.g., April)\n"
                            "  %%d - Day of the month (01-31)\n"
                            "Example formats:\n"
                            "  '%%Y/%%B/%%d' -> '2021/April/12'\n"
                            "  '%%y/%%m/%%d' -> '21/04/12'\n"
                            "  '%%Y/%%m'    -> '2021/04'\n"
                            "  '%%d/%%m/%%y' -> '12/04/21'\n"
                        ))
    parser.add_argument('--move', action='store_true', help="Move files instead of copying them")
    parser.add_argument('--check-date', action='store_true', help="Check from which photos and videos the tool is able to extract the info")
    parser.add_argument('--validate-dir', action='store_true', help="Validate the structure of a ginven folder based on the date-format")
    args = parser.parse_args()

    # Ensure input directory exists
    if not os.path.isdir(args.input):
        logger.error(f"❌ Input directory '{args.input}' does not exist.")
        sys.exit(1)

    try:
        if args.check_date:
            check_dates(args.input, args.date_format, logger)
        elif args.validate_dir:
            validate_dir(args.input, args.date_format, logger)
        else:
            organize_files(args.input, args.output, args.date_format, logger, move=args.move)
    except Exception as e:
        sys.exit(1)

    logger.info("\n\n✅✅ Process completed successfully ✅✅")

if __name__ == "__main__":
    main()
    # validate_dir("./test", "%Y/.*", logger)
