from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from fileinput import filename
from tkinter.filedialog import*
from function_Add_class import *
from matplotlib.pyplot import text
import pandas as pd
from PIL import Image, ImageTk
User_CSV = 'csv/USER.csv'

class Show_info:

    def __init__(self) -> None:
        pass

    def show_user(self,value,x=100,y=10) :
        
        self.window = Tk()
        self.window.geometry("500x300")
        self.window.title("회원조회")
        self.window.resizable(width = FALSE, height=FALSE)
        self.df_User_CSV = pd.read_csv(User_CSV,encoding='utf-8')

        

        self.gwak = value.values.tolist()
        self.gwak = sum(self.gwak,[])
        

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
        self.entry_name = Entry(self.window )
        self.entry_name.place(x=x+170,y=y,width=200)
        
        F_list = list(range(1950,2022))


        self.Fbirth_combobox = ttk.Combobox(self.window,values=F_list,state ="readonly")
        self.Fbirth_combobox.place(x=x+170,y=y+30,width=60)
        

        S_list = ['01','02','03','04','05','06','07','08','09','10','11','12']

        self.Sbirth_combobox = ttk.Combobox(self.window,values=S_list,state ="readonly")
        self.Sbirth_combobox.place(x=x+255,y=y+30,width=45)
        

        T_list = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23',\
            '24','25','26','27','28','29','30','31']

        self.Tbirth_combobox = ttk.Combobox(self.window,values=T_list,state ="readonly")
        self.Tbirth_combobox.place(x=x+325,y=y+30,width=45)
        

        
        self.Gender = StringVar(self.window)
        self.Men_button = Radiobutton(self.window,text="남",variable=self.Gender,value='남')
        self.Men_button.place(x=x+170,y=y+70,anchor=W)

        self.Girl_button = Radiobutton(self.window,text="여",variable=self.Gender,value='여')
        self.Girl_button.place(x=x+220,y=y+70,anchor=W)

        a = ["010","016","011"]
        self.Phone_combobox = ttk.Combobox(self.window,values=a,state="readonly")
        self.Phone_combobox.place(x=x+170,y=y+90,width=50)

        self.entry_phone1 = Entry(self.window)
        self.entry_phone1.place(x=x+245,y=y+90,width=50)

        self.entry_phone2 = Entry(self.window)
        self.entry_phone2.place(x=x+320,y=y+90,width=50)

        self.entry_email = Entry(self.window)
        self.entry_email.place(x=x+170,y=y+120,width=200)

        
        self.default_user_image = Image.open(self.gwak[5]) # 기본이미지
        self.default_user_image = self.default_user_image.resize((110, 140))     # 사진 크기조정
        self.Tk_user_image = ImageTk.PhotoImage(self.default_user_image, master=self.window)   #PIL이미지 Tk의 이미지로 변환
        self.label_user_image = Label(self.window, image=self.Tk_user_image)
        self.label_user_image.place(x=x-62,y=y)

        self.image_add_button = Button(self.window, text = "이미지 추가",width =14, command=self.insert_user_image)
        self.image_add_button.place(x=x-60,y=y+150)

        self.check_button = Button(self.window, text="수정",width =10,command=self.edit_user)
        self.check_button.place(x=x,y=y+240)
        self.check_button = Button(self.window, text="삭제",width =10)
        self.check_button.place(x=x+100,y=y+240)
        self.cancle_button = Button(self.window,text="취소",width=10,command=self.quit)
        self.cancle_button.place(x=x+200,y=y+240)

       

        # 이름 생년월일 성별 전번 이메일 사진
       
        self.entry_name.insert(0,self.gwak[1])

        self.bb = self.gwak[2]
        
        self.Fbirth_combobox.set(self.bb[:4])
        self.Sbirth_combobox.set(self.bb[4:6])
        self.Tbirth_combobox.set(self.bb[6:])

        if self.gwak[3] == "남" :
            self.Men_button.select()
        else :
            self.Girl_button.select()

        self.zz = self.gwak[0].split('-')

        self.Phone_combobox.set(self.zz[0])
        self.entry_phone1.insert(0,self.zz[1])
        self.entry_phone2.insert(0,self.zz[2])
        self.entry_email.insert(0,self.gwak[4])
        
        self.window.mainloop()

    def insert_user_image (self):       # 이미지 불러오기 함수
        self.userfilename = askopenfilename(parent=self.window, filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
        self.new_user_image = Image.open(self.userfilename)
        self.new_user_image = self.new_user_image.resize((110, 140))
        self.Tk_user_newimage = ImageTk.PhotoImage(self.new_user_image, master=self.window)
        self.label_user_image.config(image=self.Tk_user_newimage)

    def quit(self) :
        self.window.quit()
        self.window.destroy()

    def edit_user(self) :

        df_user = pd.read_csv(User_CSV, encoding='utf-8')
        df_user = df_user.set_index(df_user['USER_PHONE'])
        user_phone = df_user["USER_PHONE"].tolist()

        self.Name = self.entry_name.get()

        self.P = self.Phone_combobox.get()
        self.H = self.entry_phone1.get()
        self.O = self.entry_phone2.get()
        self.Phone = (self.P+'-' + self.H+ '-' + self.O)

        self.F = self.Fbirth_combobox.get()
        self.S = self.Sbirth_combobox.get()
        self.T = self.Tbirth_combobox.get()
        self.Birth = self.F + self.S + self.T

        self.Sex = self.Gender.get()
        self.Email = self.entry_email.get()

        #user_phone = df_user["USER_PHONE"].tolist()
        df_user["USER_PHONE"].loc[self.gwak[0]] = self.Phone
        df_user["USER_NAME"].loc[self.gwak[0]] = self.Name
        df_user["USER_BIRTH"].loc[self.gwak[0]] = self.Birth
        df_user["USER_SEX"].loc[self.gwak[0]] = self.Sex
        df_user["USER_MAIL"].loc[self.gwak[0]] = self.Email
        user_phone.remove(self.gwak[0])

        if self.entry_name.get() == "" :
            messagebox.showerror("이름 에러","이름을 입력해주세요")
            return 0
        if self.Fbirth_combobox.get() =="선택" :
            messagebox.showerror("생년월일 에러","년도를 선택해주세요")
            return 0
        if self.Gender.get() == "" :
            messagebox.showerror('성별에러','성별을 선택해주세요')
            return 0
        if self.Phone_combobox.get() =="선택" :
            messagebox.showerror("전화번호 에러","지역번호를 선택해주세요")
            return 0
        if  not self.H.isdigit() :
            messagebox.showerror("전화번호 에러","숫자만 입력해주세요")
            return 0
        if  not self.O.isdigit() :
            messagebox.showerror("전화번호 에러","숫자만 입력해주세요")
            return 0
        if len(self.entry_phone1.get()) > 5 or len(self.entry_phone2.get()) > 5:
            messagebox.showerror("전화번호 에러", "전화번호 자리에 숫자를 5개 이상 입력하셨습니다.")
            return 0
        if (self.Phone) in user_phone :
            messagebox.showerror('전화번호 중복','전화번호가 중복되었습니다.')
            return 0
        if self.entry_email.get() == "" or len(self.entry_email.get()) > 30 :
            messagebox.showerror('이메일 에러','이메일 형식을 지켜주세요')
            return 0

        try :
            self.new_user_image = Image.open(self.userfilename)
        except :
            self.new_user_image = Image.open(self.gwak[5])
        
        self.new_user_image.save("IMAGE/" + str(self.Phone) + ".gif",'GIF')     # 이미지 저장

        
        df_user["USER_IMAGE"].loc[self.gwak[0]] = "USER_IMAGE/" + str(self.Phone) + ".gif"
        df_user.to_csv(User_CSV, index=False, encoding='utf-8')

        messagebox.showinfo("회원 정보 수정", "회원 정보가 수정되었습니다.")
        self.quit()
     
