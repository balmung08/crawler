import tkinter
import tkinter.messagebox
interaction = tkinter.Tk()#建立主框
interaction.title("666")#建立主框的标题
interaction.geometry("450x200")#规定主框尺寸
'''
back=tkinter.PhotoImage(file="resource\\background.png")#从某个路径读取图片（png）
tkinter.Label(image=back,anchor = 'nw').place(x=0,y=0)#放置读取的图片
'''
text1 = tkinter.Label(interaction, text="    图片来源为pixiv镜像站pixic",font=20).place(x=10,y=0)#在主框上写文字

#获取输入框的内容，并赋值给value
tag = tkinter.StringVar()
text2 = tkinter.Entry(interaction,textvariable=tag).place(x=150,y=105)
value = tag.get()

#点击按钮即执行相关函数
def code():
    print("666")
yzm =tkinter.Entry(interaction,textvariable=code).place(x=150,y=135)
def int(a):
    print(a)

#菜单栏
menubar = tkinter.Menu(interaction)#新增菜单栏
filemenu = tkinter.Menu(menubar, tearoff=0)#菜单栏新增项
menubar.add_cascade(label='爬取张数', menu=filemenu)#给新增项命名
filemenu.add_command(label='30',command=code)
filemenu.add_command(label='60',command=lambda: int(30))#如果command需要传入值，必须写lambda
helpmenu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='帮助', menu=helpmenu)
interaction.config(menu = menubar)#菜单执行

#弹出提示框
tkinter.messagebox.showinfo('已完成爬取', '已完成爬取，十秒后退出')
#循环执行函数，放在末尾
interaction.mainloop()