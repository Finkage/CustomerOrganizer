import os
from datetime import date

# Save and load customer's data file.
class FileIO():
	DATA_FOLDER_NAME = "data"
	FORMATTED_DATE = date.today().strftime("%m/%d/%y")

	def save_file(self):
		try:
			os.makedirs(DATA_FOLDER_NAME)
			print("Data folder created")
		except FileExistsError:
			print("Data folder already exists")  

		file = open("data/test.txt", "w+")
		file.write("this is a test")
		file.close()
		print("Saved file")