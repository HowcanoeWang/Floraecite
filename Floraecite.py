# -*- coding: utf-8 -*-
import os, random, xlrd
from tkinter import *
from tkinter.messagebox import *
from PIL import Image
from PIL.ImageTk import PhotoImage

testpicname = "010"
testpickind = ".jpg"
testdatadir = "Data/"
imgdir=testdatadir + testpicname + testpickind

# 打开GUI时，读取xlsx的数据库和Data文件夹下所有的图片列表，并对图片列表进行逆序
def OpeningGUI(datadir):
    ##########
    # Excel读取
    ##########
    rfile = xlrd.open_workbook(datadir+'000.xlsx')
    table = rfile.sheet_by_index(0)
    table.col_values(0)#获取整列的值
    # 预获取列表
    List_Num = table.col_values(0)
    List_SciName = table.col_values(1)
    List_ComName = table.col_values(2)
    List_Latin = table.col_values(3)
    DataBase={'Num':List_Num,'SciName':List_SciName,'ComName':List_ComName,'Latin':List_Latin}
    ##########
    # 图片列表获取与打乱
    ##########
    imagefiles = os.listdir('Data/')
    PicList = imagefiles[1:]
    random.shuffle(PicList)
    # print(PicList)
    # print(DataBase['Num'][2])
    return DataBase, PicList

#def next():
    #flag=0
    #def view_mode():
    #def test_mode():

    #if flag==0:

    #else:

def SelectMode():
    flag=var.get()
    if flag==0: #浏览模式
        Entry_CommonName.config(state='disabled')
        Entry_ScientificName.config(state='disabled')
    else: # 测试模式
        Entry_CommonName.config(state='normal')
        Entry_ScientificName.config(state='normal')
        Entry_CommonName.delete('0',END)
        Entry_ScientificName.delete('0',END)

(DataBase, PicList) = OpeningGUI(testdatadir)


root = Tk()
root.title('Floræcite')
root.config(bg='White')

testimgobj = Image.open(imgdir)
testimgobj.thumbnail((600,800), Image.ANTIALIAS)
imgobj = PhotoImage(testimgobj)
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
Entry_CommonName.config(bg='White',fg='Black',font=('Times', 40, 'normal'),state='disabled')
Entry_ScientificName = Entry(root)
Entry_ScientificName.config(bg='White',fg='Black',font=('Times', 40, 'italic'),state='disabled')


Img.pack(side=LEFT,padx=20,pady=20)

Text_ModeSelect.pack(side=TOP,padx=40,pady=50)
var = IntVar(0)
ModeSelectText=['Viewing mode','Testing mode']
for i in range(2):
    rad = Radiobutton(root,text=ModeSelectText[i],value=i,variable=var,command=SelectMode)
    rad.config(bg='White', fg='Black', font=('Times', 20, 'normal'))
    rad.pack(side=TOP)
Text_CommonName.pack(side=TOP,padx=60,pady=20)
Entry_CommonName.pack(side=TOP,pady=10)
Text_ScientificName.pack(side=TOP,padx=60,pady=30)
Entry_ScientificName.pack(side=TOP,pady=10)

Button_Help.pack(side=LEFT,padx=100)
Button_Next.pack(side=RIGHT,padx=100)

root.mainloop()
print()