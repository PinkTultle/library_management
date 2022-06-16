from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from function_Add_class import Add_Book, Add_User
#from GUI_Entry_class import Entry_User

class MainStart() :
    def __init__(self) :

        self.win = Tk()
        self.labeltitle = Label(self.win,text="회원 조회",font=("맑은고딕", 12))

        self.win.geometry("800x450")
        self.win.title("도서 관리 프로그램")
        self.win.resizable(width =FALSE, height = FALSE)

        
        self.startlabel = Label(self.win, text = "도서 관리 프로그램",font = ("궁서체",50))
        self.startlabel.place(x = 100, y = 150)
        self.photo = PhotoImage(file="프로그램\cat.gif")
        self.startscreen = Label(self.win,image=self.photo)
        self.startscreen.place(width=800,height=450)

        ### 도서 관리 메뉴
        self.mainMenu = Menu(self.win)
        self.win.config(menu = self.mainMenu)

        self.fileMenu1 = Menu(self.mainMenu,tearoff = 0)
        self.mainMenu.add_cascade(label = "도서관리", menu=self.fileMenu1)
        self.fileMenu1.add_command(label ="도서등록",command=Add_Book)
        self.fileMenu1.add_separator()
        self.fileMenu1.add_command(label = "도서조회",command = self.Search_book)


        ### 회원 관리 메뉴


        self.win.config(menu = self.mainMenu)

        self.fileMenu2 = Menu(self.mainMenu,tearoff = 0)
        self.mainMenu.add_cascade(label = "회원관리", menu=self.fileMenu2)
        self.fileMenu2.add_command(label ="회원등록",command=Add_User)
        self.fileMenu2.add_separator()
        self.fileMenu2.add_command(label = "회원조회",command=self.Search_User)
        self.fileMenu2.add_separator()
        self.fileMenu2.add_command(label = "탈퇴회원",command=self.Delete_User)


        ### 대여 관리 메뉴

        self.win.config(menu = self.mainMenu)

        self.fileMenu2 = Menu(self.mainMenu,tearoff = 0)
        self.mainMenu.add_cascade(label = "대여관리", menu=self.fileMenu2)
        self.fileMenu2.add_command(label ="도서대여",command=self.Book_Rent)
        self.fileMenu2.add_separator()
        self.fileMenu2.add_command(label = "도서반납",command=self.Book_Return)
        self.win.mainloop()

    ##################
    ### 도서 조회 함수
    ##################
    def Search_book (self) :
        
        self.startscreen.destroy()
        self.labeltitle = Label(self.win,text="도서 조회",font=("맑은고딕", 12,"bold")).place(x=30,y=10)
       
        self.tree = ttk.Treeview(self.win)
        

        ##콤보박스 
        a = ["책 제목","ISBN 명"]
        self.Phone_combobox = ttk.Combobox(self.win,values=a,state="readonly")
        self.Phone_combobox.place(x=30,y=50,width=100)
        self.Phone_combobox.set("선택")

        ## 검색창
        self.search_Entry = Entry(self.win)
        self.search_Entry.place(x=200,y=50,width=350)

        ### 검색 버튼
        self.Spec_Search_button = Button(self.win,text="검색",bg="lightsteelblue")
        self.Spec_Search_button.place(x=650,y=45,width=80,height=30)

        ### 트리뷰 테이블 생성
        self.tree['columns'] = ("사진","ISBN","도서명","저자","가격","URL")

        self.tree.column("#0",width=0, stretch=NO)
        self.tree.column("사진",anchor=W,width=120,minwidth=120, stretch=NO)
        self.tree.column("ISBN",anchor=W,width=80,minwidth=80, stretch=NO)
        self.tree.column("도서명",anchor=W, width=80,minwidth=80, stretch=NO)
        self.tree.column("저자",anchor=W, width=80)
        self.tree.column("가격",anchor=W, width=80)
        self.tree.column("URL",anchor=W, width=80)

        self.tree.heading("#0",text="",anchor=W)
        self.tree.heading("사진",text="사진",anchor=W)
        self.tree.heading("ISBN",text="ISBN",anchor=W)
        self.tree.heading("도서명",text="도서명",anchor=W)
        self.tree.heading("저자",text="저자",anchor=W)
        self.tree.heading("가격",text="가격",anchor=W)
        self.tree.heading("URL",text="URL",anchor=W)
        

        self.tree.place(x=30,y=100,width=740,height=300)

        
        

        

    ##################
    ### 회원 조회 함수
    ##################
    def Search_User (self) :
        self.startscreen.destroy()
        self.labeltitle = Label(self.win,text="회원 조회",font=("맑은고딕", 12,"bold")).place(x=30,y=10)
        
        self.tree = ttk.Treeview(self.win)

        ##콤보박스 
        a = ["이름","전화번호"]
        self.Phone_combobox = ttk.Combobox(self.win,values=a,state="readonly")
        self.Phone_combobox.place(x=30,y=50,width=100)
        self.Phone_combobox.set("선택")

        ## 검색창
        self.search_Entry = Entry(self.win)
        self.search_Entry.place(x=200,y=50,width=350)

        ### 검색 버튼
        self.Spec_Search_button = Button(self.win,text="검색",bg="lightsteelblue")
        self.Spec_Search_button.place(x=650,y=45,width=80,height=30)

        ### 트리뷰 테이블 생성
        self.tree['columns'] = ("회원이름","전화번호","대여권수","성별")

        self.tree.column("#0",width=0, stretch=NO)
        self.tree.column("회원이름",anchor=W,width=120)
        self.tree.column("전화번호",anchor=W,width=80)
        self.tree.column("대여권수",anchor=W, width=80)
        self.tree.column("성별",anchor=W, width=80)
        

        self.tree.heading("#0",text="",anchor=W)
        self.tree.heading("회원이름",text="회원이름",anchor=W)
        self.tree.heading("전화번호",text="전화번호",anchor=W)
        self.tree.heading("대여권수",text="대여권수",anchor=W)
        self.tree.heading("성별",text="성별",anchor=W)
        

        self.tree.place(x=30,y=100,width=740,height=300)

    ##################
    ### 도서 대여 함수
    ##################
    def Book_Rent (self) :
        
        self.startscreen.destroy()
        self.tree = ttk.Treeview(self.win)

        self.labeltitle = Label(self.win,text="도서 대여",font=("맑은고딕", 12,"bold")).place(x=30,y=10)
        ##콤보박스 
        a = ["이름","전화번호"]
        self.Phone_combobox = ttk.Combobox(self.win,values=a,state="readonly")
        self.Phone_combobox.place(x=30,y=50,width=100)
        self.Phone_combobox.set("선택")

        ## 검색창
        self.search_Entry = Entry(self.win)
        self.search_Entry.place(x=200,y=50,width=350)

        ### 검색 버튼
        self.Spec_Search_button = Button(self.win,text="검색",bg="lightsteelblue")
        self.Spec_Search_button.place(x=650,y=45,width=80,height=30)

        ### 트리뷰 테이블 생성
        self.tree['columns'] = ("회원이름","전화번호","대여권수","성별")

        self.tree.column("#0",width=0, stretch=NO)
        self.tree.column("회원이름",anchor=W,width=120)
        self.tree.column("전화번호",anchor=W,width=80)
        self.tree.column("대여권수",anchor=W, width=80)
        self.tree.column("성별",anchor=W, width=80)
        

        self.tree.heading("#0",text="",anchor=W)
        self.tree.heading("회원이름",text="회원이름",anchor=W)
        self.tree.heading("전화번호",text="전화번호",anchor=W)
        self.tree.heading("대여권수",text="대여권수",anchor=W)
        self.tree.heading("성별",text="성별",anchor=W)
        

        self.tree.place(x=30,y=100,width=740,height=300)

    ##################
    ### 도서 반납 함수
    ##################
    def Book_Return (self) :
        self.startscreen.destroy()
        self.tree = ttk.Treeview(self.win)

        
        self.labeltitle = Label(self.win,text="도서 반납",font=("맑은고딕", 12,"bold")).place(x=30,y=10)
        ##콤보박스 
        a = ["이름","전화번호"]
        self.Phone_combobox = ttk.Combobox(self.win,values=a,state="readonly")
        self.Phone_combobox.place(x=30,y=50,width=100)
        self.Phone_combobox.set("선택")

        ## 검색창
        self.search_Entry = Entry(self.win)
        self.search_Entry.place(x=200,y=50,width=350)

        ### 검색 버튼
        self.Spec_Search_button = Button(self.win,text="검색",bg="lightsteelblue")
        self.Spec_Search_button.place(x=650,y=45,width=80,height=30)

        ### 트리뷰 테이블 생성
        self.tree['columns'] = ("회원이름","전화번호","대여권수","성별")

        self.tree.column("#0",width=0, stretch=NO)
        self.tree.column("회원이름",anchor=W,width=120)
        self.tree.column("전화번호",anchor=W,width=80)
        self.tree.column("대여권수",anchor=W, width=80)
        self.tree.column("성별",anchor=W, width=80)
        

        self.tree.heading("#0",text="",anchor=W)
        self.tree.heading("회원이름",text="회원이름",anchor=W)
        self.tree.heading("전화번호",text="전화번호",anchor=W)
        self.tree.heading("대여권수",text="대여권수",anchor=W)
        self.tree.heading("성별",text="성별",anchor=W)
        

        self.tree.place(x=30,y=100,width=740,height=300)

    ##################
    ### 탈퇴 회원 ui
    ##################

    def Delete_User (self) :
        self.startscreen.destroy() 
        self.tree = ttk.Treeview(self.win)

        self.labeltitle = Label(self.win,text="탈퇴 회원",font=("맑은고딕", 12,"bold")).place(x=30,y=10)
        ##콤보박스 
        a = ["이름","전화번호"]
        self.Phone_combobox = ttk.Combobox(self.win,values=a,state="readonly")
        self.Phone_combobox.place(x=30,y=50,width=100)
        self.Phone_combobox.set("선택")

        ## 검색창
        self.search_Entry = Entry(self.win)
        self.search_Entry.place(x=200,y=50,width=350)

        ### 검색 버튼
        self.Spec_Search_button = Button(self.win,text="검색",bg="lightsteelblue")
        self.Spec_Search_button.place(x=650,y=45,width=80,height=30)

        ### 트리뷰 테이블 생성
        self.tree['columns'] = ("탈퇴여부","회원이름","전화번호","대여권수")

        self.tree.column("#0",width=0, stretch=NO)
        self.tree.column("탈퇴여부",anchor=W, width=80)
        self.tree.column("회원이름",anchor=W,width=120)
        self.tree.column("전화번호",anchor=W,width=80)
        self.tree.column("대여권수",anchor=W, width=80)
        
        

        self.tree.heading("#0",text="",anchor=W)
        self.tree.heading("탈퇴여부",text="탈퇴여부",anchor=W)
        self.tree.heading("회원이름",text="회원이름",anchor=W)
        self.tree.heading("전화번호",text="전화번호",anchor=W)
        self.tree.heading("대여권수",text="대여권수",anchor=W)
        
        

        self.tree.place(x=30,y=100,width=740,height=300)




    
       





aaa = MainStart()