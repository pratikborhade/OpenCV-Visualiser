from PIL import Image, ImageTk
import cv2


def convert_cv_img_to_image(img):
    # Rearrange the color channel
    b, g, r = cv2.split(img)
    img = cv2.merge((r, g, b))
    # Create image for tkinter
    tk_img = Image.fromarray(img)
    return tk_img


def convert_cv_img_to_thumbnail(img, size):
    tk_img = convert_cv_img_to_image(img)
    return tk_img.thumbnail(size)


def convert_cv_img_to_tk_photo(img):
    tk_img = convert_cv_img_to_image(img)
    window_img = ImageTk.PhotoImage(image=tk_img)
    return window_img
