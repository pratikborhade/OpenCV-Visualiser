import lib.GUI.guimain
import lib.Context.Frame


last_frame_location = (0, 0)


def get_next_frame_location():
    global last_frame_location
    half_size_of_thumbnail = int(lib.Context.Frame.thumbnail_size[0] / 2)
    main_window_width = lib.GUI.guimain.main_window.winfo_width()
    thumbnail_height = lib.Context.Frame.thumbnail_size[1]
    next_location = (main_window_width/2 - half_size_of_thumbnail, last_frame_location[1] + thumbnail_height)
    last_frame_location = next_location
    return next_location

