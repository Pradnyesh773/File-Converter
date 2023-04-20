import tkinter as tk
import tabula
from tkinter import filedialog
import aspose.words as aw
from tkinter import*

root = tk.Tk()
root.title("File Converter")
f=("Arial",20,"bold")
lab1=Label(root,text="Choose File Type",font=f,fg="black")
lab1.pack(pady=10)
root.configure(background="black")


button_font = ('italic', 16, 'bold')
button_bg = 'red'
button_fg = 'white'
button_borderwidth = 0
button_relief = 'flat'

 

def pdf():
        file_path= filedialog.askopenfilename()
        doc = aw.Document(file_path)
        doc.save("Output.pdf")

def word(): 
        file_path = filedialog.askopenfilename()
        doc = aw.Document(file_path)
        doc.save("Output.docx")

def html():
        file_path = filedialog.askopenfilename()
        doc = aw.Document(file_path)
        doc.save("Output.html")

def text():
        file_path = filedialog.askopenfilename() 
        doc = aw.Document("demo.pdf")
        doc.save("Output.txt")

def png():
        file_path = filedialog.askopenfilename() 
        doc = aw.Document(file_path)
        for page in range(0,doc.page_count):
          extractedPage = doc.extract_pages(page, 1)
          extractedPage.save(f"Output_{page + 1}.png")

def jpg():
       file_path = filedialog.askopenfilename() 
       doc = aw.Document(file_path)
       for page in range(1,doc.page_count):
         extractedPage = doc.extract_pages(page, 1)
         extractedPage.save(f"Output_{page + 1}.jpg")

def epub():    
      file_path = filedialog.askopenfilename()
      doc = aw.Document(file_path)
      doc.save("Output.epub")                 


button = tk.Button(root, text="pdf", font=button_font, fg=button_fg, bg=button_bg,
                   borderwidth=button_borderwidth, relief=button_relief,
                   command=pdf)

button1 = tk.Button(root, text="word", font=button_font, fg=button_fg, bg=button_bg,
                   borderwidth=button_borderwidth, relief=button_relief,
                   command=word)

button2 = tk.Button(root, text="html", font=button_font, fg=button_fg, bg=button_bg,
                   borderwidth=button_borderwidth, relief=button_relief,
                   command=html)

button3 = tk.Button(root, text="text", font=button_font, fg=button_fg, bg=button_bg,
                   borderwidth=button_borderwidth, relief=button_relief,
                   command=text)

button4 = tk.Button(root, text="jpg", font=button_font, fg=button_fg, bg=button_bg,
                   borderwidth=button_borderwidth, relief=button_relief,
                   command=jpg)

button5 = tk.Button(root, text="png", font=button_font, fg=button_fg, bg=button_bg,
                   borderwidth=button_borderwidth, relief=button_relief,
                   command=png)

button6 = tk.Button(root, text="epub", font=button_font, fg=button_fg, bg=button_bg,
                   borderwidth=button_borderwidth, relief=button_relief,
                   command=epub)

button.pack(pady=20)
button1.pack(pady=20)
button2.pack(pady=20)
button3.pack(pady=20)
button4.pack(pady=20)
button5.pack(pady=20)
button6.pack(pady=20)


root.mainloop()