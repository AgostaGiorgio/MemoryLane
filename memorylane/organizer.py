import os
import re
import shutil
import sys
from memorylane.date_extractor import get_creation_date

def organize_files(input_dir, output_dir, date_format, logger, move=False):
    """
    Organizes photos and videos from the input directory into folders based on their creation date.
    
    :param input_dir: Directory containing photos and videos
    :param output_dir: Directory to store organized files
    :param date_format: Format string for organizing files (e.g., '%Y/%B/%d')
    :param move: Whether to move files instead of copying (default is False)
    :param logger: Logger to log the process
    """
    # Ensure the input directory exists
    if not os.path.isdir(input_dir):
        logger.error(f"❌ Input directory {input_dir} does not exist.")
        sys.exit(1)

    if not output_dir:
        logger.error(f"❌ Missing parameter: Output dir. Use --help to see how to use the tool.")
        sys.exit(1)

    # Ensure output directory exists, create if not
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each file in the input directory
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)

        # Skip directories
        if os.path.isdir(file_path):
            organize_files(file_path, output_dir, date_format, logger, move=move)
        else:
            # Get the creation time of the file
            try:
                date = get_creation_date(file_path)
                output_path = date.strftime(date_format)  # Format the date according to the user's choice
            except Exception as e:
                logger.error(f"🚧 Could not retrieve creation date for file {filename}: {e}")
                output_path = "unknown"

            # Create the target directory path
            target_dir = os.path.join(output_dir, output_path)

            # Ensure the target directory exists
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            # Determine the target file path
            target_path = os.path.join(target_dir, filename)

            # Move or copy the file based on the user's choice
            try:
                if move:
                    shutil.move(file_path, target_path)
                else:
                    shutil.copy2(file_path, target_path)

                logger.info(f"✅ {file_path} {'moved' if move else 'copied'} --> {target_path}")
            except Exception as e:
                logger.error(f"❌ {file_path}: {e}")

def check_dates(input_dir, date_format, logger):
    """
    Analyze photos and videos from the input directory trying to extract their creation date.
    
    :param input_dir: Directory containing photos and videos
    :param date_format: Format string for organizing files (e.g., '%Y/%B/%d')
    :param logger: Logger to log the process
    """
    # Ensure the input directory exists
    if not os.path.isdir(input_dir):
        logger.error(f"❌ Input directory {input_dir} does not exist.")
        sys.exit(1)

    # Process each file in the input directory
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)

        # Skip directories
        if os.path.isdir(file_path):
            check_dates(file_path, date_format, logger)
        else:
            # Get the creation time of the file
            try:
                date = get_creation_date(file_path)
                output_path = date.strftime(date_format)  # Format the date according to the user's choice
                logger.info(f"✅ {file_path} --> {output_path}")
            except Exception as e:
                logger.error(f"❌ Could not retrieve creation date for file {file_path}")

def validate_dir(input_dir, date_format, logger):
    """
    Analyze photos and videos from the input directory and validate the path based on their creation date and the date-format.
    
    :param input_dir: Directory containing photos and videos
    :param date_format: Format string for organizing files (e.g., '%Y/%B/%d')
    :param logger: Logger to log the process
    """
    # Ensure the input directory exists
    if not os.path.isdir(input_dir):
        logger.error(f"❌ Input directory {input_dir} does not exist.")
        sys.exit(1)

    # Process each file in the input directory
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)

        # Skip directories
        if os.path.isdir(file_path):
            validate_dir(file_path, date_format, logger)
        else:
            # Get the creation time of the file
            try:
                date = get_creation_date(file_path)
                regex = os.path.join(date.strftime(date_format), filename)  # Format the date according to the user's choice
                regex = re.compile(regex, re.IGNORECASE)

                match = re.search(regex, file_path)
                if match:
                    logger.info(f"✅ {file_path}")
                else:
                    logger.info(f"❌ {file_path}: should be {regex.pattern}")
            except Exception as e:
                logger.error(f"🚧 Could not retrieve creation date for file {file_path}")
    return "OK"