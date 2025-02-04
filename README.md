# **MemoryLane**

**MemoryLane** is a Python-based project designed to organize personal photos and videos into structured folders and subfolders based on the date they were captured. This project was created to help users preserve and organize their life's memories in a chronological and easily accessible way.

## **Key Features**
- **Automatic Organization:** Photos and videos are sorted into folders based on their creation date.
- **Customizable Date Format:** Users can specify the folder structure using custom date formats (e.g., `DD/MM/YY`, `YY/MM`, or others).
- **Metadata Extraction:** Utilizes file metadata (EXIF data) to determine the creation date of photos and videos.
- **Error Handling:** Files without metadata are handled gracefully, allowing users to manually assign dates or place them in a separate folder (e.g., `Unknown Date`).
- **Cross-Platform:** Fully functional on Windows, macOS, and Linux.
- **Supports Multiple Formats:** Works with a variety of photo and video file formats, including JPEG, PNG, MP4, and more.
- **Safe Processing:** Ensures files are moved or copied without overwriting or accidental loss of data.

## **How It Works**
1. The program scans a given directory containing photos and videos.
2. It reads the metadata (e.g., EXIF) of each file to extract the creation date.
3. Files are then moved into a folder structure based on the user-defined date format: \
`<Base Directory>/<Custom Date Format>/<File> ` \
Examples: 
    - A photo taken on April 12, 2024, with the format `DD/MM/YY`, will be moved to: `12/04/24/img.png` 
    - The same photo with the format `YY/MM` will be moved to: `24/04/img.png`
4. Files without valid metadata are either skipped or placed in a folder named Unknown Date for manual review.

## **Requirements**
- Python 3.8 or higher
- Poetry for dependency management

Install Poetry by following the [official guide](https://python-poetry.org/docs/#installation).

## **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/memorylane.git
   cd memorylane
   ```
1. Install the project dependencies using Poetry:
   ```bash
   poetry install
   ```

## **Usage**
Run the script:
```bash
python main.py --input <input-folder> --output <output-folder> --date-format <date-format>
```  
- Replace `<input-folder>` with the directory containing your photos and videos.
- Replace `<output-folder>` with the directory where organized files will be stored.
- Replace `<date-format>` with your desired date format (e.g., `DD/MM/YY`, `YY/MM`).

### **Command-Line Options**
- `--input`: Directory containing the photos and videos (required).
- `--output`: Directory to store organized files (required).
- `--date-format`: **Date format** for organizing files. You can specify the format using the following placeholders:
  - `%Y`: Year with 4 digits (e.g., `2021`)
  - `%y`: Year with 2 digits (e.g., `21`)
  - `%m`: Month in numbers (01-12)
  - `%B`: Full month name (e.g., `April`)
  - `%d`: Day of the month (01-31)

  **Example formats:**
  - `'%Y/%B/%d'` → `2021/April/12`
  - `'%y/%m/%d'` → `21/04/12`
  - `'%Y/%m'`    → `2021/04`
  - `'%d/%m/%y'` → `12/04/21`

  **Default format**: `'%Y/%B'` (e.g., `2021/April`).
- `--move`: Move files instead of copying them (optional).
- `--check-date`: Check from which photos and videos the tool is able to extract the info
- `--validate-dir`: Validate the structure of a ginven folder based on the date-format

## **Example**
```bash
python main.py --input /path/to/photos --output /path/to/organized --date-format DD/MM/YY
``` 

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## **Acknowledgments**
Special thanks to the open-source community for providing the libraries and tools that made this project possible.
