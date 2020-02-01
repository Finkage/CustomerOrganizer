from tkinter import *
from FieldsConfig import *
from CustomerClass import *

class Main_Window(Tk):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master

        # initializing variables
        self.customer = Customer()
        self.fields_config = FieldsConfig()
        self.customer_widgets = {}
        self.vehicle_widgets = {}
        self.note_widgets = {}
        self.frames = {}

        # initializing functions
        self.tool_bar()
        self.setup_fields()


    # clear current data
    def clear_data(self):
        self.customer_widgets.clear()
        self.vehicle_widgets.clear()
        self.note_widgets.clear()


    # Close current customer and open a new blank customer
    def new_customer(self):
        self.customer.close()
        self.customer.new()
        self.clear_data()
        self.display_customer()


    # open a customer file and display it onto GUI
    def open_customer(self):
        self.customer.open(self)
        self.clear_data()
        self.display_customer()


    # saves customer data currently input into file
    def save_customer(self):
        tmpData = {}
        tmpVehicle = {}
        tmpNotes ={}
        for data in self.customer_widgets.keys():
            tmpData[data] = self.customer_widgets[data].get('1.0', 'end')
        for data in self.vehicle_widgets.keys():
            tmpVehicle[data] = self.vehicle_widgets[data].get('1.0', 'end')
        for data in self.note_widgets.keys():
            tmpNotes[data] = self.note_widgets[data].get('1.0', 'end')

        self.customer.save(tmpData, tmpVehicle, tmpNotes)


    # saves current customer as a new customer, must have different name or liscense plate number
    def save_customer_as(self):
        self.customer.close()
        self.customer.new()

        #self.customer.save()


    # toolbar initialization
    def tool_bar(self):
        menubar = Menu(self)

        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "New Customer", command = self.new_customer)
        filemenu.add_command(label = "Open Customer", command = self.open_customer)
        filemenu.add_command(label = "Save Customer", command = self.save_customer)
        filemenu.add_command(label = "Save Customer as...", command = self.save_customer_as)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = self.quit)

        menubar.add_cascade(label = "File", menu = filemenu)

        self.config(menu = menubar)


    # loads config file
    def setup_fields(self):
        self.fields_config.load_config()

     
    # display customer data onto GUI
    def display_customer(self):
        # clear out all of the GUI
        for frame in self.frames.keys():
            self.frames[frame].pack_forget()
            self.frames[frame].destroy()

        # top level frame
        self.frames["top"] = Frame(self)
        self.frames["top"].pack(fill = BOTH, side = TOP)

        # frame to hold basic customer info
        self.frames["customer_info"] = Frame(self.frames["top"])
        self.frames["customer_info"].pack(fill = BOTH, side = LEFT)

        # title for the customer info frame
        bi_title = Label(self.frames["customer_info"], text = "Customer Info", font = 'Helvetica 16 bold')
        bi_title.grid(row = 0, columnspan = 2)

        iteration = 1
        # display all customer data into the frame
        for data in self.fields_config.dict_customer.keys():
            entry_label = Label(master = self.frames["customer_info"], text = data)
            entry_label.grid(row = iteration)
            self.customer_widgets[data] = Text(master = self.frames["customer_info"], height = 1, width = 20)
            if data in self.customer.get_data():
                self.customer_widgets[data].config(text = self.customer.get_data()[data])
            self.customer_widgets[data].grid(row = iteration, column = 1)
            iteration += 1

        # frame to hold vehicle info
        self.frames["vehicle_info"] = Frame(self.frames["top"])
        self.frames["vehicle_info"].pack(fill = BOTH, side = LEFT)

        # title for the customer info frame
        vi_title = Label(self.frames["vehicle_info"], text = "Vehicle Info", font = 'Helvetica 16 bold')
        vi_title.grid(row = 0, columnspan = 2)

        iteration = 1
        # display all vehicle data into the frame
        for data in self.fields_config.dict_vehicle.keys():
            entry_label = Label(master = self.frames["vehicle_info"], text = data)
            entry_label.grid(row = iteration)
            self.vehicle_widgets[data] = Text(master = self.frames["vehicle_info"], height = 1, width = 20)
            if data in self.customer.get_vehicle():
                self.vehicle_widgets[data].config(text = self.customer.get_vehicle()[data])
            self.vehicle_widgets[data].grid(row = iteration, column = 1)
            iteration += 1

        # frame to hold note info
        self.frames["note_info"] = Frame(self)
        self.frames["note_info"].pack(fill = BOTH, side = BOTTOM)

        # title for the customer info frame
        n_title = Label(self.frames["note_info"], text = "Notes", font = 'Helvetica 16 bold')
        n_title.grid(row = 0, columnspan = 2)

        iteration = 2
        # display all vehicle data into the frame
        for data in self.fields_config.dict_notes.keys():
            entry_label = Label(master = self.frames["note_info"], text = data)
            entry_label.grid(row = iteration)
            self.note_widgets[data] = Text(master = self.frames["note_info"] , height = 5, width = 40)
            if data in self.customer.get_notes():
                self.note_widgets[data].config(text = self.customer.get_notes()[data])
            self.note_widgets[data].grid(row = iteration, column = 1)
            iteration += 1
