from tkinter import *
from tkinter import messagebox
import pandas as pd
from tkinter import ttk
from tkinter.filedialog import askopenfilename
#from GUI_Entry_class import Entry_User,Entry_Book

### 회원 등록 클래스
#"프로그램\csv"

User_CSV = 'csv/USER.csv'

class Add_User ():

   ##생성자
    def __init__(self,x=100,y=10):
        self.window = Tk()
        self.window.geometry("500x300")
        self.window.title("신규 회원 등록")
        self.window.resizable(width = FALSE, height=FALSE)
        #self.df_User_CSV = pd.read_csv(User_CSV,encoding='CP949')
    

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


        ### 엔트리 시작
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
        self.Gender = StringVar(self.window)
        self.Men_button = Radiobutton(self.window,text="남",variable=self.Gender,value='남')
        self.Men_button.place(x=x+170,y=y+70,anchor=W)

        self.Girl_button = Radiobutton(self.window,text="여",variable=self.Gender,value='여')
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
        
        self.check_button = Button(self.window, text="등록",width =10,command=self.Edit_User)
        self.check_button.place(x=x+60,y=y+240)
        self.cancle_button = Button(self.window,text="취소",width=10,command=self.quit)
        self.cancle_button.place(x=x+160,y=y+240)
        self.window.mainloop()
    
    def quit(self) :
        self.window.quit()
        self.window.destroy()
    
   

    
    def Edit_User(self) :
        self.df_User_CSV = pd.read_csv(User_CSV,encoding='CP949')

        self.Name = self.entry_name.get()

        self.F = self.Fbirth_combobox.get()
        self.S = self.Sbirth_combobox.get()
        self.T = self.Tbirth_combobox.get()
        self.Birth = self.F + self.S + self.T

        self.Sex = self.Gender.get()

        self.P = self.Phone_combobox.get()
        self.H = self.entry_phone1.get()
        self.O = self.entry_phone2.get()
        ### 0이 처음으로 시작되어 저장되면 0이 삭제되서 1을 추가하고 나중에 1을 삭제할 예정
        self.Phone = '1'+self.P + self.H + self.O

        self.Email = self.entry_email.get()

        ### 등록 예외처리 ###

        ### 전화번호 중복 처리
        
        

        ### 공백 예외처리
        if self.entry_name.get() == "" :
            messagebox.showerror("이름 에러","이름을 입력해주세요")
            return 0

        if self.Phone in self.df_User_CSV['USER_PHONE']:
            messagebox.showerror('전화번호 중복','전화번호가 중복되었습니다.')
            return 0

        #for i in ignoreDF['USER_PHONE'] :
        #    if i == self.Phone :
        #        messagebox.showerror('전화번호 중복','전화번호가 중복되었습니다.')
        #        return 0

        

        if self.Fbirth_combobox.get() =="선택" :
            messagebox.showerror("생년월일 에러","년도를 선택해주세요")
            return 0
        if self.Gender.get() == "" :
            messagebox.showerror('성별에러','성별을 선택해주세요')
            return 0
        if self.Phone_combobox.get() =="선택" :
            messagebox.showerror("전화번호 에러","지역번호를 선택해주세요")
            return 0
        if  not self.Phone.isdigit() :
            messagebox.showerror("전화번호 에러","숫자만 입력해주세요")
            return 0
        if len(self.H) >= 5 or len(self.O) >= 5:
            messagebox.showerror("전화번호 에러", "전화번호 자리에 숫자를 5개 이상 입력하셨습니다.")
            return 0
        if self.entry_email.get() == "" or len(self.entry_email.get()) > 30 :
            messagebox.showerror('이메일 에러','이메일 형식을 지켜주세요')
            return 0

        #USER_PHONE,USER_NAME,USER_BIRTH,USER_SEX,USER_MAIL,
        # USER_IMAGE,USER_REG_DATE,USER_OUT_DATE,USER_RENT_CNT

        df = pd.DataFrame.from_records([{'USER_PHONE' : str(self.Phone),'USER_NAME' : self.Name,'USER_BIRTH':self.Birth,'USER_SEX':self.Gender,\
            'USER_MAIL':self.Email,'USER_IMAGE':'0','USER_REG_DATE':'0','USER_OUT_DATE':'0','USER_RENT_CNT':'0'}])

        self.question = messagebox.askquestion("등록확인창",self.entry_name.get()+' , '+self.Phone+' 를 등록하겠습니까?')
        if self.question == "yes" :

            self.df_User_CSV = pd.concat([self.df_User_CSV,df])
            self.df_User_CSV = self.df_User_CSV.set_index(self.df_User_CSV['USER_PHONE'])
            self.df_User_CSV.to_csv(User_CSV,index=False,encoding='cp949')
            messagebox.showinfo('등록완료',self.entry_name.get()+' , '+self.Phone+'이 등록되었습니다.')
            self.window.quit()
            self.window.destroy()

        

      

