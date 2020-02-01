import os
from datetime import date
from tkinter import *
from tkinter import filedialog

# Save and load customer's data file.
class FileIO():
    DATA_FOLDER_NAME = "data"
    DATA_FILE_NAME = "test.txt"
    FORMATTED_DATE = date.today().strftime("%m/%d/%y")
    file = None

    def save_file(self):
        try:
            os.makedirs(self.DATA_FOLDER_NAME)
            print("Data folder created")
        except FileExistsError:
            print("Data folder already exists")  

        file_name = self.DATA_FOLDER_NAME + self.DATA_FILE_NAME
        file = open(file_name, "w+")
        file.write("this is a test")
        file.close()
        print("Saved file")

    def load_file(self, window):
        load_window = window
        load_window.filename = filedialog.askopenfilename(initialdir = "C:\\Users\\Public\\Documents", 
                                                          title = "Select File", 
                                                          filetypes = (("Text Files", "*.txt"), ("All Files", "*.*")))
        try:
            self.file = open(load_window.filename)
        except FileNotFoundError:
            print("invalid file opened")


    def close_file(self):
        if self.file is not None:
            self.file.close()