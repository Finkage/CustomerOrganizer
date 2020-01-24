import tkinter
from tkinter import *
import FileIO
from FileIO import *
import FieldsConfig
from FieldsConfig import *

class Main_Window(tkinter.Tk):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.customer = FileIO()
        self.fields_config = FieldsConfig()
        self.tool_bar()
        self.setup_fields()

    def do_nothing():
        '''do nothing at all'''

    def tool_bar(self):
        menubar = Menu(self)

        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "New Customer", command = self.do_nothing)
        filemenu.add_command(label = "Open Customer", command = self.do_nothing)
        filemenu.add_command(label = "Save Customer", command = self.customer.save_file)
        filemenu.add_command(label = "Save Customer as...", command = self.do_nothing)
        filemenu.add_command(label = "Close Customer", command = self.do_nothing)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = self.quit)

        menubar.add_cascade(label = "File", menu = filemenu)

        self.config(menu = menubar)

    def setup_fields(self):
        self.fields_config.load_config()