import re
from FileIO import *
from FieldsConfig import *

class Customer():
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
                        print("Error: Unable to determine section.")
                        # TO-DO: Popup screen with error here.
                        return None
                # Populate dictionary using : as a delimiter. Left of delimiter is key; right of delimiter is value.
                else:
                    pair = line.split(":", 1)
                    FieldsConfig().update_field(dictionary, pair[0].strip(), pair[1].strip())

            print("\nCustomer dictionary: ", self.data)
            print("Vehicle dictionary: ", self.vehicle)
            print("Notes dictionary: ", self.notes)
            
            return 0

        except:
            print("Error: Something has gone wrong while attempting to parse the file.")
            return None


    def save(self, new_data, new_vehicle, new_notes):
        self.data = new_data
        self.vehicle = new_vehicle
        self.notes = new_notes
        total_data = []

        total_data.append("CUSTOMER\n")
        for key in self.data.keys():
            total_data.append(key + ": " + self.data[key])
        total_data.append("\n")
        total_data.append("VEHICLE\n")
        for key in self.vehicle.keys():
            total_data.append(key + ": " + self.vehicle[key])
        total_data.append("\n")
        total_data.append("NOTES\n")
        for key in self.notes.keys():
            total_data.append(key + ": " + self.notes[key])

        self.file.save_file(total_data, self.data["Last name"] + "_" + self.data["First name"][0] + self.vehicle["VIN"][0:2])


    def get_data(self):
        return self.data
    

    def get_vehicle(self):
        return self.vehicle


    def get_notes(self):
        return self.notes


        