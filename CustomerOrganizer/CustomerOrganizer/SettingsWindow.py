from tkinter import *

class Settings_Window():
    SETTINGS_WINDOW_TITLE = "Settings"
    SETTINGS_WINDOW_WIDTH = 500
    SETTINGS_WINDOW_HEIGHT = 300

    def __init__(self, master = None):
        settings_window = Toplevel(width = self.SETTINGS_WINDOW_WIDTH, height = self.SETTINGS_WINDOW_HEIGHT)
        settings_window.transient(master)                       # Make settings window transient of main window
        settings_window.withdraw()                              # Hide window to reposition it to avoid flashing
        settings_window.title(self.SETTINGS_WINDOW_TITLE)       # Rename settings window title
        master.center_window(settings_window, 0.5, 0.75)        # Position window to center of screen
        settings_window.focus()                                 # Shift focus of window to settings instead of main
        settings_window.deiconify()                             # Show settings window