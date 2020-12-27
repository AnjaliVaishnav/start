from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PyPDF2 #to convert file into one string
from gtts import gTTS #google text to speech


Tk.withdraw() #dont want full GUI so keep root from appearing
filelocation = askopenfilename() #open the filedialog

with open(filelocation, "rb") as read: #open file in reading mode and name it as read
pdf = PyPDF2.PdfFileReader(read) # store a text of pdf read in pdf variable
i = 0
string_of_text = ''
while i<pdf.getnumpages():
    page = pdf.getpage():
    text += page.extractText():
    i += 1 #to amke it as one piece

final_file = gTTS(text = string_of_text, lang = 'en') #store file in variable
final_file.save("Generated speech.mp3")  # save file to computer
