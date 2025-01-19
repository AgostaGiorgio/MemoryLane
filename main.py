import os
import sys
import argparse
from argparse import RawTextHelpFormatter
from memorylane.organizer import organize_files
from memorylane.logger import logger

def main():

    # Parsing command-line arguments
    parser = argparse.ArgumentParser(description="Organize photos and videos by date", formatter_class=RawTextHelpFormatter)
    parser.add_argument('--input', type=str, required=True, help="Directory containing the photos and videos")
    parser.add_argument('--output', type=str, required=True, help="Directory to store organized files")
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
    parser.add_argument('--log', action='store_true', help="Enable detailed logging")
    args = parser.parse_args()

    # Log the command-line parameters
    if args.log:
        logger.info(f"Starting the process with the following parameters:")
        logger.info(f"Input Directory: {args.input}")
        logger.info(f"Output Directory: {args.output}")
        logger.info(f"Date Format: {args.date_format}")

    # Ensure input directory exists
    if not os.path.isdir(args.input):
        logger.error(f"The input directory '{args.input}' does not exist.")
        sys.exit(1)

    # Ensure output directory exists, create if not
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    # Organize files
    try:
        organize_files(args.input, args.output, args.date_format, move=args.move, logger=logger)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        sys.exit(1)

    logger.info("Process completed successfully.")

if __name__ == "__main__":
    main()
