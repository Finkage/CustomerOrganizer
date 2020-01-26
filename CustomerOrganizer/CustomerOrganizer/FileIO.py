import os
from datetime import date

# Save and load customer's data file.
class FileIO():
	DATA_FOLDER_NAME = "data"
	DATA_FILE_NAME = "test.txt"
	FORMATTED_DATE = date.today().strftime("%m/%d/%y")

	def save_file(self):
		try:
			os.makedirs(DATA_FOLDER_NAME)
			print("Data folder created")
		except FileExistsError:
			print("Data folder already exists")  

		file_name = DATA_FOLDER_NAME + DATA_FILE_NAME
		file = open(file_name, "w+")
		file.write("this is a test")
		file.close()
		print("Saved file")