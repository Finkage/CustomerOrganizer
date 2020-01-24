class FieldsConfig():
	CONFIG_FILE_NAME = "config.txt"
	DEFAULT_CUSTOMER_FIELDS = ["First name", "Last name", "Address", "City", "Phone number"]
	DEFAULT_VEHICLE_FIELDS = ["Year", "Make", "Model", "VIN", "Engine", "Submodel", "Mileage in", "Lic"]
	DEFAULT_NOTES_FIELDS = ["Customer complaints", "Services rendered", "Recommended services", "Notes"]

	def create_config(self):
		cfile = open(self.CONFIG_FILE_NAME, "w+")
		
		cfile.write("CUSTOMER\n")
		for field in self.DEFAULT_CUSTOMER_FIELDS:
			cfile.write(field + "\n")

		cfile.write("\nVEHICLE\n")
		for field in self.DEFAULT_VEHICLE_FIELDS:
			cfile.write(field + "\n")

		cfile.write("\nNOTES\n")
		for field in self.DEFAULT_NOTES_FIELDS:
			cfile.write(field + "\n")
		
		cfile.close()
		print("Created new config file.")

	def load_config(self):
		try:
			cfile = open(self.CONFIG_FILE_NAME, "r")
			print("Config file loaded successfully.")
		except IOError:
			print("Could not find " + self.CONFIG_FILE_NAME)
			self.create_config()
