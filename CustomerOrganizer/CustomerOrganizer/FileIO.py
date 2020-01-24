import os

# Save and load customer's data file.
class FileIO():
	def save_file(self):
		try:
			os.makedirs("data")
			print("Data folder created")
		except FileExistsError:
			print("Data folder already exists")  

		file = open("data/test.txt", "w+")
		file.write("this is a test")
		file.close()
		print("Saved file")