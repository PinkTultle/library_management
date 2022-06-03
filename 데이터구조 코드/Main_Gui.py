from tkinter import *
from tkinter import messagebox
from Add_class import Add_Book, Add_User
from Entry_class import Entry_User


win = Tk()


win.geometry("800x450")
win.title("도서 관리 프로그램")
win.resizable(width =FALSE, height = FALSE)

startlabel = Label(win, text = "도서 관리 프로그램",font = ("궁서체",50))
startlabel.place(x = 100, y = 150)

### 도서 관리 메뉴
mainMenu = Menu(win)
win.config(menu = mainMenu)

fileMenu1 = Menu(mainMenu)
mainMenu.add_cascade(label = "도서관리", menu=fileMenu1)
fileMenu1.add_command(label ="도서등록",command=Add_Book)
fileMenu1.add_separator()
fileMenu1.add_command(label = "도서조회")


### 회원 관리 메뉴


win.config(menu = mainMenu)

fileMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label = "회원관리", menu=fileMenu2)
fileMenu2.add_command(label ="회원등록",command=Add_User)
fileMenu2.add_separator()
fileMenu2.add_command(label = "회원조회")
fileMenu2.add_separator()
fileMenu2.add_command(label = "탈퇴회원")


### 대여 관리 메뉴

win.config(menu = mainMenu)

fileMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label = "대여관리", menu=fileMenu2)
fileMenu2.add_command(label ="도서대여")
fileMenu2.add_separator()
fileMenu2.add_command(label = "도서반납")








win.mainloop()