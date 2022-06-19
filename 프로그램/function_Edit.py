from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
#회원조회 회원수정 회원탈퇴
#########

class User_Info() :

    def __init__(self,x=100,y=10):
        self.window = Tk()
        self.window.geometry("500x300")
        self.window.title("회원조회")
        self.window.resizable(width = FALSE, height=FALSE)

        # 이름 생년월일 성별 전번 이메일 사진

        self.name = StringVar()
        self.information = StringVar()
        self.department = StringVar()
        self.certifi = StringVar()
        self.toeic = StringVar()

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

        self.name = StringVar()
        self.Fbirth = StringVar()
        self.Fbirth = StringVar()
        self.Fbirth = StringVar()
        self.male = StringVar()
        self.P1 = StringVar()
        self.H1 = StringVar()
        self.O1 = StringVar()
        self.email = StringVar()

        ### 엔트리 시작
        self.entry_name = Entry(self.window,textvariable=self.name ,state="disable")
        self.entry_name.place(x=x+170,y=y,width=200)
        
        F_list = list(range(1950,2022))


        self.Fbirth_combobox = ttk.Combobox(self.window,values= F_list,state ="readonly")
        self.Fbirth_combobox.place(x=x+170,y=y+30,width=60)
        self.Fbirth_combobox.set('선택')

        S_list = list(range(1,13))

        self.Sbirth_combobox = ttk.Combobox(self.window,values=S_list,state ="readonly")
        self.Sbirth_combobox.place(x=x+255,y=y+30,width=45)
        self.Sbirth_combobox.set('01')

        T_list = list(range(1,32))

        self.Tbirth_combobox = ttk.Combobox(self.window,values=T_list,state ="readonly")
        self.Tbirth_combobox.place(x=x+325,y=y+30,width=45)
        self.Tbirth_combobox.set('01')


        self.Gender = StringVar(self.window)
        self.Men_button = Radiobutton(self.window,text="남",variable=self.Gender,value='남')
        self.Men_button.place(x=x+170,y=y+70,anchor=W)

        self.Girl_button = Radiobutton(self.window,text="여",variable=self.Gender,value='여')
        self.Girl_button.place(x=x+220,y=y+70,anchor=W)

        self.Phone_combobox = Entry(self.window,textvariable=self.P1, state="disable")
        self.Phone_combobox.place(x=x+170,y=y+90,width=50)

        self.entry_phone1 = Entry(self.window,textvariable=self.H1, state="disable")
        self.entry_phone1.place(x=x+245,y=y+90,width=50)

        self.entry_phone2 = Entry(self.window,textvariable=self.O1, state="disable")
        self.entry_phone2.place(x=x+320,y=y+90,width=50)

        self.entry_email = Entry(self.window,textvariable=self.email, state="disable")
        self.entry_email.place(x=x+170,y=y+120,width=200)

        self.default_user_image = Image.open("IMAGE\default_user.gif") # 기본이미지
        self.default_user_image = self.default_user_image.resize((110, 140))     # 사진 크기조정
        self.Tk_user_image = ImageTk.PhotoImage(self.default_user_image, master=self.window)   #PIL이미지 Tk의 이미지로 변환
        self.label_user_image = Label(self.window, image=self.Tk_user_image)
        self.label_user_image.place(x=x-62,y=y)







        '''def click_item(event):
            Job_List = []
            selectedItem = JobTree.focus()
            getValue = JobTree.item(selectedItem).get(
                'values')  # 딕셔너리의 값만 가져오기
            Job_List = JobEditSystem.JobLoad(getValue[0])
            name.set(Job_List[0])
            information.set(Job_List[1])
            certifi.set(Job_List[2])
            toeic.set(Job_List[3])
            department.set(Job_List[4])
            wage.set(Job_List[5])
            prosp.set(Job_List[6])
            equality.set(Job_List[7])
            view.set(Job_List[8])
            sex.set(Job_List[9])
            link.set(Job_List[10])

        JobTree.bind('<ButtonRelease-1>', click_item)'''

