from FileIO import *

class Customer():
    file = FileIO()
    data = {}
    vehicle = {}
    notes = {}

    def close(self):
        self.data.clear()
        self.vehicle.clear()
        self.notes.clear()

        self.file.close_file()


    def new(self):
        self.file.save_file()

    
    def open(self, window):
        self.file.load_file(window)

        # parsing goes here


    def save(self, new_data, new_vehicle, new_notes):
        self.data = new_data
        self.vehicle = new_vehicle
        self.notes = new_notes

        # parsing goes here


    def get_data(self):
        return self.data

        
    def get_vehicle(self):
        return self.vehicle


    def get_notes(self):
        return self.notes