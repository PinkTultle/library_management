from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from fileinput import filename
from tkinter.filedialog import*

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

        

        gwak = value.values.tolist()
        gwak = sum(gwak,[])
        

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

        
        self.default_user_image = Image.open(gwak[5]) # 기본이미지
        self.default_user_image = self.default_user_image.resize((110, 140))     # 사진 크기조정
        self.Tk_user_image = ImageTk.PhotoImage(self.default_user_image, master=self.window)   #PIL이미지 Tk의 이미지로 변환
        self.label_user_image = Label(self.window, image=self.Tk_user_image)
        self.label_user_image.place(x=x-62,y=y)

        self.image_add_button = Button(self.window, text = "이미지 추가",width =14, command=self.insert_user_image)
        self.image_add_button.place(x=x-60,y=y+150)

        self.check_button = Button(self.window, text="수정",width =10)
        self.check_button.place(x=x,y=y+240)
        self.check_button = Button(self.window, text="삭제",width =10)
        self.check_button.place(x=x+100,y=y+240)
        self.cancle_button = Button(self.window,text="취소",width=10,command=self.quit)
        self.cancle_button.place(x=x+200,y=y+240)

       

        # 이름 생년월일 성별 전번 이메일 사진
       
        self.entry_name.insert(0,gwak[1])

        self.bb = gwak[2]
        
        self.Fbirth_combobox.set(self.bb[:4])
        self.Sbirth_combobox.set(self.bb[4:6])
        self.Tbirth_combobox.set(self.bb[6:])

        if gwak[3] == "남" :
            self.Men_button.select()
        else :
            self.Girl_button.select()

        self.zz = gwak[0].split('-')

        self.Phone_combobox.set(self.zz[0])
        self.entry_phone1.insert(0,self.zz[1])
        self.entry_phone2.insert(0,self.zz[2])
        self.entry_email.insert(0,gwak[4])
        
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


