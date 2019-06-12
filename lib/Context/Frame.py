import lib.Algorithms.ImageUtils as ImageUtils
import lib.Algorithms.LocationCalculator as LocationCalculator
import lib.GUI.FrameWindow
import tkinter
import sys
from io import StringIO
import cv2

# Default size of thumbnail image
thumbnail_size = (240, 240)

# List of frames currently active
frames = []


# Frame class used to track images currently available in application
class Frame:
    def __init__(self, img=None, code=None):
        global thumbnail_size
        global frames
        # setting variables required for code
        self.code = code
        self.variable_name = "frame" + str(len(frames))
        self.input = img
        self.img = None
        self.errors = None
        # self.input_variable = self.variable_name + "_input"
        # setting name for input variable
        # exec("%s = %d" % (self.input_variable, self.input))
        if code is not None:
            self.update()
        self.name = "Frame "+str(len(frames))
        self.next_frames = []
        frames.append(self)

    def update(self):
        # running code
        self.run_code()
        # getting output for the code
        self.thumbnail = ImageUtils.convert_cv_img_to_tk_photo(self.img)

    def show_frame(self):
        window = lib.GUI.FrameWindow.FrameWindow(self)
        window.show()

    def register(self, root_window):
        global thumbnail_size
        # configure button
        button = tkinter.Button(root_window, text=self.name, command=lambda: self.show_frame())
        next_location = LocationCalculator.get_next_frame_location()
        button.config(image=self.thumbnail, height=thumbnail_size[1], width=thumbnail_size[0])
        button.place(x=next_location[0], y=next_location[1])
        button.pack()

        # update main window
        root_window.Update()

    def rename(self, new_name):
        self.name = new_name

    def run_code(self):
        #code_out = StringIO.StringIO()
        #code_error = StringIO.StringIO()
        #sys.stdout = code_out
        #sys.stderr = code_error
        code = self.variable_name + " = " + self.code + "\n"
        #try:
        exec(code)
        #finally:
            #pass
            # restore stdout and stderr
            #sys.stdout = sys.__stdout__
            #sys.stderr = sys.__stderr__
        self.img = eval(self.variable_name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        global frames
        frames.remove(self)
