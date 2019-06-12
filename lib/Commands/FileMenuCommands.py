import tkinter
import tkinter.filedialog
import cv2
import lib.GUI.guimain
import lib.Context.Frame


def open_file():
    file = tkinter.filedialog.askopenfilename()
    frame = lib.Context.Frame.Frame()
    frame.code = frame.variable_name + "=" + "cv2.imread('" + file + "')"
    frame.update()
    frame.register(lib.GUI.guimain.main_window)

