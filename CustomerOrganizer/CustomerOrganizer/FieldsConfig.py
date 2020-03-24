class FieldsConfig():
	CONFIG_FILE_NAME = "config.txt"
	DEFAULT_SECTIONS = {"customer", "vehicle", "notes"}
	DEFAULT_CUSTOMER_FIELDS = ["First name", "Last name", "Address", "City", "Phone number"]
	DEFAULT_VEHICLE_FIELDS = ["Year", "Make", "Model", "VIN", "Engine", "Submodel", "Mileage in", "Lic"]
	DEFAULT_NOTES_FIELDS = ["Customer complaints", "Services rendered", "Recommended services", "Notes"]

	dict_customer = {}
	dict_vehicle = {}
	dict_notes = {}

	def create_config(self):
		c_file = open(self.CONFIG_FILE_NAME, "w+")
		
		c_file.write("CUSTOMER\n")
		for field in self.DEFAULT_CUSTOMER_FIELDS:
			c_file.write(field + "\n")

		c_file.write("\nVEHICLE\n")
		for field in self.DEFAULT_VEHICLE_FIELDS:
			c_file.write(field + "\n")

		c_file.write("\nNOTES\n")
		for field in self.DEFAULT_NOTES_FIELDS:
			c_file.write(field + "\n")
		
		c_file.close()
		print("Created new config file.")

	def load_config(self):
		try:
			c_file = open(self.CONFIG_FILE_NAME, "r")
			current_section = ""

			for line in c_file:
				if line == "\n":
					current_section = ""
					continue

				formatted_line = line.lower().strip("\n")

				if current_section == "":
					if formatted_line in self.DEFAULT_SECTIONS:
						current_section = formatted_line
					continue
				else:
					if current_section == "customer":
						self.update_field(self.dict_customer, line.strip("\n"), "")
					elif current_section == "vehicle":
						self.update_field(self.dict_vehicle, line.strip("\n"), "")
					elif current_section == "notes":
						self.update_field(self.dict_notes, line.strip("\n"), "")

			c_file.close()
			print("Config file loaded successfully.")

		except IOError:
			print("Could not find " + self.CONFIG_FILE_NAME)
			self.create_config()
			self.load_config()

	def update_field(self, dictionary, key, value):
		dictionary[key] = value
