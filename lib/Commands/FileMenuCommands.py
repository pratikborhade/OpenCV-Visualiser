import tkinter
import tkinter.filedialog
import cv2
import lib.GUI.guimain
import lib.Context.frame


def open_file():
    file = tkinter.filedialog.askopenfilename()
    img = cv2.imread(file)
    frame = lib.Context.frame.Frame(img)
    frame.register(lib.GUI.guimain.main_window)

