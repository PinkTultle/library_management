from tkinter import *
from tkinter import messagebox
import pandas as pd
#from Entry_class import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
### 회원 등록 클래스

class Add_User ():

    ##생성자
    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x300")
        self.window.title("신규 회원 등록")
        self.window.resizable(width = FALSE, height=FALSE)
        
        #self.user_add = Entry_User(self.window,x=100, y =10)
        

        self.window.mainloop()
    def Entry_User(self,x=100,y=10):

        ###레이블 선언
        self.label_name = Label(self.window, text = "이름 : ")
        self.label_birth = Label(self.window, text = "생년월일 : ")
        self.label_gender = Label(self.window, text = "성별 : ")
        self.label_phone = Label(self.window, text = "전화번호 : ")
        self.label_email = Label(self.window, text = "이메일 : ")

        ## 전화번호 하이퍼 문자 
        self.hyper = Label(self.window, text ="-")
        self.hyper1 = Label(self.window, text ="-")
        self.hyper.place(x=x+225,y=y+90)
        self.hyper1.place(x=x+300,y=y+90)

        ### 레이블 플레이스
        self.label_name.place(x=x+100,y=y) 
        self.label_birth.place(x=x+100,y=y+30)
        self.label_gender.place(x=x+100,y=y+60)  
        self.label_phone.place(x=x+100,y=y+90)  
        self.label_email.place(x=x+100,y=y+120)  

        self.entry_name = Entry(self.window)
        self.entry_name.place(x=x+170,y=y,width=200)
        
        ### 생년월일 콤보박스 

        F_list = []
        for i in range(1950,2022) :
            m = 0
            F_list.append(i)
            m+=1

        self.Fbirth_combobox = ttk.Combobox(self.window,values= F_list,state ="readonly")
        self.Fbirth_combobox.place(x=x+170,y=y+30,width=60)
        self.Fbirth_combobox.set('선택')

        S_list = ['01','02','03','04','05','06','07','08','09','10','11','12']

        self.Sbirth_combobox = ttk.Combobox(self.window,values=S_list,state ="readonly")
        self.Sbirth_combobox.place(x=x+255,y=y+30,width=45)
        self.Sbirth_combobox.set('01')

        T_list = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23',\
            '24','25','26','27','28','29','30','31']

        self.Tbirth_combobox = ttk.Combobox(self.window,values=T_list,state ="readonly")
        self.Tbirth_combobox.place(x=x+325,y=y+30,width=45)
        self.Tbirth_combobox.set('01')
        ##########################################

        self.Men_button = Radiobutton(self.window,text="남",value=0)
        self.Men_button.place(x=x+170,y=y+70,anchor=W)

        self.Girl_button = Radiobutton(self.window,text="여",value=1)
        self.Girl_button.place(x=x+220,y=y+70,anchor=W)

        ### 전화번호를 엔트리 3개로 나눠서 받기
        a = ["010","016","011"]
        self.Phone_combobox = ttk.Combobox(self.window,values=a,state="readonly")
        self.Phone_combobox.place(x=x+170,y=y+90,width=50)
        self.Phone_combobox.set("선택")

        self.entry_phone1 = Entry(self.window)
        self.entry_phone1.place(x=x+245,y=y+90,width=50)

        self.entry_phone2 = Entry(self.window)
        self.entry_phone2.place(x=x+320,y=y+90,width=50)

        ###
        self.entry_email = Entry(self.window)
        self.entry_email.place(x=x+170,y=y+120,width=200)

        #기본이미지

        


        ## 이미지 추가 버튼 + 레이블 
        #self.proto_image = PhotoImage(file= "C:\\Users\\user\\OneDrive\\바탕 화면\\personAdd.png")
        ##self.label_image = Label(window, image=self.proto_image)
        #self.label_image.place(x=x-50,y=y)

        self.image_add_button = Button(self.window, text = "이미지 추가",width =14)
        self.image_add_button.place(x=x-60,y=y+150)

        

        ## 확인버튼 취소버튼
        
        self.check_button = Button(self.window, text="확인",width =10)
        self.check_button.place(x=x+60,y=y+240)
        self.cancle_button = Button(self.window,text="취소",width=10)
        self.cancle_button.place(x=x+160,y=y+240)
      

class Add_Book ():


    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x400")
        self.window.title("도서 등록")
        self.window.resizable(width = FALSE, height=FALSE)

        #self.book_add = Entry_Book(self.window,x=100, y =10)


        self.window.mainloop()

    def Entry_Book(self,window,x,y):

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

        self.entry_writer = Entry(window)
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
        def quit(self):
            window.quit()
            window.destory()

        self.check_button = Button(window, text="등록",width =10)
        self.check_button.place(x=x+60,y=y+355)
        self.cancle_button = Button(window,text="취소",width=10,command=quit)
        self.cancle_button.place(x=x+160,y=y+355)
