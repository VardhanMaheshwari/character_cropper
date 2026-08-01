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

- **images/** → Place the manuscript image(s) here.
- **output/** → Cropped character images are saved here automatically.

## Requirements

- Python 3.8+
- OpenCV

Install OpenCV:

```bash
pip install opencv-python
```

## Running the Tool

```bash
python cropper.py
```

## Controls

| Action | Control |
|--------|---------|
| Set Top Y | Ctrl + Left Click |
| Set Bottom Y | Ctrl + Right Click |
| Select Start X | Left Click |
| Select End X & Save Crop | Left Click |
| Cancel Current Selection | C |
| Undo Last Crop | Z |
| Refresh Display | R |
| Quit | Q |

## Workflow

1. Place the manuscript image inside the `images/` folder.
2. Update the `IMAGE_PATH` in `cropper.py` if needed.
3. Run the script.
4. Set the **Top Y** and **Bottom Y** using **Ctrl + Click**.
5. Click the left and right boundaries of each character.
6. Cropped images are automatically saved in the `output/` folder as:

```text
char_0001.png
char_0002.png
char_0003.png
...
```

## Notes

- The tool keeps accepting crops until you press **Q**.
- Images are automatically numbered.
- Press **Z** to delete the last saved crop if a mistake is made.
