# -*- coding: utf-8 -*-
# packing code
# pyinstaller -i D:\OneDrive\Program\Python\Floraecite\Source_code\floraecite.ico -F -w D:\OneDrive\Program\Python\Floraecite\Source_code\Floraecite.py
import os, sys, random, xlrd, webbrowser,base64
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askdirectory
from PIL import Image
from PIL.ImageTk import PhotoImage
from icon import img
import urllib.request


global view_i, imgobj, picname, MasterList, correctnum, help_flag
root = Tk()
root.title('Floræcite')
root.config(bg='White')
root.wm_state( 'zoomed' )
tmp = open("tmp.png","wb+")
tmp.write(base64.b64decode(img))
tmp.close()
icon = PhotoImage(file='tmp.png')
root.tk.call('wm', 'iconphoto', root._w, icon)
os.remove("tmp.png")

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
    imagefiles = os.listdir(datadir)
    imagefiles.remove('000.xlsx')
    for i in range(len(imagefiles)):
        string=imagefiles[i]
        if string.find('jpg')==-1 and string.find('png')==-1 and string.find('gif')==-1:
            imagefiles.remove(string)
    PicList = imagefiles
    random.shuffle(PicList)
    return DataBase, PicList

def SelectMode():
    global picname,view_i, correctnum
    flag=var.get()
    if flag==0: #浏览模式
        if Entry_CommonName.cget('state') == 'normal':
            if askyesno('Verify', 'Do you really want to switch to viewing mode? This will reutrn to begining'):
                view_i = 0
                correctnum = 0
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
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    testimgobj = Image.open(imgdir)
    #testimgobj.thumbnail((600,800), Image.ANTIALIAS)
    testimgobj = testimgobj.resize((int(w/2.5),int(h-100)), Image.ANTIALIAS)
    imgobj = PhotoImage(testimgobj)
    return imgobj

def linkclick(event=None):
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

def Next_Page(event=None):
    global view_i, imgobj,picname, correctnum, help_flag, ComName_flag, MasterList
    print(view_i)
    if var.get() == 0:  # viewing mode
        if view_i >= Len-1: # exceed picture number
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
            view_i += 1
            picname = PicList[view_i][:-4]
            pickind = PicList[view_i][-4:]
            imgdir = datadir + picname + pickind
            imgobj = image_load(imgdir)
            Img.config(image=imgobj)
            name_show(picname)
            fresh_label()
    else:# testing mode
        picname = PicList[view_i][:-4]
        pickind = PicList[view_i][-4:]
        Input_ComName = Entry_CommonName.get()
        Input_SciName = Entry_ScientificName.get()
        (SciName,ComName,Latin)=name_show(picname)
        flag = False
        if Input_ComName != ComName: # if common name incorrect 如果输入的common name不正确
            showerror(title="Error!",message="Common name is not correct! Check the spelling please!")
        else: # 如果输入的common name正确  if common name correct
            Entry_CommonName.insert(END,Input_ComName)
            if Latin==1: # 需要写拉丁名
                if Input_SciName != SciName: # if Latin name incorrect 拉丁名不正确
                    showerror(title="Error!", message="Scientific name is not correct! Check the spelling please!")
                    Entry_ScientificName.insert(END, Input_SciName)
                    if Button_Help.cget('state') == 'disabled':  # Common name correct @ 1st time
                        ComName_flag = True
                else: # 拉丁名填写正确 if Latin name correct
                    flag = True
            else: # 不需要写拉丁名 if Latin name not required
                flag = True
        if flag:
            if not help_flag: # if not help and correct, Mastery +1 如果没有求助且做对了，则熟练度+1
                correctnum += 1
                MasterList[PicList[view_i]] += 1
                if Button_Help.cget('state')=='disabled': # if correct in the first time Mastery +0.2 again 不但做对了，而且一次通关，熟练度再加0.2
                    MasterList[PicList[view_i]] += 0.2
                elif ComName_flag: # Common name correct @ 1st time BUT scientific name not right
                    MasterList[PicList[view_i]] += 0.1
            view_i += 1
            if view_i > Len-1: # If come to the last picture
                showinfo('Congratulation!', 'All pictures have been tested!')
                view_i = 0
            picname = PicList[view_i][:-4]
            pickind = PicList[view_i][-4:]
            imgdir = datadir + picname + pickind
            imgobj = image_load(imgdir)
            Img.config(image=imgobj)
            name_show(picname)
            Button_Help.config(state='disabled')
            fresh_label()
            help_flag = False
            ComName_flag = False
        else:
            Button_Help.config(state='normal')

def help():
    global help_flag
    picname = PicList[view_i][:-4]
    (SciName, ComName, Latin) = name_show(picname)
    if askyesno('Notice:','Are you sure asking for help?'):
        Input_ComName = Entry_CommonName.get()
        Input_SciName = Entry_ScientificName.get()
        help_flag = True
        if Input_ComName != ComName:
            Entry_CommonName.delete('0',END)
            Entry_CommonName.insert(END,ComName)
        if Input_ComName != ComName and Latin==1:
            Entry_ScientificName.delete('0', END)
            Entry_ScientificName.insert(END,SciName)

