import tkinter
import lib.GUI.menu as menu


def init_window(window):
    window.title("OpenCV Visualiser");
    window.geometry("1028x800")


main_window = None


def launch():
    global main_window
    main_window = tkinter.Tk()
    init_window(main_window)
    menu.configure_menu(main_window)
    main_window.mainloop()
