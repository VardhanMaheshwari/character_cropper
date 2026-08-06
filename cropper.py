import cv2
import os

# ---------------- SETTINGS ----------------

IMAGE_PATH = "../../BEProject/images/Manuscript02(SPPU_SANSKRIT)/2_2.jpg"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------------------

image = cv2.imread(IMAGE_PATH)

if image is None:
    raise Exception("Could not load image.")

display = image.copy()

start_point = None   # (x, y)

saved_images = []
saved_regions = []   # Stores (left, top, right, bottom)

counter = len(os.listdir(OUTPUT_DIR)) + 1


def redraw():
    global display

    display = image.copy()
    overlay = display.copy()

    for left, top, right, bottom in saved_regions:
        cv2.rectangle(
            overlay,
            (left, top),
            (right, bottom),
            (0, 0, 255),
            -1
        )

    alpha = 0.35
    cv2.addWeighted(overlay, alpha, display, 1-alpha, 0, display)

    if start_point is not None:
        cv2.circle(display, start_point, 4, (0,255,0), -1)


def mouse(event, x, y, flags, param):

    global start_point
    global counter

    if event != cv2.EVENT_LBUTTONDOWN:
        return

    # First click -> top-left
    if start_point is None:
        start_point = (x, y)
        redraw()
        return

    # Second click -> bottom-right
    x1, y1 = start_point
    x2, y2 = x, y

    left = min(x1, x2)
    right = max(x1, x2)

    top = min(y1, y2)
    bottom = max(y1, y2)

    crop = image[top:bottom, left:right]

    filename = os.path.join(
        OUTPUT_DIR,
        f"char_{counter:04d}.png"
    )

    cv2.imwrite(filename, crop)

    saved_images.append(filename)
    saved_regions.append((left, top, right, bottom))

    print("Saved:", filename)

    counter += 1

    start_point = None

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
        start_point = None
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
            
            saved_regions.pop()
            counter -= 1
            
            redraw()
            
            print("Deleted:", last)

cv2.destroyAllWindows()
