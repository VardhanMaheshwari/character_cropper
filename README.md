# Character Cropper Tool

A simple Python + OpenCV tool for manually cropping individual characters from manuscript images. It is designed to help create datasets for OCR and handwritten character recognition.

## Project Structure

```text
character_cropper/
│
├── cropper.py
├── images/
│   └── manuscript1.jpg
└── output/
```

* **images/** – Store the manuscript image(s).
* **output/** – Cropped character images are saved here automatically.

## Requirements

* Python 3.8+
* OpenCV

Install OpenCV:

```bash
pip install opencv-python
```

## Configuration

Update the image path in `cropper.py` before running:

```python
IMAGE_PATH = "images/Manuscript02(SPPU_SANSKRIT)/2_2.jpg"
```

The output directory is created automatically if it does not already exist:

```python
OUTPUT_DIR = "output"
```

## Running the Tool

```bash
python cropper.py
```

## Controls

| Action                             | Control    |
| ---------------------------------- | ---------- |
| Select first corner of crop        | Left Click |
| Select opposite corner & save crop | Left Click |
| Cancel current selection           | C          |
| Undo last crop                     | Z          |
| Refresh display                    | R          |
| Quit                               | Q          |

## Workflow

1. Update `IMAGE_PATH` with the manuscript image you want to crop.
2. Run the script.
3. Click once to select the first corner of a character.
4. Click again on the opposite corner to define the crop.
5. The selected region is automatically saved in the `output/` directory.
6. Continue selecting characters until finished.
7. Press **Q** to exit.

## Output

Each cropped character is saved as:

```text
char_0001.png
char_0002.png
char_0003.png
...
```

If the `output/` directory already contains images, numbering continues from the next available index.

## Features

* Manual two-click rectangular cropping.
* Automatic sequential file naming.
* Semi-transparent overlay showing previously cropped regions.
* Undo the last saved crop with **Z**.
* Cancel the current selection with **C**.
* Refresh the display with **R**.
* Automatically resizes the display window to fit within **1200 × 800** while preserving the image's original resolution for cropping.