class Add_Book ():


    def __init__(self,x=100,y=10):
        self.window = Tk()
        self.window.geometry("500x400")
        self.window.title("도서 등록")
        self.window.resizable(width = FALSE, height=FALSE)

        #self.book_add = Entry_Book(self.window,x=100, y =10)


        

    

        self.label_title = Label(self.window, text = "제목 : ")
        self.label_publish = Label(self.window, text = "출판사 : ")
        self.label_writer = Label(self.window, text = "저자 : ")
        self.label_isbn = Label(self.window, text = "ISBN : ")
        self.label_price = Label(self.window, text = "가격 : ")

        #관련링크
        self.link = Label(self.window, text = "관련 링크")
        self.link.place(x=x-60,y=y+185)#170  
        self.entry_link = Entry(self.window)
        self.entry_link.place(x=x-60,y=y+205,width=420,height=50)

        #책설명
        self.book_info = Label(self.window, text = "책 설명")
        self.book_info.place(x=x-60,y=y+275)  
        self.entry_book_info = Entry(self.window)
        self.entry_book_info.place(x=x-60,y=y+295,width=420,height=50)

        self.label_title.place(x=x+100,y=y) 
        self.label_publish.place(x=x+100,y=y+30)
        self.label_writer.place(x=x+100,y=y+60)  
        self.label_isbn.place(x=x+100,y=y+90)  
        self.label_price.place(x=x+100,y=y+120)  

        self.entry_title = Entry(self.window)
        self.entry_title.place(x=x+170,y=y,width=200)

        self.entry_publish = Entry(self.window)
        self.entry_publish.place(x=x+170,y=y+30,width=200)

        self.entry_writer = Entry(self.window)
        self.entry_writer.place(x=x+170,y=y+60,width=200)

        self.entry_isbn = Entry(self.window)
        self.entry_isbn.place(x=x+170,y=y+90,width=200)

        self.entry_price = Entry(self.window)
        self.entry_price.place(x=x+170,y=y+120,width=200)

        #기본이미지

        


        ## 이미지 추가 버튼 + 레이블 
        #self.proto_image = PhotoImage(file= "C:\\Users\\user\\OneDrive\\바탕 화면\\personAdd.png")
        ##self.label_image = Label(window, image=self.proto_image)
        #self.label_image.place(x=x-50,y=y)

        self.image_add_button = Button(self.window, text = "이미지 추가",width =14)
        self.image_add_button.place(x=x-60,y=y+150)

        

        ## 확인버튼 취소버튼
    

        self.check_button = Button(self.window, text="등록",width =10)
        self.check_button.place(x=x+60,y=y+355)
        self.cancle_button = Button(self.window,text="취소",width=10,command=self.quit)
        self.cancle_button.place(x=x+160,y=y+355)
        self.window.mainloop()
    
    def quit(self) :
        self.window.quit()
        self.window.destroy()
