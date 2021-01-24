import pyttsx3
import PyPDF2

# book=open("BCS-27.pdf","rb")
# pdfReader=PyPDF2.PdfFileReader(book)
# pages=pdfReader.numPages
# print(pages)
speaker=pyttsx3.init()
file_name=input("Enter the name of the text file:- ")
page=open(file_name,"rb")
text=page.readlines()
speaker.say(text)
speaker.runAndWait()

#Debugging area during developing this
# for num in range(10,pages):
#     page=pdfReader.getPage(num)
#     text=page.extractText()
#     speaker.say(text)
#     speaker.runAndWait()