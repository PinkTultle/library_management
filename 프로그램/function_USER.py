import pandas as pd
from datetime import datetime, timedelta

nowDay = datetime.today().strftime('%Y-%m-%d')

user_field = ['USER_PHONE', 'USER_NAME', 'USER_BIRTH','USER_SEX','USER_MAIL','USER_IMAGE',
'USER_REG_DATE', 'USER_OUT_DATE', 'USER_RENT_CNT']
#필드 명

user_table = pd.read_csv('csv/USER.csv', names = user_field ,encoding= 'utf-8', dtype= str ,skiprows = [0]) #csv파일 

user_table = user_table.set_index('USER_PHONE', drop= False)

def add_user() : #USER.csv파일에 누적 저장 형식으로 회원 정보를 저장한다.
    while 1:
        PHONE = input('회원 전화번호 :')
        if PHONE in user_table['USER_PHONE'].values :
            print("중복된 전화번호가 이미 존재합니다.")
        else:
            try:
                int(PHONE)
                break
            except:
                print("전화번호는 숫자로만 입력 할 수 있습니다.")


    while 1:
            NAME = input('회원 이름 :').strip()
            if NAME == '':
                print("회원이름 칸은 비울 수 없습니다.")
            else:
                try: 
                    int(NAME)
                    print("회원이름은 숫자로 입력할 수 없습니다.")
                except:
                    break

    while 1:
            BIRTH = input('회원 생년월일 :').strip()
            if BIRTH == '':
                print("생년월일 칸은 비울 수 없습니다.")
            else:
                try: 
                    int(BIRTH)
                    break
                except:
                    print("생년월일은 숫자외에 입력 할 수 없습니다.")

    while 1:
            SEX = input('회원 성별 :').strip()
            if SEX == '':
                print("성별 칸은 비울 수 없습니다.")
            else:
                try: 
                    int(SEX)
                    print("성별은 숫자로 입력할 수 없습니다.")
                except:
                    break

    MAIL = input('회원 메일 :')
    IMAGE = input('회원 이미지 :')
    REG_DATE = nowDay
    OUT_DATE = False
    RENT_CNT = 3

    #여기에 입력시 조건 넣어주면 기본값, 널값, 자료형 걸러서 입력 받을 수 있다.

    newuser = pd.DataFrame({'USER_PHONE' : [PHONE], 'USER_NAME' : [NAME],'USER_BIRTH' : [BIRTH],'USER_SEX' : [SEX],
    'USER_MAIL' : [MAIL],'USER_IMAGE' : [IMAGE],'USER_REG_DATE' : [REG_DATE],'USER_OUT_DATE' : [OUT_DATE], 'USER_RENT_CNT' : [RENT_CNT]})
    newuser.to_csv('csv/USER.csv', mode='a', index = False, header= None)
    
    HA = pd.read_csv('csv/USER.csv', names = user_field ,encoding= 'utf-8', dtype= str) #csv파일
    print(HA)

def reset_user_csv() : #csv파일을 초기화 시키는 함수 
    rsuser = pd.DataFrame(columns= user_field)
    rsuser.to_csv('csv/USER.csv', mode='w', index = False, header= True)


def search_user() : # csv파일안에서 원하는 값을 찾는다.
    property = input("1 : 전화번호 \n2 : 이름\n>>")
    keyword = input("키워드를 입력하시오. \n>>")

    if property == '1': # 9번 라인에서 인덱스를 전화번호열로 설정했기에 전화번호로 검색시 .index를 사용하였다.
        search = user_table[user_table.index == keyword]
    elif property == '2' :
        search = user_table[user_table['USER_NAME'] == keyword]

    if search.empty:
        print("검색 결과가 없습니다.")
    else :
        print(search)


