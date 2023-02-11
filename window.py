from tkinter import *
from writeOnJpg import writeOnJpg
from printImage import printImage
from os import remove
from toPDF import toPDF

base = Tk()  
base.geometry('500x500')  
base.title("Generador de citas")
  
labl_0 = Label(base, text="Generador de citas. Kevin",width=20,font=("bold", 17))  
labl_0.place(x=90,y=53)  
  
  
labl_1 = Label(base, text="NOMBRE",width=20,font=("bold", 10))  
labl_1.place(x=80,y=130)    
entry_1 = Entry(base)  
entry_1.place(x=240,y=130)  
  
labl_2 = Label(base, text="FECHA",width=20,font=("bold", 10))  
labl_2.place(x=68,y=180)   
entry_02 = Entry(base)  
entry_02.place(x=240,y=180)  
  
labl_3 = Label(base, text="AGENDA",width=20,font=("bold", 10))  
labl_3.place(x=70,y=230)
entry_03 = Entry(base)
entry_03.insert(0, "Legalización")
entry_03.place(x=240,y=230)  
 
labl_4 = Label(base, text="SERVICIO",width=20,font=("bold", 10))  
labl_4.place(x=70,y=280)
entry_04 = Entry(base)
entry_04.insert(0, "Legalizaciones")
entry_04.place(x=240,y=280)

labl_5 = Label(base, text="FOOTER",width=20,font=("bold", 10))  
labl_5.place(x=70,y=330)
entry_05 = Entry(base)  
entry_05.place(x=240,y=330)



def create():
    name = entry_1.get()
    date = entry_02.get()
    agend = entry_03.get()
    service = entry_04.get() 
    footer = entry_05.get()

    writeOnJpg(name, date, agend, service, footer)

def createAndPrint():
    name = entry_1.get()
    date = entry_02.get()
    agend = entry_03.get()
    service = entry_04.get() 
    footer = entry_05.get()

    writeOnJpg(name, date, agend, service, footer)
    toPDF()
    remove("./src/temp/result.jpg")
    printImage()
    remove("./src/temp/result.pdf")


Button(base, text='Generar', width=20, bg='brown', fg='white', command=create).place(x=180,y=380)
Button(base, text='Generar e imprimir', width=20, bg='brown', fg='white', command=createAndPrint).place(x=180,y=430)
# it will be used for displaying the registration form onto the window  
base.mainloop()  