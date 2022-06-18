from tkinter import *
from tkinter import ttk
import pandas as pd

class TREE():

    def __init__(self) :
        self.win = Tk()

        self.win.geometry("800x450")
        self.win.title("도서 관리 프로그램")
        self.win.resizable(width =FALSE, height = FALSE)
    
        self.tree = ttk.Treeview(self.win)
        

        ## 검색창
        self.search_Entry = Entry(self.win)
        self.search_Entry.place(x=200,y=50,width=350)

        ### 검색 버튼
        self.Spec_Search_button = Button(self.win,text="검색",bg="lightsteelblue")
        self.Spec_Search_button.place(x=650,y=45,width=80,height=30)

        self.tree.place(x=30,y=100,width=740,height=300)


        #각각의 csv파일 불러와서 데이터 프레임에 산입후 출력에 맞게 변경
        self.book = pd.read_csv('csv/BOOK.csv', encoding= 'utf-8', dtype= str)
        self.user = pd.read_csv('csv/USER.csv', encoding= 'utf-8', dtype= str)
        self.rent = pd.read_csv('csv/RENT.csv', encoding= 'utf-8', dtype= str)

        self.rent = self.rent[['RENT_ISBN','RENT_USER','RENTAL_DATA','RETURN_DATA','RETURN_VALUE']]
        self.book = self.book[['BOOK_IMAGE','BOOK_ISBN','BOOK_TITLE','BOOK_AUTHOR','BOOK_PRICE','BOOK_LINK']]
        self.user = self.user[['USER_IMAGE','USER_PHONE','USER_NAME','USER_RENT_CNT','USER_MAIL']]
        #불러온 csv파일의 데이터중 출력할 데이터 열을 추출하여 새로운 데이터 프레임 생성


        self.win.mainloop()
        

    def showTree(self , mode) :

        if mode == '도서' :
            self.book_tree()
        
        if mode == '회원' :
            self.user_tree()
            
        if mode == '탈퇴회원':
            self.Delete_User()
            
        if mode == '대여' :
            self.rent_tree()

        if mode == '반납':
            self.return_tree()



    def book_tree(self) :

        a = ["책 제목","ISBN 명"]
        self.Phone_combobox = ttk.Combobox(self.win,values=a,state="readonly")
        self.Phone_combobox.place(x=30,y=50,width=100)
        self.Phone_combobox.set("선택")

        self.labeltitle = Label(self.win,text="도서 조회",font=("맑은고딕", 12,"bold")).place(x=30,y=10)


        self.tree['columns'] = ("사진","ISBN","도서명","저자","가격","출판사")

        self.tree.column("#0",width=0, stretch=NO)
        self.tree.column("사진",anchor=W,width=120,minwidth=120, stretch=NO)
        self.tree.column("ISBN",anchor=W,width=80,minwidth=80, stretch=NO)
        self.tree.column("도서명",anchor=W, width=80,minwidth=80, stretch=NO)
        self.tree.column("저자",anchor=W, width=80)
        self.tree.column("가격",anchor=W, width=80)
        self.tree.column("출판사",anchor=W, width=80)

        self.tree.heading("#0",text="",anchor=W)
        self.tree.heading("사진",text="사진",anchor=W)
        self.tree.heading("ISBN",text="ISBN",anchor=W)
        self.tree.heading("도서명",text="도서명",anchor=W)
        self.tree.heading("저자",text="저자",anchor=W)
        self.tree.heading("가격",text="가격",anchor=W)
        self.tree.heading("출판사",text="출판사",anchor=W)

        for i in range(len(self.book.index)) :
            self.tree.insert('', 'end', text=i,values=list(self.book.loc[i])) 

    def user_tree(self) :

        #####
        #이부분에 탈퇴상태 아닌 회원만 출력하도록 데이터 프에림 검색 코드 넣어야함
        #####

        self.labeltitle = Label(self.win,text="회원 조회",font=("맑은고딕", 12,"bold")).place(x=30,y=10)

        a = ["이름","전화번호"]
        self.Phone_combobox = ttk.Combobox(self.win,values=a,state="readonly")
        self.Phone_combobox.place(x=30,y=50,width=100)
        self.Phone_combobox.set("선택")

        self.tree['columns'] = ("사진","전화번호","이름","대여가능권수","이메일")

        self.tree.column("#0",width=0, stretch=NO)
        self.tree.column("사진",anchor=W,width=120,minwidth=120, stretch=NO)
        self.tree.column("전화번호",anchor=W,width=120,minwidth=80, stretch=NO)
        self.tree.column("이름",anchor=W, width=80,minwidth=80, stretch=NO)
        self.tree.column("대여가능권수",anchor=W, width=30)
        self.tree.column("이메일",anchor=W, width=120)

        self.tree.heading("#0",text="",anchor=W)
        self.tree.heading("사진",text="사진",anchor=W)
        self.tree.heading("전화번호",text="전화번호",anchor=W)
        self.tree.heading("이름",text="이름",anchor=W)
        self.tree.heading("대여가능권수",text="대여가능권수",anchor=W)
        self.tree.heading("이메일",text="이메일",anchor=W)

        for i in range(len(self.user.index)) :
            self.tree.insert('', 'end', text=i,values=list(self.user.loc[i])) 

    def Delete_User(self) :

        #####
        #이부분에 탈퇴상태 회원만 출력하도록 데이터 프레임 검색 코드 넣어야함
        #####

        self.labeltitle = Label(self.win,text="탈퇴 회원 조회",font=("맑은고딕", 12,"bold")).place(x=30,y=10)

        a = ["이름","전화번호"]
        self.Phone_combobox = ttk.Combobox(self.win,values=a,state="readonly")
        self.Phone_combobox.place(x=30,y=50,width=100)
        self.Phone_combobox.set("선택")

        self.tree['columns'] = ("사진","전화번호","이름","이메일")

        self.tree.column("#0",width=0, stretch=NO)
        self.tree.column("사진",anchor=W,width=200,minwidth=120, stretch=NO)
        self.tree.column("전화번호",anchor=W,width=150,minwidth=80, stretch=NO)
        self.tree.column("이름",anchor=W, width=150,minwidth=80, stretch=NO)
        self.tree.column("이메일",anchor=W, width=150)

        self.tree.heading("#0",text="",anchor=W)
        self.tree.heading("사진",text="사진",anchor=W)
        self.tree.heading("전화번호",text="전화번호",anchor=W)
        self.tree.heading("이름",text="이름",anchor=W)
        self.tree.heading("이메일",text="이메일",anchor=W)

        for i in range(len(self.user.index)) :
            self.tree.insert('', 'end', text=i,values=list(self.user.loc[i]))         

    def rent_tree(self) :

        #####
        #이부분에 대여가능권수가 있는 회원만 출력하도록 데이터 프레임 검색 코드 넣어야함
        #####

        self.labeltitle = Label(self.win,text="도서 대여",font=("맑은고딕", 12,"bold")).place(x=30,y=10)

        a = ["이름","전화번호"]
        self.Phone_combobox = ttk.Combobox(self.win,values=a,state="readonly")
        self.Phone_combobox.place(x=30,y=50,width=100)
        self.Phone_combobox.set("선택")

        self.tree['columns'] = ("사진","전화번호","이름","대여가능권수","이메일")

        self.tree.column("#0",width=0, stretch=NO)
        self.tree.column("사진",anchor=W,width=120,minwidth=120, stretch=NO)
        self.tree.column("전화번호",anchor=W,width=120,minwidth=80, stretch=NO)
        self.tree.column("이름",anchor=W, width=80,minwidth=80, stretch=NO)
        self.tree.column("대여가능권수",anchor=W, width=30)
        self.tree.column("이메일",anchor=W, width=120)

        self.tree.heading("#0",text="",anchor=W)
        self.tree.heading("사진",text="사진",anchor=W)
        self.tree.heading("전화번호",text="전화번호",anchor=W)
        self.tree.heading("이름",text="이름",anchor=W)
        self.tree.heading("대여가능권수",text="대여가능권수",anchor=W)
        self.tree.heading("이메일",text="이메일",anchor=W)

        for i in range(len(self.user.index)) :
            self.tree.insert('', 'end', text=i,values=list(self.user.loc[i])) 


    def return_tree(self) :
        
        #####
        #이부분에 대여상태 회원만 출력하도록 데이터 프레임 검색 코드 넣어야함
        #####


        self.labeltitle = Label(self.win,text="도서 반납",font=("맑은고딕", 12,"bold")).place(x=30,y=10)

        a = ["이름","전화번호"]
        self.Phone_combobox = ttk.Combobox(self.win,values=a,state="readonly")
        self.Phone_combobox.place(x=30,y=50,width=100)
        self.Phone_combobox.set("선택")

        self.tree['columns'] = ("사진","전화번호","이름","대여가능권수","이메일")

        self.tree.column("#0",width=0, stretch=NO)
        self.tree.column("사진",anchor=W,width=120,minwidth=120, stretch=NO)
        self.tree.column("전화번호",anchor=W,width=120,minwidth=80, stretch=NO)
        self.tree.column("이름",anchor=W, width=80,minwidth=80, stretch=NO)
        self.tree.column("대여가능권수",anchor=W, width=30)
        self.tree.column("이메일",anchor=W, width=120)

        self.tree.heading("#0",text="",anchor=W)
        self.tree.heading("사진",text="사진",anchor=W)
        self.tree.heading("전화번호",text="전화번호",anchor=W)
        self.tree.heading("이름",text="이름",anchor=W)
        self.tree.heading("대여가능권수",text="대여가능권수",anchor=W)
        self.tree.heading("이메일",text="이메일",anchor=W)

        for i in range(len(self.user.index)) :
            self.tree.insert('', 'end', text=i,values=list(self.user.loc[i])) 


    
aaaa = TREE()

a = aaaa.showTree('탈퇴회원')