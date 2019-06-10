import tkinter
import lib.Algorithms.ImageUtils


class FrameWindow:
    def __init__(self, frame):
        self.frame = frame
        self.image_window = tkinter.Toplevel()
        #self.image_window.pack(fill=tkinter.BOTH, expand=1)
        self.config_window = tkinter.PanedWindow(self.image_window, orient=tkinter.HORIZONTAL)
        self.config_window.config(width=self.image_window.winfo_width()/4)

    def show(self):
        self.image_window.title(self.frame.name)
        tk_img = lib.Algorithms.ImageUtils.convert_cv_img_to_tk_photo(self.frame.img)
        tkinter.Label(self.image_window, image=tk_img).pack()
        self.image_window.mainloop()
