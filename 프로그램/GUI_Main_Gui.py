from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from function_Add_class import Add_Book, Add_User
import pandas as pd
from function_Edit import *
import csv
from PIL import Image, ImageTk
#from GUI_Entry_class import Entry_User

User_CSV = 'csv/USER.csv'

class MainStart() :
    def __init__(self) :

        self.win = Tk()
        self.labeltitle = Label(self.win,text="회원 조회",font=("맑은고딕", 12))

        self.win.geometry("800x450")
        self.win.title("도서 관리 프로그램")
        self.win.resizable(width =FALSE, height = FALSE)

        
        self.startlabel = Label(self.win, text = "도서 관리 프로그램",font = ("궁서체",50))
        self.startlabel.place(x = 100, y = 150)

        #각각의 csv파일 불러와서 데이터 프레임에 산입후 출력에 맞게 변경
        self.book = pd.read_csv('csv/BOOK.csv', encoding= 'utf-8', dtype= str)
        self.user = pd.read_csv('csv/USER.csv', encoding= 'utf-8', dtype= str)
        self.rent = pd.read_csv('csv/RENT.csv', encoding= 'utf-8', dtype= str)

        self.rent = self.rent[['RENT_ISBN','RENT_USER','RENTAL_DATA','RETURN_DATA','RETURN_VALUE']]
        self.book = self.book[['BOOK_IMAGE','BOOK_ISBN','BOOK_TITLE','BOOK_AUTHOR','BOOK_PRICE','BOOK_LINK']]
        self.user = self.user[['USER_IMAGE','USER_PHONE','USER_NAME','USER_RENT_CNT','USER_MAIL']]
        #불러온 csv파일의 데이터중 출력할 데이터 열을 추출하여 새로운 데이터 프레임 생성


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
        
        self.labeltitle = Label(self.win,text="도서 조회",font=("맑은고딕", 12,"bold")).place(x=30,y=10)
       
        self.tree = ttk.Treeview(self.win)

        self.book = pd.read_csv('csv/BOOK.csv', encoding= 'utf-8', dtype= str)
        self.book = self.book[['BOOK_ISBN','BOOK_TITLE','BOOK_AUTHOR','BOOK_PRICE','BOOK_LINK']]
        

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
        self.tree['columns'] = ("ISBN","도서명","저자","가격","URL")

        self.tree.column("#0",width=0, stretch=NO)
        self.tree.column("ISBN",anchor=W,width=100,minwidth=80, stretch=NO)
        self.tree.column("도서명",anchor=W, width=100,minwidth=80, stretch=NO)
        self.tree.column("저자",anchor=W, width=80)
        self.tree.column("가격",anchor=W, width=80)
        self.tree.column("URL",anchor=W, width=80)

        self.tree.heading("#0",text="",anchor=W)
        self.tree.heading("ISBN",text="ISBN",anchor=W)
        self.tree.heading("도서명",text="도서명",anchor=W)
        self.tree.heading("저자",text="저자",anchor=W)
        self.tree.heading("가격",text="가격",anchor=W)
        self.tree.heading("URL",text="URL",anchor=W)


        for i in range(len(self.book.index)) :
            self.tree.insert('', 'end', text=i,values=list(self.book.loc[i])) 
        

        self.tree.place(x=30,y=100,width=740,height=300)

        
        

        

    ##################
    ### 회원 조회 함수
    ##################
    def Search_User (self) :
        self.labeltitle = Label(self.win,text="회원 조회",font=("맑은고딕", 12,"bold")).place(x=30,y=10)
        
        self.tree = ttk.Treeview(self.win)
        ###
        self.user = pd.read_csv('csv/USER.csv', encoding= 'utf-8', dtype= str)
        self.user = self.user[['USER_PHONE','USER_NAME','USER_SEX','USER_RENT_CNT','USER_MAIL']]


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
        self.tree['columns'] = ("전화번호","이름","성별","대여가능권수","이메일")

        self.tree.column("#0",width=0, stretch=NO)
        self.tree.column("전화번호",anchor=W,width=120,minwidth=80, stretch=NO)
        self.tree.column("이름",anchor=W, width=60,minwidth=80, stretch=NO)
        self.tree.column("성별",anchor=W,width=150,minwidth=150, stretch=NO)
        self.tree.column("대여가능권수",anchor=W, width=30)
        self.tree.column("이메일",anchor=W, width=120)

        self.tree.heading("#0",text="",anchor=W)
        self.tree.heading("전화번호",text="전화번호",anchor=W)
        self.tree.heading("이름",text="이름",anchor=W)
        self.tree.heading("성별",text="성별",anchor=W)
        self.tree.heading("대여가능권수",text="대여가능권수",anchor=W)
        self.tree.heading("이메일",text="이메일",anchor=W)

        for i in range(len(self.user.index)) :
            self.tree.insert('', 'end', text=i,values=list(self.user.loc[i]))

        self.btn = Button(self.win,text="선택",command=self.Edit_func)
        self.btn.place(x=650,y=420) 
        self.tree.bind('<ButtonRelease-1>',self.click_event)
        self.tree.place(x=30,y=100,width=740,height=300)

    def click_event(self,event):
            
        double_click = self.tree.focus()
        self.getTable = self.tree.item(double_click).get('values')
        
    def Edit_func(self,x=100,y=10):
        self.window = Tk()
        self.window.geometry("500x300")
        self.window.title("회원조회")
        self.window.resizable(width = FALSE, height=FALSE)
        self.df_User_CSV = pd.read_csv(User_CSV,encoding='utf-8')


        self.label_name = Label(self.window, text = "이름 : ")
        self.label_birth = Label(self.window, text = "생년월일 : ")
        self.label_gender = Label(self.window, text = "성별 : ")
        self.label_phone = Label(self.window, text = "전화번호 : ")
        self.label_email = Label(self.window, text = "이메일 : ")

        self.hyper = Label(self.window, text ="-")
        self.hyper1 = Label(self.window, text ="-")
        self.hyper.place(x=x+225,y=y+90)
        self.hyper1.place(x=x+300,y=y+90)

        self.label_name.place(x=x+100,y=y) 
        self.label_birth.place(x=x+100,y=y+30)
        self.label_gender.place(x=x+100,y=y+60)  
        self.label_phone.place(x=x+100,y=y+90)  
        self.label_email.place(x=x+100,y=y+120)  

        


        ### 엔트리 시작
        self.entry_name = Entry(self.window ,state="disable")
        self.entry_name.place(x=x+170,y=y,width=200)
        
        F_list = list(range(1950,2022))


        self.Fbirth_combobox = ttk.Combobox(self.window,state ="readonly")
        self.Fbirth_combobox.place(x=x+170,y=y+30,width=60)
        

        S_list = ['01','02','03','04','05','06','07','08','09','10','11','12']

        self.Sbirth_combobox = ttk.Combobox(self.window,state ="readonly")
        self.Sbirth_combobox.place(x=x+255,y=y+30,width=45)
        

        T_list = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23',\
            '24','25','26','27','28','29','30','31']

        self.Tbirth_combobox = ttk.Combobox(self.window,state ="readonly")
        self.Tbirth_combobox.place(x=x+325,y=y+30,width=45)
        


        self.Gender = StringVar(self.window)
        self.Men_button = Radiobutton(self.window,text="남",variable=self.Gender,value='남')
        self.Men_button.place(x=x+170,y=y+70,anchor=W)

        self.Girl_button = Radiobutton(self.window,text="여",variable=self.Gender,value='여')
        self.Girl_button.place(x=x+220,y=y+70,anchor=W)
        a = ["010","016","011"]
        self.Phone_combobox = ttk.Combobox(self.window,state="readonly")
        self.Phone_combobox.place(x=x+170,y=y+90,width=50)

        self.entry_phone1 = Entry(self.window, state="disable")
        self.entry_phone1.place(x=x+245,y=y+90,width=50)

        self.entry_phone2 = Entry(self.window, state="disable")
        self.entry_phone2.place(x=x+320,y=y+90,width=50)

        self.entry_email = Entry(self.window, state="disable")
        self.entry_email.place(x=x+170,y=y+120,width=200)

        self.Image = self.getTable[5]
        self.default_user_image = Image.open(self.Image) # 기본이미지
        self.default_user_image = self.default_user_image.resize((110, 140))     # 사진 크기조정
        self.Tk_user_image = ImageTk.PhotoImage(self.default_user_image, master=self.window)   #PIL이미지 Tk의 이미지로 변환
        self.label_user_image = Label(self.window, image=self.Tk_user_image)
        self.label_user_image.place(x=x-62,y=y)

        # 이름 생년월일 성별 전번 이메일 사진
        self.entry_name = self.getTable[1]
        self.bb = self.getTable[2]
        self.Fbirth_combobox.set(self.bb[:4])
        self.Sbirth_combobox.set(self.bb[5:7])
        self.Tbirth_combobox.set(self.bb[6:])
        self.zz = self.getTable[0]
        self.zz.split('-')
        self.Phone_combobox.set(self.zz[0])
        self.entry_phone1.insert(0,self.zz[1])
        self.entry_phone2.insert(0,self.zz[2])
        self.entry_email.insert(0,self.getTable[4])
        

        self.window.mainloop()
            

        

    ##################
    ### 도서 대여 함수
    ##################
    def Book_Rent (self) :
        
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