def fresh_label(): # fresh the text in the correct display label 更新正确数量的显示标签
    global view_i, correctnum
    Text_Infomation.config(text='Page: ' + str(view_i+1) + '/' + str(Len) +  '  Mastery: ' + str(MasterList[PicList[view_i]]) + '\n Correct number:' + str(correctnum))

def map_sort(dict): # Mastery rank method 熟练度排序算法
    dicted = list(sorted(dict.items(), key=lambda e:e[1], reverse=False))
    res = []
    for i in range(len(dicted)):
        res.append(dicted[i][0])
    return res

def NewVersionDetect():
    flag = False
    try:
        r = urllib.request.urlopen('https://github.com/HowcanoeWang/Floraecite/tree/master/Source_Code')
        html = str(r.read())
        VersionIndex=html.find('Latest_version_')
        if VersionIndex>=0:
            EndIndex = html.find('.txt')
            global WebVersionNum
            WebVersionNum=html[VersionIndex+15:EndIndex]
            if WebVersionNum != VersionNum:
                flag = True
        else:
            flag = False
    except(urllib.error.URLError):
        flag=False
        print('network failed')
    return flag

def NewPictureDectect():
    try:
        r = urllib.request.urlopen('https://github.com/HowcanoeWang/Floraecite/tree/master/Source_Code')
        html = str(r.read())
        PictureIndex=html.find('UNBPicNum_')
        if PictureIndex>=0:
            EndIndex = html.find('.num')
            global WebVersionNum
            WebPictureNum=html[PictureIndex+10:EndIndex]
            if int(WebPictureNum) > len(__PicList__):
                answer=askokcancel('New pictures','New pictures have been released, download?')
                if answer:
                    webbrowser.open_new(r"https://github.com/HowcanoeWang/Floraecite/releases")
    except(urllib.error.URLError):
        print('network failed')

def download_exe():
    def reporthook(count, block_size, total_size):
        percent = int(count * block_size * 100 / total_size)
        percent_str="Download %d%%, %.1f / %.1f MB"%(percent,(count*block_size)/(1024**2),total_size/(1024**2))
        root.title(percent_str)
    global WebVersionNum
    download_URL = 'https://github.com/HowcanoeWang/Floraecite/raw/master/Source_Code/Floraecite(' + WebVersionNum + ').exe'
    download_exename = 'Floraecite(' + WebVersionNum + ').exe'
    urllib.request.urlretrieve(download_URL, download_exename, reporthook)
    showinfo('Done', 'New version has been downloaded!')
    sys.exit()

#####################################################################
'''opening GUI'''
VersionNum='v1.0'
if NewVersionDetect():
    answer=askokcancel(title='Update Notes',message='New version detected, update now?')
    if answer: # if user click download
        # foo_thread = threading.Thread(target=download_exe)
        # foo_thread.start()
        # from tkinter import ttk
        # win = Toplevel(root)
        # ProgressBar = ttk.Progressbar(win, orient="horizontal", length=200, mode="determinate")
        # ProgressBar["value"] = 0
        # ProgressBar["maximum"] = 100
        #ProgressBar.pack(expand=YES, fill=BOTH)
        download_exe()
        # win.mainloop()
Ask = askdirectory(title='Select a picture data folder',initialdir=os.getcwd())
if Ask != '':
    datadir = Ask+'/'
else:
    datadir = 'Data/'
if os.path.exists(datadir[:-1]):
    if not os.path.exists(datadir + '000.xlsx'):
        showwarning('Error!', 'No found [000.xlsx] in the ['+ datadir[:-1]+ ']folder')
        sys.exit()
else:
    showwarning('Error!', 'No folder called [' + datadir[:-1] +  ']')
    sys.exit()
correctnum = 0
help_flag = False
ComName_flag = False
(DataBase, __PicList__) = OpeningGUI(datadir)
NewPictureDectect()
for i in range(len(__PicList__)):
    if not __PicList__[i][:-4] in DataBase['Num']:
        showwarning('Error!','No picture file names [' + __PicList__[i][:-4] + '] in the 000.xlsx')
        sys.exit()
Len = len(__PicList__)
if os.path.isfile(datadir + 'memeory.floraecite'):  # if log file exist # 如果日志文件存在
    f = open(datadir + 'memeory.floraecite', 'r')
    MasterList = eval(f.read())
    if map_sort(MasterList) != __PicList__:
        __PicListLog__ = map_sort(MasterList)
        __AddedPic__=list(set(__PicList__)-set(__PicListLog__)) # 在文件夹中但是不在log文件中的
        __MissedPic__ =list( set(__PicListLog__) - set(__PicList__))  # 在log中但是不在文件夹中的文件
        for m in range(len(__MissedPic__)):
            del MasterList[__MissedPic__[m]]
        for a in range(len(__AddedPic__)):
            MasterList[__AddedPic__[a]] = 0
    f.close()
