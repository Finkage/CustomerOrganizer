import MainWindow
import FileIO
import tkinter

root = tkinter.Tk()
app = MainWindow.Application(master=root)
app.mainloop()

fileOutput = FileIO.FileIO()
fileOutput.saveFile()