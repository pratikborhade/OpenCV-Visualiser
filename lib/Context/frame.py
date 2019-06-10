import lib.Algorithms.ImageUtils as ImageUtils
import lib.Algorithms.LocationCalculator as LocationCalculator
import lib.GUI.FrameWindow
import tkinter
import cv2

# Default size of thumbnail image
thumbnail_size = (240, 240)

# List of frames currently active
frames = []


# Frame class used to track images currently available in application
class Frame:
    def __init__(self, img, code):
        global thumbnail_size
        global frames
        self.img = img
        self.code = code
        self.thumbnail = ImageUtils.convert_cv_img_to_tk_photo(img)
        self.name = "Frame "+str(len(frames))
        self.next_frames = []

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
        frames.append(self)

        # update main window
        root_window.Update()

    def rename(self, new_name):
        self.name = new_name