def edit_user() :
    user_table = pd.read_csv('csv/USER.csv', names = user_field ,encoding= 'utf-8', dtype= str)
    # user_table = user_table.set_index('USER_PHONE', drop=False)
    st_user = input("수정할 회원의 이름을 입력하시오.\n>>")
    print(user_table)
    if st_user in user_table['USER_NAME'].values :
        what_user_edit = int(input("수정할 목록의 번호를 입력하세요 \n1: 회원 전화번호 \n2: 회원 이름 \n3: 회원 생년월일\
             \n4: 회원 성별 \n5: 회원 메일 \n6: 회원 이미지 \n7: 회원 가입일 \n8: 회월 탈퇴일 \n9: 대여가능 도서수 \n>> "))
        if what_user_edit == 1:
            colums = 'USER_PHONE'
        elif what_user_edit == 2:
            colums = 'USER_NAME'
        elif what_user_edit == 3:
            colums = 'USER_BIRTH'
        elif what_user_edit == 4:
            colums = 'USER_SEX'
        elif what_user_edit == 5:
            colums = 'USER_MAIL'
        elif what_user_edit == 6:
            colums = 'USER_IMAGE'
        elif what_user_edit == 7:
            colums = 'USER_REG_DATE'
        elif what_user_edit == 8:
            colums = 'USER_OUT_DATE'
        elif what_user_edit == 9:
            colums = 'USER_RENT_CNT'
        elif what_user_edit < 1 or what_user_edit > 9:
            print("1~9 사이를 입력해주세요.")

        edit_user_info(st_user,colums)                 
    else:
        print("저장되지 않은 회원입니다. 확인 후 다시 입력하세요.")
        
def edit_user_info(user1, what_user_edit):
    user_table = pd.read_csv('csv/USER.csv', encoding= 'utf-8', dtype= str)
    user_table = user_table.set_index('USER_PHONE', drop=False)
    user_abc='0'+str(int(user_table[user_table['USER_NAME'] == user1]['USER_PHONE'])) #int 에서 str 으로 바꾸는변환하는 과정에서 0이 생략됨
    print(user_abc)
    # print(user_table[user_table['USER_NAME'] == book]['USER_PHONE'])
    new_user_values = input("새로운 값을 입력: ")
    if what_user_edit == 'USER_PHONE':
        if new_user_values in user_table['USER_PHONE'].values :
            print("중복된 전화번호가 이미 존재합니다.")
        else:
            try:
                int(new_user_values)
                user_table[what_user_edit].loc[user_abc] = new_user_values
            except:
                print("전화번호는 숫자로 입력하세요")

    elif what_user_edit == 'USER_NAME':
        if new_user_values.strip() == '':
            print("회원명 칸을 비울 수 없습니다. ")
        else:
            try:
                int(new_user_values)
                print("회원명은 숫자로 입력하실 수 없습니다.")
            except:    
                user_table[what_user_edit].loc[user_abc] = new_user_values
    
    elif what_user_edit == 'USER_BIRTH':
        if new_user_values.strip() == '':
            print("생년월일 칸은 비울 수 없습니다. ")
        else:
            try:
                int(new_user_values)
                user_table[what_user_edit].loc[user_abc] = new_user_values 
            except:    
                print("생년월일은 숫자만 입력하실 수 있습니다.")    
    
    elif what_user_edit == 'USER_SEX':
        if new_user_values.strip() == '':
            print("성별 칸은 비울 수 없습니다.")
        else:
            try: 
                int(new_user_values)
                print("성별은 숫자로 입력할 수 없습니다.")
            except:
                user_table[what_user_edit].loc[user_abc] = new_user_values
    else:
        user_table[what_user_edit].loc[user_abc] = new_user_values

    user_table.to_csv('csv/USER.csv', index=False, header=True, encoding='utf-8')


def remove_user():
    user_table = pd.read_csv('csv/USER.csv', encoding= 'utf-8', dtype= str)
    user_table = user_table.set_index('USER_PHONE', drop=False)
    del_user = input("삭제할 회원의 이름을 입력하시오.\n>>")
    if del_user in user_table['USER_NAME'].values :
            user_abc = '0'+str(int(user_table[user_table['USER_NAME'] == del_user]['USER_PHONE']))
            user_table.drop(index=user_abc, axis=0, inplace=True)
            user_table.to_csv('csv/USER.csv', index=False, header=True, encoding='utf-8')
    else:
        print("존재 하지 않는 회원입니다.")






# add_user()
#reset_user_csv()
#search_user()
edit_user()
#edit_user_info()
#remove_user()
