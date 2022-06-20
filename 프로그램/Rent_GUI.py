from tkinter import *
from tkinter import ttk
import pandas as pd

class Rent_Table () :

    def __init__(self) :

        self.wind = Tk()
        self.wind.geometry("600x400")
        self.wind.title("도서 대여")
        self.wind.resizable(width =FALSE, height = FALSE)

        self.book = pd.read_csv('csv/BOOK.csv', encoding= 'utf-8', dtype= str)
        self.book = self.book[['BOOK_ISBN','BOOK_TITLE','BOOK_AUTHOR','BOOK_PUB']]
        
        
        
        self.Load_table()
        self.wind.mainloop()

    def Load_table(self) :

        self.a = ["책 제목","ISBN 명"]
        self.C_combobox = ttk.Combobox(self.wind,values=self.a,state="readonly")
        self.C_combobox.place(x=30,y=43,width=100)
        self.C_combobox.set("선택")

        self.labeltitle = Label(self.wind,text="대여 가능한 도서",font=("맑은고딕", 12,"bold")).place(x=30,y=10)

        self.search_book = Entry(self.wind)
        self.search_book.place(x=155,y=43,width=300)

        self.Search_button = Button(self.wind,text="검색",bg="lightsteelblue")
        self.Search_button.place(x=490,y=41,width=80,height=30)

        self.book_tree = ttk.Treeview(self.wind)
        
        
        self.book_tree['columns'] = ("ISBN","도서명","저자","출판사")
        
        self.book_tree.column("#0",width=0, stretch=NO)
        self.book_tree.column("ISBN",anchor=W,width=140,minwidth=140, stretch=NO)
        self.book_tree.column("도서명",anchor=W, width=140,minwidth=140, stretch=NO)
        self.book_tree.column("저자",anchor=W, width=120,minwidth=140,stretch=NO)
        self.book_tree.column("출판사",anchor=W, width=140,minwidth=140,stretch=NO)
        
        self.book_tree.heading("#0",text="",anchor=W)
        self.book_tree.heading("ISBN",text="ISBN",anchor=W)
        self.book_tree.heading("도서명",text="도서명",anchor=W)
        self.book_tree.heading("저자",text="저자",anchor=W)       
        self.book_tree.heading("출판사",text="출판사",anchor=W)

        for i in range(len(self.book.index)) :
            self.book_tree.insert('', 'end', text=i,values=list(self.book.loc[i])) 

        self.book_tree.place(x=30,y=90,width=540,height=250)

       


abc = Rent_Table()



        
        


