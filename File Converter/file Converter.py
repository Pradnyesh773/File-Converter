import pyautogui
import aspose.words as aw
import tabula
from tkinter import filedialog
from tkinter import*

confirm= pyautogui.confirm(title="Alert",text="File Converter",buttons=["pdf","word","html","text","jpg","png","epub","xhtml"])

if confirm== "pdf":
    file_path = filedialog.askopenfilename()
    doc = aw.Document(file_path)
    doc.save("Output.pdf")

elif confirm == "word":
    file_path = filedialog.askopenfilename()
    doc = aw.Document(file_path)
    doc.save("Output.docx")
  
elif confirm == "html":
    file_path = filedialog.askopenfilename()
    doc = aw.Document(file_path)
    doc.save("Output.html")

elif confirm == "text":
    doc = aw.Document("demo.pdf")
    doc.save("Output.txt")
             
elif confirm == "jpg":
    file_path = filedialog.askopenfilename() 
    doc = aw.Document(file_path)
    for page in range(1,doc.page_count):
       extractedPage = doc.extract_pages(page, 1)
       extractedPage.save(f"Output_{page + 1}.jpg")     

elif confirm == "png":
    file_path = filedialog.askopenfilename() 
    doc = aw.Document(file_path)
    for page in range(0,doc.page_count):
       extractedPage = doc.extract_pages(page, 1)
       extractedPage.save(f"Output_{page + 1}.png")

elif confirm == "epub":
    file_path = filedialog.askopenfilename()
    doc = aw.Document(file_path)
    doc.save("Output.epub")

elif confirm == "xhtml":
    file_path = filedialog.askopenfilename() 
    doc = aw.Document(file_path)
    doc.save("Output.xhtml")

else:
    print("wrong input")   

           
