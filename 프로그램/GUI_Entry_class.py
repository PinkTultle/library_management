from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
from setuptools import Command
from tkinter import messagebox
from function_BOOK import add_book

### 회원 등록 클래스

class Entry_User():
    win = None
    
    def __init__(self,window,x,y):
        self.win = window

        ###레이블 선언
        self.label_name = Label(window, text = "이름 : ")
        self.label_birth = Label(window, text = "생년월일 : ")
        self.label_gender = Label(window, text = "성별 : ")
        self.label_phone = Label(window, text = "전화번호 : ")
        self.label_email = Label(window, text = "이메일 : ")

        ## 전화번호 하이퍼 문자 
        self.hyper = Label(window, text ="-")
        self.hyper1 = Label(window, text ="-")
        self.hyper.place(x=x+225,y=y+90)
        self.hyper1.place(x=x+300,y=y+90)

        ### 레이블 플레이스
        self.label_name.place(x=x+100,y=y) 
        self.label_birth.place(x=x+100,y=y+30)
        self.label_gender.place(x=x+100,y=y+60)  
        self.label_phone.place(x=x+100,y=y+90)  
        self.label_email.place(x=x+100,y=y+120)  

        self.entry_name = Entry(window)
        self.entry_name.place(x=x+170,y=y,width=200)

        self.entry_birth = Entry(window)
        self.entry_birth.place(x=x+170,y=y+30,width=200)

        self.Men_button = Radiobutton(window,text="남",value=0)
        self.Men_button.place(x=x+170,y=y+70,anchor=W)

        self.Girl_button = Radiobutton(window,text="여",value=1)
        self.Girl_button.place(x=x+220,y=y+70,anchor=W)

        ### 전화번호를 엔트리 3개로 나눠서 받기
        self.entry_phone = Entry(window)
        self.entry_phone.place(x=x+170,y=y+90,width=50)

        self.entry_phone1 = Entry(window)
        self.entry_phone1.place(x=x+245,y=y+90,width=50)

        self.entry_phone2 = Entry(window)
        self.entry_phone2.place(x=x+320,y=y+90,width=50)

        ###
        self.entry_email = Entry(window)
        self.entry_email.place(x=x+170,y=y+120,width=200)

        #기본이미지

        


        ## 이미지 추가 버튼 + 레이블 
        #self.proto_image = PhotoImage(file= "C:\\Users\\user\\OneDrive\\바탕 화면\\personAdd.png")
        ##self.label_image = Label(self.window, image=self.proto_image)
        #self.label_image.place(self.x=self.x-50,y=y)

        self.image_add_button = Button(window, text = "이미지 추가",width =14)
        self.image_add_button.place(x=x-60,y=y+150)

        

        ## 확인버튼 취소버튼
        
        self.check_button = Button(window, text="확인",width =10)
        self.check_button.place(x=x+60,y=y+240)
        self.cancle_button = Button(window,text="취소",width=10)
        self.cancle_button.place(x=x+160,y=y+240)
        
    def add_user(self) : #USER.csv파일에 누적 저장 형식으로 회원 정보를 저장한다.
        user_table = pd.read_csv('csv/USER.csv', encoding= 'utf-8', dtype= str ,skiprows = [0]) #csv파일 
        user_table = user_table.set_index('USER_PHONE', drop= False)

        PHONE = self.entry_phone.get()
        if PHONE in user_table['USER_PHONE'].values :
            messagebox.showinfo("경고", "중복된 전호번호가 이미 존재합니다.")
        else:
            try:
                int(PHONE)
                return
            except:
                messagebox.showinfo("경고", "전화번호는 숫자로만 입력 할 수 있습니다.")


            NAME = input('회원 이름 :').strip()
            if NAME == '':
                print("회원이름 칸은 비울 수 없습니다.")
            else:
                try: 
                    int(NAME)
                    print("회원이름은 숫자로 입력할 수 없습니다.")
                except:
                    return

            BIRTH = input('회원 생년월일 :').strip()
            if BIRTH == '':
                print("생년월일 칸은 비울 수 없습니다.")
            else:
                try: 
                    int(BIRTH)
                    return
                except:
                    print("생년월일은 숫자외에 입력 할 수 없습니다.")

            SEX = input('회원 성별 :').strip()
            if SEX == '':
                print("성별 칸은 비울 수 없습니다.")
            else:
                try: 
                    int(SEX)
                    print("성별은 숫자로 입력할 수 없습니다.")
                except:
                    return

        MAIL = self.entry_email
        IMAGE = input('회원 이미지 :')
        REG_DATE = '2022-06-12'
        OUT_DATE = False
        RENT_CNT = 3

    #여기에 입력시 조건 넣어주면 기본값, 널값, 자료형 걸러서 입력 받을 수 있다.



