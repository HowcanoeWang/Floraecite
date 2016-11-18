# -*- coding: utf-8 -*-
import os, random, xlrd, webbrowser
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askdirectory
from PIL import Image
from PIL.ImageTk import PhotoImage

global view_i, imgobj, picname, MasterList, correctnum, help_flag
root = Tk()
root.title('Floræcite')
root.config(bg='White')

def OpeningGUI(datadir): # 打开GUI时，读取xlsx的数据库和Data文件夹下所有的图片列表，并对图片列表进行逆序
    # Excel读取
    rfile = xlrd.open_workbook(datadir+'000.xlsx')
    table = rfile.sheet_by_index(0)
    table.col_values(0)#获取整列的值
    # 预获取列表
    List_Num = table.col_values(0)
    List_SciName = table.col_values(1)
    List_ComName = table.col_values(2)
    List_Latin = table.col_values(3)
    DataBase={'Num':List_Num,'SciName':List_SciName,'ComName':List_ComName,'Latin':List_Latin}

    # 图片列表获取与打乱
    imagefiles = os.listdir('Data/')
    PicList = imagefiles[1:]
    random.shuffle(PicList)
    # print(PicList)
    # print(DataBase['Num'][2])
    return DataBase, PicList

def SelectMode():
    global picname,view_i
    flag=var.get()
    if flag==0: #浏览模式
        if askyesno('Verify', 'Do you really want to switch to viewing mode? This will reutrn to begining'):
            view_i = 0
            picname = PicList[0][:-4]
            imgdir = datadir + picname + pickind
            imgobj = image_load(imgdir)
            Img.config(image=imgobj)
            name_show(picname)
            Entry_CommonName.config(state='disabled')
            Entry_ScientificName.config(state='disabled')
            fresh_label()
        else:
            var.set(1)
    else: # 测试模式
        Entry_CommonName.config(state='normal')
        Entry_ScientificName.config(state='normal')
        Entry_CommonName.delete('0',END)
        Entry_ScientificName.delete('0',END)
        name_show(picname)

def image_load(imgdir):
    global imgobj
    testimgobj = Image.open(imgdir)
    #testimgobj.thumbnail((600,800), Image.ANTIALIAS)
    testimgobj = testimgobj.resize((600,800), Image.ANTIALIAS)
    imgobj = PhotoImage(testimgobj)
    return imgobj

def linkclick(event):
    webbrowser.open_new(r"https://github.com/HowcanoeWang/Floraecite")

def name_show(x):
    # x 为PicName
    Entry_CommonName.config(state='normal')
    Entry_ScientificName.config(state='normal')
    num = DataBase['Num'].index(x)
    SciName = DataBase['SciName'][num]
    ComName = DataBase['ComName'][num]
    Latin = DataBase['Latin'][num]
    if var.get()==0: # 查看模式
        if Latin==0: # 不要求拉丁名
            Entry_CommonName.delete('0', END)
            Entry_CommonName.insert(0, ComName)
            Entry_CommonName.config(state='disable')
            Entry_ScientificName.delete('0', END)
            Entry_ScientificName.config(state='disable')
        else: # 要求拉丁名
            Entry_CommonName.delete('0', END)
            Entry_CommonName.insert(0, ComName)
            Entry_CommonName.config(state='disable')
            Entry_ScientificName.delete('0', END)
            Entry_ScientificName.insert(0, SciName)
            Entry_ScientificName.config(state='disable')
    else: # 测试模式
        if Latin==0: # 不要求拉丁名
            Entry_CommonName.delete('0', END)
            Entry_CommonName.config(state='normal')
            Entry_ScientificName.delete('0', END)
            Entry_ScientificName.config(state='disable')
        else: # 要求拉丁名
            Entry_CommonName.delete('0', END)
            Entry_CommonName.config(state='normal')
            Entry_ScientificName.delete('0', END)
            Entry_ScientificName.config(state='normal')
    return SciName,ComName,Latin

def next():
    global view_i, imgobj,picname, correctnum, help_flag, MasterList
    if view_i >= Len-1: # 如果超过了图片数
        showinfo('Congratulation!', 'All pictures have been viewed!')
        view_i = 0
        picname = PicList[0][:-4]
        pickind = PicList[0][-4:]
        imgdir = datadir + picname + pickind
        imgobj = image_load(imgdir)
        Img.config(image=imgobj)
        name_show(picname)
        fresh_label()
    else:
        if var.get() == 0:  # 查看模式
            view_i += 1
            picname = PicList[view_i][:-4]
            pickind = PicList[view_i][-4:]
            imgdir = datadir + picname + pickind
            imgobj = image_load(imgdir)
            Img.config(image=imgobj)
            name_show(picname)
            fresh_label()
        else:# 测试模式
            picname = PicList[view_i][:-4]
            pickind = PicList[view_i][-4:]
            Input_ComName = Entry_CommonName.get()
            Input_SciName = Entry_ScientificName.get()
            (SciName,ComName,Latin)=name_show(picname)
            # print(Input_ComName,Input_SciName,ComName,SciName)
            flag =False
            if Input_ComName != ComName: # 如果输入的common name不正确
                showerror(title="Error!",message="Common name is not correct! Check the spelling please!")
            else: # 如果输入的common name正确
                Entry_CommonName.insert(END,Input_ComName)
                if Latin==1: # 需要写拉丁名
                    if Input_SciName != SciName: # 拉丁名不正确
                        showerror(title="Error!", message="Scientific name is not correct! Check the spelling please!")
                    else: # 拉丁名填写正确
                        flag = True
                else: # 不需要写拉丁名
                    flag = True
            if flag:
                if not help_flag: # 如果没有求助且做对了，则熟练度+1
                    correctnum += 1
                    MasterList[PicList[view_i]] += 1
                view_i += 1
                picname = PicList[view_i][:-4]
                pickind = PicList[view_i][-4:]
                imgdir = datadir + picname + pickind
                imgobj = image_load(imgdir)
                Img.config(image=imgobj)
                name_show(picname)
                Button_Help.config(state='disabled')
                fresh_label()
                help_flag = False
            else:
                Button_Help.config(state='normal')

