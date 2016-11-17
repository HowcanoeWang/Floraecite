# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
from PIL import Image
from PIL.ImageTk import PhotoImage
# from picture import *

root = Tk()
root.title('Floræcite')
root.config(bg='White')

testpicname = "010"
testpickind = ".jpg"
testdatadir = "Data/"
imgdir=testdatadir + testpicname + testpickind

testimgobj = Image.open(imgdir)
testimgobj.thumbnail((600,800), Image.ANTIALIAS)
testimgobj.save(testdatadir + testpicname+ '_thumb' + testpickind)
imgobj = PhotoImage(file=testdatadir + testpicname+ '_thumb' + testpickind)
Img = Label(root,image=imgobj)

Text_ModeSelect = Label(root,text='Mode select:')
Text_ModeSelect.config(bg='White',fg='Black',font=('Times', 30, 'normal'))
Text_CommonName = Label(root,text='Common name')
Text_CommonName.config(bg='White',fg='Black',font=('Times', 40, 'normal'))
Text_ScientificName = Label(root,text='Scientific name')
Text_ScientificName.config(bg='White',fg='Black',font=('Times', 40, 'italic'))
Button_Help = Button(root,text='Help')
Button_Help.config(bg='White',fg='Black',font=('Times', 30, 'normal'))
Button_Next = Button(root,text='Next')
Button_Next.config(bg='White',fg='Black',font=('Times', 30, 'normal'))
Entry_CommonName = Entry(root)
Entry_CommonName.config(bg='White',fg='Black',font=('Times', 40, 'normal'))
Entry_ScientificName = Entry(root)
Entry_ScientificName.config(bg='White',fg='Black',font=('Times', 40, 'italic'))

Img.pack(side=LEFT,padx=20,pady=20)

Text_ModeSelect.pack(side=TOP,padx=40,pady=50)
Text_CommonName.pack(side=TOP,padx=60,pady=30)
Entry_CommonName.pack(side=TOP,pady=10)
Text_ScientificName.pack(side=TOP,padx=60,pady=30)
Entry_ScientificName.pack(side=TOP,pady=10)

Button_Help.pack(side=LEFT,padx=100)
Button_Next.pack(side=RIGHT,padx=100)

root.mainloop()