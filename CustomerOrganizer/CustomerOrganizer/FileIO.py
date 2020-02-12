import os
from datetime import date
from tkinter import *
from tkinter import filedialog

# Save and load customer's data file.
class FileIO():
    DATA_FOLDER_NAME = "data"
#    DATA_FILE_NAME = "test.txt"
    FORMATTED_DATE = date.today().strftime("%m/%d/%y")
    file = None

    # saves file, creates new file if it doesnt already exist
    def save_file(self, file_data, file_name):
        # if saving a new file, all the data will be created into a new file
        if self.file == None:
            try:
                os.makedirs(self.DATA_FOLDER_NAME)
                print("Data folder created")
            except FileExistsError:
                print("Data folder already exists")  

            file_name = self.DATA_FOLDER_NAME + "\\" + file_name + ".txt"
            self.file = open(file_name, "w+")

            for line in file_data:
                self.file.write(line)
        # if the file is already one that is being worked on, it will simply be overwritten with the new info
        else:
            for line in file_data:
                self.file.write(line)

    def load_file(self, window):
        load_window = window
        load_window.filename = filedialog.askopenfilename(initialdir = "C:\\Users\\Public\\Documents", 
                                                          title = "Select File", 
                                                          filetypes = (("Text Files", "*.txt"), ("All Files", "*.*")))
        try:
            self.file = open(load_window.filename, "r")
            return self.file.readlines()
        except FileNotFoundError:
            print("invalid file opened")
            return None


    def close_file(self):
        if self.file is not None:
            self.file.close()
        self.file = None