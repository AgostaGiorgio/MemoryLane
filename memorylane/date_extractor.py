import re
import pyheif
import piexif
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
from pymediainfo import MediaInfo
from memorylane.utils import get_filename_from_path
from memorylane.logger import logger

XMP_REGEX = re.compile(
    r'.*photoshop:DateCreated>(.*)<\/photoshop:DateCreated.*', re.IGNORECASE)
IMAGE_EXTS = {"jpg", "jpeg", "png", "gif", "bmp", "tiff", "heic", "webp"}
VIDEO_EXTS = {"mp4", "mkv", "avi", "mov", "flv", "wmv", "webm", "m4v"}
DATE_PATTERN = r"(\d{4})(\d{2})(\d{2})"


def get_creation_date(file_path):
    """
    Attempts to extract the creation date from a photo or video file.
    Handles HEIC and MOV files separately from other image formats.

    :param file_path: Path to the photo or video file
    :return: The creation date as a datetime object, or None if not found
    """
    date = _from_file_name(file_path)
    if not date:
        file_extension = file_path.lower().split('.')[-1]

        if file_extension == 'heic':
            date = _from_heic(file_path)
        elif file_extension in IMAGE_EXTS:
            date = _from_classic_image(file_path)
        elif file_extension in VIDEO_EXTS:
            date = _from_classic_video(file_path)
        else:
            pass

    return date


def _from_file_name(file_path):    
    date = None
    match = re.search(DATE_PATTERN, get_filename_from_path(file_path))
    if match:
        y, m, d = match.groups()
        try:
            date = datetime.strptime(f"{y}{m}{d}", "%Y%m%d")
            logger.debug("Date extracted from the title")
        except:
            pass
    return date


def _from_heic(file_path):
    date = None

    metadata = pyheif.read(file_path).metadata
    if metadata:
        for meta in metadata:
            if meta['type'] == 'Exif':
                exif_raw_data = meta['data']
                exif_data = piexif.load(exif_raw_data)
                date = datetime.strptime(exif_data.get("Exif").get(piexif.ExifIFD.DateTimeOriginal).decode("UTF-8"), '%Y:%m:%d %H:%M:%S')
                logger.debug("Date extracted from heic dedicated logic")
    return date


def _from_classic_image(file_path):
    date = None

    # Extract EXIF metadata
    exif_data = Image.open(file_path)._getexif()
    if exif_data:
        date = datetime.strptime(exif_data.get(piexif.ExifIFD.DateTimeOriginal), '%Y:%m:%d %H:%M:%S')
        logger.debug("Date extracted from classic image logic")
    return date


def _from_classic_video(file_path):
    date = None

    metadata = MediaInfo.parse(file_path)
    for track in metadata.tracks:
        if track.track_type == "General" and track.tagged_date:
            date = datetime.strptime(track.tagged_date, 'UTC %Y-%m-%d %H:%M:%S')
            logger.debug("Date extracted from classic video logic")

    return date
