from tkinter import *
from tkinter import ttk
import pandas as pd

class treeveiw() :

    def __init__(self) :
        self.win = Tk()

        self.win.geometry("800x450")
        self.win.title("도서 관리 프로그램")
        self.win.resizable(width =FALSE, height = FALSE)

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
                
        a = self.TreeView_Print()   

        self.win.mainloop()



    def TreeView_Print(self) :

        self.book = pd.read_csv('csv/BOOK.csv', encoding= 'utf-8', dtype= str)
        print(self.book)


        self.treelist=[("Tom", 80, 3), ("Bani", 71, 5), ("Boni", 90, 2), ("Dannel", 78, 4), ("Minho", 93, 1)]

        for i in range(len(self.book.index)):
            for j in self.book.columns :
                print(j)
                self.tree.insert('', 'end', text=i, values=self.book, iid=str(i)+"번")

        self.tree = pd.DataFrame()

        #벨류부분에 데이터 프레임 행으로 끊어서 입력
        '''
        # 슴겨진 항목
        top= self.tree.insert('', 'end', text="hidden index", iid="5번")
        top_mid1= self.tree.insert(top, 'end', text="5", values=["Timy", 0, 8], iid="5번-1")
        top_mid2= self.tree.insert(top, 0, text="6", values=["Ann", 35, 7], iid="5번-0")
        top_mid3= self.tree.insert(top, 'end', text="7", values=["Sany", 60, 6], iid="5번-2")
        '''
    def TreeView_Ref() :
        d = 4


aaaa = treeveiw()