### 도서 등록 클래스

class Entry_Book():

    
    def __init__(self,window,x,y):
        self.win = window
        self.label_title = Label(window, text = "제목 : ")
        self.label_publish = Label(window, text = "출판사 : ")
        self.label_writer = Label(window, text = "저자 : ")
        self.label_isbn = Label(window, text = "ISBN : ")
        self.label_price = Label(window, text = "가격 : ")

        #관련링크
        self.link = Label(window, text = "관련 링크")
        self.link.place(x=x-60,y=y+185)#170  
        self.entry_link = Entry(window)
        self.entry_link.place(x=x-60,y=y+205,width=420,height=50)

        #책설명
        self.book_info = Label(window, text = "책 설명")
        self.book_info.place(x=x-60,y=y+275)  
        self.entry_book_info = Entry(window)
        self.entry_book_info.place(x=x-60,y=y+295,width=420,height=50)

        self.label_title.place(x=x+100,y=y) 
        self.label_publish.place(x=x+100,y=y+30)
        self.label_writer.place(x=x+100,y=y+60)  
        self.label_isbn.place(x=x+100,y=y+90)  
        self.label_price.place(x=x+100,y=y+120)  
        
        # title_type = StringVar()
        self.entry_title = Entry(window)
        self.entry_title.place(x=x+170,y=y,width=200)

        self.entry_publish = Entry(window)
        self.entry_publish.place(x=x+170,y=y+30,width=200)

        self.entry_writer = Entry(window)
        self.entry_writer.place(x=x+170,y=y+60,width=200)

        self.entry_isbn = Entry(window)
        self.entry_isbn.place(x=x+170,y=y+90,width=200)

        self.entry_price = Entry(window)
        self.entry_price.place(x=x+170,y=y+120,width=200)

        #기본이미지

        


        # 이미지 추가 버튼 + 레이블 
        # self.proto_image = PhotoImage(file= "pic9.gif")
        # self.label_image = Label(self.window, image=self.proto_image)
        # self.label_image.place(self.x=self.x-50,y=y)

        self.image_add_button = Button(window, text = "이미지 추가",width =14)
        self.image_add_button.place(x=x-60,y=y+150)

        self.check_button = Button(window, text="등록",width =10, command=self.add_book)
        self.check_button.place(x=x+60,y=y+355)

        self.cancle_button = Button(window,text="취소",width=10, command=self.exit_book)
        self.cancle_button.place(x=x+160,y=y+355)


        

    def add_book(self): 
        book_table = pd.read_csv('csv/BOOK.csv', encoding= 'utf-8', dtype= str) #csv파일 

        book_table = book_table.set_index('BOOK_ISBN', drop= False)


        try:
            ISBN = self.entry_isbn.get()
            if str(ISBN) in book_table['BOOK_ISBN'].values :
                messagebox.showinfo("경고", "중복된 ISBN이 이미 존재합니다.")
                return
        except:
            messagebox.showinfo("경고", "숫자 이외는 입력할 수 없습니다.")


        TITLE = self.entry_title.get()
        if TITLE == '':
            messagebox.showinfo("경고", "도서명 칸은 비울 수 없습니다.")
            return


        AUTHOR = self.entry_writer.get()
        if AUTHOR == '':
            messagebox.showinfo("경고", "저자 칸은 비울 수 없습니다.")
            return


        PUB = self.entry_publish.get()
        if PUB == '':
            messagebox.showinfo("경고", "출판사 칸은 비울 수 없습니다.")
            return


        try:
            PRICE = int(self.entry_price.get())
        except:
            messagebox.showinfo("경고", "가격을 다시 입력해주세요.")
            return

        LINK = self.entry_link.get()
        IMAGE = 'x'
        DESCRIPTION = self.entry_book_info.get()
        PRE = True


        #현재 위치에 데이터 값을 판별하여 기본값, NULL값등을 설정

        newbook = pd.DataFrame({'BOOK_ISBN' : [ISBN], 'BOOK_TITLE' : [TITLE],'BOOK_AUTHOR' : [AUTHOR],'BOOK_PUB' : [PUB],'BOOK_PRICE' : [PRICE],'BOOK_LINK' : [LINK],
        'BOOK_IMAGE' : [IMAGE],'BOOK_DESCRIPTION' : [DESCRIPTION],'BOOK_PRE' : [PRE]})
        newbook.to_csv('csv/BOOK.csv', mode='a', index = False, header= None)

        messagebox.showinfo("확인", "저장완료")
        self.exit_book()
            ## 확인버튼 취소버튼
        
        
    def exit_book(self):
        self.win.destroy()




    

