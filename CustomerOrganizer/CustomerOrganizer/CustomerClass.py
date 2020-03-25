import re
from FileIO import *
from FieldsConfig import *
from tkinter import messagebox

class Customer():
    ERROR_MESSAGE_CUSTOMER_NAME = "Customer needs a first and last name."
    ERROR_MESSAGE_LOAD = "Something has gone wrong while attempting to parse the file. Check formatting of file or open another file."
    ERROR_MESSAGE_SAVE = "Unable to save file."

    file = FileIO()
    fields_config = FieldsConfig()
    data = {}
    vehicle = {}
    notes = {}

    def close(self):
        self.data.clear()
        self.vehicle.clear()
        self.notes.clear()

        self.file.close_file()


    def new(self):
        self.fields_config.load_config()
        self.data = self.fields_config.dict_customer
        self.vehicle = self.fields_config.dict_vehicle
        self.notes = self.fields_config.dict_notes
    

    def open(self, window):
        try:
            self.data.clear()
            lines = self.file.load_file(window)
            dictionary = None

            # Parse through lines in file and populate dictionary with values.
            for line in lines:
                line_s = line.strip().lower()
                date_string = re.compile(".*/.*/.*")

                # If new line, we are in a new section and need to determine what section we are in.
                if line_s == "" or date_string.match(line_s) is not None:
                    dictionary = None
                    continue
                # Determine which section we are parsing through.
                # Only valid sections are customer, vehicle, and notes.
                elif dictionary is None:
                    if line_s in FieldsConfig.DEFAULT_SECTIONS:
                        if line_s == "customer":
                            dictionary = self.data
                        elif line_s == "vehicle":
                            dictionary = self.vehicle
                        elif line_s == "notes":
                            dictionary = self.notes
                        continue
                    else:
                        raise
                # Populate dictionary using : as a delimiter. Left of delimiter is key; right of delimiter is value.
                else:
                    pair = line.split(":", 1)
                    FieldsConfig().update_field(dictionary, pair[0].strip(), pair[1].strip())
            return 0

        except:
            messagebox.showerror("Error", self.ERROR_MESSAGE_LOAD)
            return None


    def save(self, new_data, new_vehicle, new_notes, save_as, window = None):
        self.data = new_data
        self.vehicle = new_vehicle
        self.notes = new_notes
        total_data = []

        # Customer first and last name will be used for naming file. Whitespaces will not allowed in file name.
        customer_first_name = self.data["First name"]
        customer_last_name = self.data["Last name"].replace(" ", "")

        total_data.append("CUSTOMER\n")

        for key in self.data.keys():
            total_data.append(key + ": " + self.data[key] + "\n")
        
        total_data.append("\nVEHICLE\n")
        
        for key in self.vehicle.keys():
            total_data.append(key + ": " + self.vehicle[key] + "\n")
        
        total_data.append("\nNOTES\n")
        
        for key in self.notes.keys():
            total_data.append(key + ": " + self.notes[key] + "\n")

        # Return error if first name or last name is empty or whitespace.
        if not customer_first_name or customer_first_name.isspace() or not customer_last_name or customer_last_name.isspace():
            messagebox.showerror("Error", self.ERROR_MESSAGE_CUSTOMER_NAME)
            return
        
        try:
            if not save_as:
                self.file.save_file(total_data, customer_last_name + "_" + customer_first_name[0] + self.vehicle["VIN"][0:2])
            else:
                self.file.save_as(total_data, window)
        except:
            messagebox.showerror("Error", self.ERROR_MESSAGE_SAVE)


    def get_data(self):
        return self.data
    

    def get_vehicle(self):
        return self.vehicle


    def get_notes(self):
        return self.notes


        