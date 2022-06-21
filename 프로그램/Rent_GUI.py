from tkinter import *
from tkinter import ttk
import pandas as pd
from datetime import datetime, timedelta
from tkinter import messagebox


Day = datetime.now()
RentDay = Day.strftime('%Y-%m-%d')
ReturnDay = (Day + timedelta(weeks= 2)).strftime('%Y-%m-%d')


class Rent_Table :

    def __init__(self, num):
        self.user_num = num

    
    def Load_table(self, num) :
        self.wind = Tk()
        self.wind.geometry("600x400")
        self.wind.title("도서 대여")
        self.wind.resizable(width =FALSE, height = FALSE)

        self.book = pd.read_csv('csv/BOOK.csv', encoding= 'utf-8', dtype= str)
        self.book = self.book[['BOOK_ISBN','BOOK_TITLE','BOOK_AUTHOR','BOOK_PUB','BOOK_PRE']]

        self.a = ["책 제목","ISBN 명"]
        self.C_combobox = ttk.Combobox(self.wind,values=self.a,state="readonly")
        self.C_combobox.place(x=30,y=43,width=100)
        self.C_combobox.set("책 제목")

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
        self.book_tree.column("출판사",anchor=W, width=135,minwidth=135,stretch=NO)
        
        self.book_tree.heading("#0",text="",anchor=W)
        self.book_tree.heading("ISBN",text="ISBN",anchor=W)
        self.book_tree.heading("도서명",text="도서명",anchor=W)
        self.book_tree.heading("저자",text="저자",anchor=W)       
        self.book_tree.heading("출판사",text="출판사",anchor=W)

        
        self.book = self.book[self.book['BOOK_PRE'] == 'True']

        for i in self.book.index.tolist() :
            self.book_tree.insert('', 'end', text=i,values=list(self.book.loc[i])) 

        self.book_tree.place(x=30,y=90,width=540,height=250)

        self.wind.bind('<Double-Button-1>', self.rant)
        self.wind.mainloop()

        

    def rant(self, event ) :

        self.stuser = str(self.user_num)

        double_click = self.book_tree.focus()
        self.getTable = self.book_tree.item(double_click).get('values')
        
        self.stbook = str(self.getTable[0])
        print(self.stbook)
        self.book = pd.read_csv('csv/BOOK.csv', encoding= 'utf-8', dtype= str)
        self.book = self.book.set_index('BOOK_ISBN', drop=False)
        self.user = pd.read_csv('csv/USER.csv', encoding= 'utf-8', dtype= str)
        self.user = self.user.set_index('USER_PHONE', drop=False)
        self.rent = pd.read_csv('csv/RENT.csv', encoding= 'utf-8', dtype= str)

        self.new_rent = pd.DataFrame({'RENT_ISBN' : self.stbook,
        'RENT_BOOK' : self.book.loc[self.stbook,'BOOK_TITLE'] ,
        'RENT_USER' : [self.stuser],
        'RENTAL_DATA' : [RentDay],
        'RETURN_DATA' : [ReturnDay],
        'RETURN_VALUE' : [self.book.loc[self.stbook,'BOOK_PRE']]})
        self.new_rent = self.new_rent.set_index('RENT_ISBN', drop=False) 

        self.user = self.user.astype({'USER_RENT_CNT':int})
        self.user.loc[self.stuser,'USER_RENT_CNT'] -= 1 
        self.user.to_csv('csv/USER.csv', mode = 'w' ,index= None, header= True)

        self.book.loc[self.stbook,'BOOK_PRE'] = False
        self.book.to_csv('csv/BOOK.csv', mode= 'w', index= None, header= True)

        self.new_rent.to_csv('csv/RENT.csv', mode='a', index = False, header= None)
        messagebox.showinfo("도서대여", "도서 대여 성공")
        self.quit()


    def quit(self) :
        self.wind.quit()
        self.wind.destroy()
        