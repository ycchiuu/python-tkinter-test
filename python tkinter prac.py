#協助者:秀
"""
MIT license: Chiu
"""
class labelComputer(object):    # 建一個 class
    comType='sf5'               # property
    comSoftware='win 10'
    comMemory='16GB'
    comDisk='512GB'
    comWeight='1050g'
    comBlack='10'
    comWhite='8'
    comRed='5'
    comGreen='5'
    comPrice='25000'
    def __init__(self,ty,sw,mem,disk,wei,bl,wh,red,gr,price):
        self.comType = ty
        self.comSoftware = sw
        self.comMemory = mem
        self.comDisk = disk
        self.comWeight = wei
        self.comBlack = bl
        self.comWhite = wh
        self.comRed = red
        self.comGreen = gr
        self.comPrice = price
    def info(self):
        list1=['型號','軟體','記憶體','硬碟','重量','黑色數量','白色數量','紅色數量','綠色數量','價錢']
        list2=[self.comType,self.comSoftware,self.comMemory,self.comDisk,self.comWeight,self.comBlack,self.comWhite,self.comRed,self.comGreen,self.comPrice]

        for x in range(len(list1)):
            print(list1[x],': ',list2[x])

def onOpen():
    print("開檔")
def onSave():
    print("儲存")

import tkinter as tk
win=tk.Tk()
win.wm_title('電腦庫存2')                   # 視窗標題
#win.iconbitmap("favicon.ico")
win.geometry('400x400')
win.configure(bg='#99e958')
### set menu
menubar = tk.Menu(win)                              #第一層的下拉選單
filemenu = tk.Menu(menubar, tearoff=False)            #第二層file 中的選單
filemenu.add_command(label="Open",command=onOpen)   # 當選取 Open 時，呼叫 onOpen() 函數
filemenu.add_command(label="Save",command=onSave)
menubar.add_cascade(label="File", menu=filemenu)
filemenu = tk.Menu(menubar)
filemenu = tk.Menu(menubar, tearoff=False)
filemenu.add_command(label="Website")
menubar.add_cascade(label="Help", menu=filemenu)
menubar.add_command(label='Exit', command=win.destroy)    # 離開
win.config(menu=menubar)
### 呼叫 class
x=labelComputer(ty='sf514',sw='win 10',mem=16,disk=512,wei=1050,bl=10,wh=8,red=5,gr=5,price=25000)

label1=tk.Label(win,text='型號: '+str(x.comType))
label1.place(x=20, y=60)
label2=tk.Label(win,text='軟體: '+str(x.comSoftware))
label2.place(x=20, y=80)
label3=tk.Label(win,text='記憶體: '+str(x.comMemory)+'GB')
label3.place(x=20, y=100)
label4=tk.Label(win,text='硬碟: '+str(x.comDisk)+'GB')
label4.place(x=20, y=120)
label5=tk.Label(win,text='重量: '+str(x.comWeight)+'g')
label5.place(x=20, y=140)
label6=tk.Label(win,text='產品顏色:').place(x=20, y=170)

chkValue1 = tk.BooleanVar()                                         # 變數值
chkValue2 = tk.BooleanVar()
chkValue3 = tk.BooleanVar()
chkValue1.set(True)                                                 # 預設值
chkcolor1 = tk.Checkbutton(win, text='紅色', var=chkValue1).place(x=20, y=190)   #  打勾
chkcolor2 = tk.Checkbutton(win, text='黑色', var=chkValue2).place(x=20, y=210)   #  打勾
chkcolor3 = tk.Checkbutton(win, text='藍色', var=chkValue3).place(x=20, y=230)   #  打勾

label7=tk.Label(win,text='存放地點:').place(x=20, y=260)

radioValue = tk.IntVar()                               # 元件的變數 int
radioValue.set(1)
whOne = tk.Radiobutton(win, text='台北總公司',variable=radioValue, value=1).place(x=20, y=280)
whTwo = tk.Radiobutton(win, text='中壢倉庫',variable=radioValue, value=2).place(x=20, y=300)
whThree = tk.Radiobutton(win, text='新竹分公司',variable=radioValue, value=3).place(x=20, y=320)

win.mainloop()