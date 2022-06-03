from tkinter import *
from tkinter.filedialog import askopenfilename

### 회원 등록 클래스

class Entry_User():

    
    def __init__(self,window,x,y):

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
        ##self.label_image = Label(window, image=self.proto_image)
        #self.label_image.place(x=x-50,y=y)

        self.image_add_button = Button(window, text = "이미지 추가",width =14)
        self.image_add_button.place(x=x-60,y=y+150)

        

        ## 확인버튼 취소버튼
        
        self.check_button = Button(window, text="확인",width =10)
        self.check_button.place(x=x+60,y=y+240)
        self.cancle_button = Button(window,text="취소",width=10)
        self.cancle_button.place(x=x+160,y=y+240)
        

### 도서 등록 클래스

class Entry_Book():

    
    def __init__(self,window,x,y):

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

        self.entry_title = Entry(window)
        self.entry_title.place(x=x+170,y=y,width=200)

        self.entry_publish = Entry(window)
        self.entry_publish.place(x=x+170,y=y+30,width=200)

        self.entry_writerh = Entry(window)
        self.entry_writer.place(x=x+170,y=y+60,width=200)

        self.entry_isbn = Entry(window)
        self.entry_isbn.place(x=x+170,y=y+90,width=200)

        self.entry_price = Entry(window)
        self.entry_price.place(x=x+170,y=y+120,width=200)

        #기본이미지

        


        ## 이미지 추가 버튼 + 레이블 
        #self.proto_image = PhotoImage(file= "C:\\Users\\user\\OneDrive\\바탕 화면\\personAdd.png")
        ##self.label_image = Label(window, image=self.proto_image)
        #self.label_image.place(x=x-50,y=y)

        self.image_add_button = Button(window, text = "이미지 추가",width =14)
        self.image_add_button.place(x=x-60,y=y+150)

        

        ## 확인버튼 취소버튼
        
        self.check_button = Button(window, text="등록",width =10)
        self.check_button.place(x=x+60,y=y+355)
        self.cancle_button = Button(window,text="취소",width=10)
        self.cancle_button.place(x=x+160,y=y+355)
        