else:
    f = open(datadir +  'memeory.floraecite', 'w')
    MasterList = {}
    for i in range(Len):
        MasterList[__PicList__[i]]=0
    f.write(str(MasterList))
    f.close()
view_i = 0
PicList = map_sort(MasterList)
# loading Image
picname = PicList[0][:-4]
pickind = PicList[0][-4:]
imgdir=datadir + picname + pickind
imgobj = image_load(imgdir)
# loading names
num = DataBase['Num'].index(picname)
Latin = DataBase['Latin'][num]
ComName = DataBase['ComName'][num]
if Latin == 0: # 不需要拉丁名
    SciName = ''
else: #需要拉丁名
    SciName = DataBase['SciName'][num]
#####################################################################

#####################################################################
'''New Controls'''
w = int(root.winfo_screenwidth()/100)
h = int(root.winfo_screenheight()/100)

Img = Label(root, image=imgobj)
Img.config(bg='White')
Text_ModeSelect = Label(root,text='Mode select:')
Text_ModeSelect.config(bg='White',fg='Black',font=('Times', h*3, 'normal'))
Text_CommonName = Label(root,text='Common name')
Text_CommonName.config(bg='White',fg='Black',font=('Times', h*5, 'normal'))
Text_ScientificName = Label(root,text='Scientific name')
Text_ScientificName.config(bg='White',fg='Black',font=('Times', h*5, 'italic'))
Text_Link = Label(root,text='https://github.com/HowcanoeWang/Floraecite' )
Text_Link.config(bg='White',fg='Blue',font=('Times', h, 'underline'),cursor='hand2')
Text_Author = Label(root,text='Author: WANG Hao-Zhou \n Version: '+ VersionNum)
Text_Author.config(bg='White',fg='Black',font=('Times', h, 'normal'))
Text_Infomation = Label(root,text='Page: ' + str(view_i+1) + '/' + str(Len) + '  Mastery: ' + str(MasterList[PicList[view_i]]) + '\n Correct number:' + str(correctnum))
Text_Infomation.config(bg='White',fg='Black',font=('Times', h*2, 'normal'))
Button_Help = Button(root,text='Help',command=help)
Button_Help.config(bg='White',fg='Black',font=('Times', h*4, 'normal'),state='disabled')
Button_Next = Button(root,text='Next',command=Next_Page)
Button_Next.config(bg='White',fg='Black',font=('Times', h*4, 'normal'))
Entry_CommonName = Entry(root)
Entry_CommonName.insert(0, ComName)
Entry_CommonName.config(bg='White',fg='Black',font=('Times', h*5, 'normal'),state='disabled')
Entry_ScientificName = Entry(root)
Entry_ScientificName.insert(0, SciName)
Entry_ScientificName.config(bg='White',fg='Black',font=('Times', h*5, 'italic'),state='disabled')
######################################################################

######################################################################
'''Putting controls'''
Img.pack(side=LEFT,padx=w,pady=w,expand=YES,fill=BOTH)

Text_Link.pack(side=TOP,expand=YES,fill=BOTH)
Text_Link.bind("<Button-1>", linkclick)
Text_Author.pack(side=TOP,expand=YES,fill=BOTH)
Text_ModeSelect.pack(side=TOP,expand=YES,padx=w*3,pady=h*2,fill=BOTH)
var = IntVar(0)
ModeSelectText=['Viewing mode','Testing mode']
for i in range(2):
    rad = Radiobutton(root,text=ModeSelectText[i],value=i,variable=var,command=SelectMode)
    rad.config(bg='White', fg='Black', font=('Times', h*2, 'normal'))
    rad.pack(side=TOP,expand=YES,fill=BOTH)
Text_CommonName.pack(side=TOP,padx=w*4,pady=h*2,expand=YES,fill=BOTH)
Entry_CommonName.pack(side=TOP,padx=w,pady=h,expand=YES,fill=BOTH)
Entry_CommonName.bind('<Return>', Next_Page)
Text_ScientificName.pack(side=TOP,padx=w*4,pady=h*4,expand=YES,fill=BOTH)
Entry_ScientificName.pack(side=TOP,padx=w,pady=h,expand=YES,fill=BOTH)
Entry_ScientificName.bind('<Return>', Next_Page)
Text_Infomation.pack(side=TOP,expand=YES,fill=BOTH)

Button_Help.pack(side=LEFT,padx=w*6,expand=YES,fill=BOTH)
Button_Next.pack(side=RIGHT,padx=w*6,expand=YES,fill=BOTH)
# Button_Next.bind('<Button-1>', Next_Page)

root.mainloop()
########################################################################
'''Save log files when exit'''
f = open(datadir +  'memeory.floraecite', 'w')
f.write(str(MasterList))
f.close()