def help():
    global help_flag
    picname = PicList[view_i][:-4]
    (SciName, ComName, Latin) = name_show(picname)
    if askyesno('Notice:','R U sure asking for help?'):
        Input_ComName = Entry_CommonName.get()
        Input_SciName = Entry_ScientificName.get()
        help_flag = True
        if Input_ComName != ComName:
            Entry_CommonName.delete('0',END)
            Entry_CommonName.insert(END,ComName)
        if Input_ComName != ComName and Latin==1:
            Entry_ScientificName.delete('0', END)
            Entry_ScientificName.insert(END,SciName)

def fresh_label():
    global view_i, correctnum
    Text_Infomation.config(text='Page: ' + str(view_i+1) + '/' + str(Len) + '\n Correct number:' + str(correctnum))
#####################################################################
# opening GUI
# Ask = askdirectory(title='Select a data folder')
# datadir = Ask+'/'
datadir = 'Data/'
correctnum = 0
help_flag = False
(DataBase, PicList) = OpeningGUI(datadir)
Len = len(PicList)
if os.path.isfile('memeory.floraecite'):  # 如果日志文件存在
    f = open('memeory.floraecite', 'r')
    MasterList = eval(f.read())
    if len(MasterList)<Len: # 缺少了图片
        for j in range(Len):
            if not PicList[j] in MasterList: # 如果不在字典里
                MasterList[PicList[j]] = 1
    f.close()
else:
    f = open( 'memeory.floraecite', 'w')
    MasterList = {}
    for i in range(Len):
        MasterList[PicList[i]]=1
    f.write(str(MasterList))
    f.close()
view_i = 0
# loading Image
picname = PicList[0][:-4]
pickind = PicList[0][-4:]
imgdir=datadir + picname + pickind
imgobj = image_load(imgdir)
Img = Label(root, image=imgobj)
# loading names
num = DataBase['Num'].index(picname)
Latin = DataBase['Latin'][num]
ComName = DataBase['ComName'][num]
if Latin == 0: # 不需要拉丁名
    SciName = ''
else: #需要拉丁名
    SciName = DataBase['SciName'][num]
#####################################################################

Text_ModeSelect = Label(root,text='Mode select:')
Text_ModeSelect.config(bg='White',fg='Black',font=('Times', 30, 'normal'))
Text_CommonName = Label(root,text='Common name')
Text_CommonName.config(bg='White',fg='Black',font=('Times', 40, 'normal'))
Text_ScientificName = Label(root,text='Scientific name')
Text_ScientificName.config(bg='White',fg='Black',font=('Times', 40, 'italic'))
Text_Link = Label(root,text='https://github.com/HowcanoeWang/Floraecite' )
Text_Link.config(bg='White',fg='Blue',font=('Times', 10, 'underline'),cursor='hand2')
Text_Author = Label(root,text='Author: WANG Hao-Zhou \n Version: Beta 1.5.0' )
Text_Author.config(bg='White',fg='Black',font=('Times', 10, 'normal'))
Text_Infomation = Label(root,text='Page: ' + str(view_i+1) + '/' + str(Len) + '\n Correct number:' + str(correctnum))
Text_Infomation.config(bg='White',fg='Black',font=('Times', 20, 'normal'))
Button_Help = Button(root,text='Help',command=help)
Button_Help.config(bg='White',fg='Black',font=('Times', 30, 'normal'),state='disabled')
Button_Next = Button(root,text='Next',command=next)
Button_Next.config(bg='White',fg='Black',font=('Times', 30, 'normal'))
Entry_CommonName = Entry(root)
Entry_CommonName.insert(0, ComName)
Entry_CommonName.config(bg='White',fg='Black',font=('Times', 40, 'normal'),state='disabled')
Entry_ScientificName = Entry(root)
Entry_ScientificName.insert(0, SciName)
Entry_ScientificName.config(bg='White',fg='Black',font=('Times', 40, 'italic'),state='disabled')

Img.pack(side=LEFT,padx=20,pady=20)

Text_Link.pack(side=TOP)
Text_Link.bind("<Button-1>", linkclick)
Text_Author.pack(side=TOP)
Text_ModeSelect.pack(side=TOP,padx=40,pady=20)
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
Text_Infomation.pack(side=TOP)

Button_Help.pack(side=LEFT,padx=100)
Button_Next.pack(side=RIGHT,padx=100)

root.mainloop()
f = open( 'memeory.floraecite', 'w')
f.write(str(MasterList))
f.close()