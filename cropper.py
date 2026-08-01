import cv2
import os

# ---------------- SETTINGS ----------------

IMAGE_PATH = "images/2_1.jpg"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------------------

image = cv2.imread(IMAGE_PATH)

if image is None:
    raise Exception("Could not load image.")

display = image.copy()

top_y = None
bottom_y = None

x_start = None

saved_images = []

counter = len(os.listdir(OUTPUT_DIR)) + 1


def redraw():
    global display

    display = image.copy()

    if top_y is not None:
        cv2.line(display, (0, top_y),
                 (display.shape[1], top_y),
                 (0,255,0),2)

    if bottom_y is not None:
        cv2.line(display, (0,bottom_y),
                 (display.shape[1],bottom_y),
                 (0,0,255),2)

    if x_start is not None:
        cv2.line(display,
                 (x_start,0),
                 (x_start,display.shape[0]),
                 (255,0,0),1)


def mouse(event, x, y, flags, param):

    global top_y
    global bottom_y
    global x_start
    global counter

    # Ctrl + Left = Top Y
    if event == cv2.EVENT_LBUTTONDOWN and flags & cv2.EVENT_FLAG_CTRLKEY:
        top_y = y
        redraw()
        return

    # Ctrl + Right = Bottom Y
    if event == cv2.EVENT_RBUTTONDOWN and flags & cv2.EVENT_FLAG_CTRLKEY:
        bottom_y = y
        redraw()
        return

    # Normal left click
    if event == cv2.EVENT_LBUTTONDOWN:

        if top_y is None or bottom_y is None:
            print("Set Top and Bottom Y first.")
            return

        if x_start is None:
            x_start = x
            redraw()
            return

        x_end = x

        left = min(x_start, x_end)
        right = max(x_start, x_end)

        top = min(top_y, bottom_y)
        bottom = max(top_y, bottom_y)

        crop = image[top:bottom, left:right]

        filename = os.path.join(
            OUTPUT_DIR,
            f"char_{counter:04d}.png"
        )

        cv2.imwrite(filename, crop)

        print("Saved:", filename)

        saved_images.append(filename)

        counter += 1

        x_start = None

        redraw()

MAX_WIDTH = 1200
MAX_HEIGHT = 800

h, w = image.shape[:2]

scale = min(MAX_WIDTH / w, MAX_HEIGHT / h, 1.0)

display_width = int(w * scale)
display_height = int(h * scale)

cv2.namedWindow("Cropper", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Cropper", display_width, display_height)

cv2.setMouseCallback("Cropper", mouse)

while True:

    cv2.imshow("Cropper", display)

    key = cv2.waitKey(20) & 0xFF

    # Quit
    if key == ord('q'):
        break

    # Cancel current selection
    elif key == ord('c'):
        x_start = None
        redraw()

    # Reload
    elif key == ord('r'):
        redraw()

    # Undo
    elif key == ord('z'):

        if saved_images:
            last = saved_images.pop()

            if os.path.exists(last):
                os.remove(last)

            counter -= 1

            print("Deleted:", last)

cv2.destroyAllWindows()
