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
        self.new_customer()


    # clear current data
    def clear_data(self):
        self.customer_widgets.clear()
        self.vehicle_widgets.clear()
        self.note_widgets.clear()


    # Close current customer and open a new blank customer
    def new_customer(self):
        self.customer.close()
        self.clear_data()
        self.customer.new()
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

        # display all customer data into the frame
        self.create_widgets(self.customer.get_data(), "customer_info", 1, 20, 1)

        # frame to hold vehicle info
        self.frames["vehicle_info"] = Frame(self.frames["top"])
        self.frames["vehicle_info"].pack(fill = BOTH, side = LEFT)

        # title for the customer info frame
        vi_title = Label(self.frames["vehicle_info"], text = "Vehicle Info", font = 'Helvetica 16 bold')
        vi_title.grid(row = 0, columnspan = 2)

        # display all vehicle data into the frame
        self.create_widgets(self.customer.get_vehicle(), "vehicle_info", 1, 20, 1)

        # frame to hold note info
        self.frames["note_info"] = Frame(self)
        self.frames["note_info"].pack(fill = BOTH, side = BOTTOM)

        # title for the customer info frame
        n_title = Label(self.frames["note_info"], text = "Notes", font = 'Helvetica 16 bold')
        n_title.grid(row = 0, columnspan = 2)

        # display all notes data into the frame
        self.create_widgets(self.customer.get_notes(), "note_info", 5, 40, 2)

    def create_widgets(self, dictionary, section, box_height, box_width, iteration):
        for key in dictionary.keys():
            data = dictionary[key]
            new_box_height = box_height

            # Create label
            entry_label = Label(master = self.frames[section], text = key)
            entry_label.grid(row = iteration)
            
            # If data has a lot of characters, expand box size.            
            if len(data) > box_width * box_height:
                new_box_height = box_height + len(data) / box_width
            
            # Create text box
            entry_box = Text(master = self.frames[section], height = new_box_height, width = box_width, wrap = WORD)
            entry_box.grid(row = iteration, column = 1)
            entry_box.insert(END, data)

            iteration += 1
