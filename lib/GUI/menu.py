import tkinter
import lib.Commands.FileMenuCommands as file_commands


def add_file_menu(main_menu):
    file_menu = tkinter.Menu(main_menu)
    main_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open File", command=file_commands.open_file)


def configure_menu(window):
    menu = tkinter.Menu(window)
    window.config(menu=menu)
    add_file_menu(menu)
