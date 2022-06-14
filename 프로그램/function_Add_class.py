from tkinter import *
from tkinter import messagebox
import pandas as pd
from GUI_Entry_class import Entry_User,Entry_Book

### 회원 등록 클래스

class Add_User ():

    ##생성자
    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x300")
        self.window.title("신규 회원 등록")
        self.window.resizable(width = FALSE, height=FALSE)
        
        self.user_add = Entry_User(self.window,x=100, y =10)
        


        self.window.mainloop()

      

class Add_Book ():


    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x400")
        self.window.title("도서 등록")
        self.window.resizable(width = FALSE, height=FALSE)

        self.book_add = Entry_Book(self.window,x=100, y =10)


        self.window.mainloop()

