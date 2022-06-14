import pandas as pd
from datetime import datetime, timedelta

import function_BOOK as BO
import function_USER as US

Day = datetime.now()
RentDay = Day.strftime('%Y-%m-%d')
ReturnDay = (Day + timedelta(weeks= 2)).strftime('%Y-%m-%d')

rent_field = ['RENT_ISBN', 'RENT_USER', 'RENTAL_DATA','RETURN_DATA','RETURN_VALUE']
#필드 명

rent_table = pd.read_csv('csv/RENT.csv', names = rent_field ,encoding= 'utf-8', dtype= str,header= None) #csv파일 

rent_table = rent_table.set_index('RENT_ISBN', drop= False)


def rant() :
    stbook = input("대여할 도서 ISBN입력\n>>")

    if stbook not in BO.book_table.index :
        print('존재하지 않는 책입니다.')
        return
    elif stbook in rent_table.index :
        print('현재 대여중인 책입니다.')
        return

    stuser = input('당신의 전화번호를 입력해 주세요\n>>')

    if stuser not in US.user_table.index :
        print('존재하지 않는 회원입니다.')
        return
    elif US.user_table['USER_RENT_CNT'].all() == False :
        print('대여가능 도서수를 채웠습니다.')
        return

    new_rent = pd.DataFrame({'RENT_ISBN' : [stbook], 'RENT_USER' : [stuser],'RENTAL_DATA' : [RentDay],
    'RETURN_DATA' : [ReturnDay],'RETURN_VALUE' : [BO.book_table.loc[stbook,'BOOK_PRE']]})  

    US.user_table = US.user_table.astype({'USER_RENT_CNT':int})
    US.user_table.loc[stuser,'USER_RENT_CNT'] -= 1 
    US.user_table.to_csv('csv/UESR.csv', mode = 'w' ,index= False, header= True)

    BO.book_table.loc[stbook,'BOOK_PRE'] = False
    BO.book_table.to_csv('csv/BOOK.csv', mode= 'w', index= False, header= None)

    new_rent.to_csv('csv/RENT.csv', mode='a', index = False, header= None) 

    print('대여를 완료하였습니다.')





def Return() :
    rent_table = pd.read_csv('csv/RENT.csv', encoding= 'utf-8', dtype= str)
    rent_table = rent_table.set_index('RENT_ISBN', drop=False)
    del_rentuser = input("반납할 회원의 전화번호를 입력하시오.\n>>")
    if del_rentuser not in rent_table['RENT_USER'].values :
        print("대여한 도서가 없습니다.")
        return
    del_rent = input("반납할 도서의 ISBN을 입력하시오.\n>>")
    if del_rent in rent_table['RENT_ISBN'].values :
            abc = str(int(rent_table[rent_table['RENT_ISBN'] == del_rent]['RENT_ISBN']))
            rent_table.drop(index=abc, axis=0, inplace=True)
            rent_table.to_csv('csv/RENT.csv', index=False, encoding='utf-8',header= True)
    else:
        print("대여 하지 않는 책입니다.")
        return

    US.user_table = US.user_table.astype({'USER_RENT_CNT':int})
    US.user_table.loc[del_rentuser,'USER_RENT_CNT'] += 1 
    US.user_table.to_csv('csv/UESR.csv', mode = 'w' ,index= False, header= True)

    BO.book_table.loc[del_rent,'BOOK_PRE'] = True
    BO.book_table.to_csv('csv/BOOK.csv', mode= 'w', index= False, header= None)

    print('반납을 완료하였습니다.')


def reset_rent_csv() : #csv파일을 초기화 시키는 함수 
    rsrent = pd.DataFrame(columns= rent_field)
    rsrent.to_csv('csv/RENT.csv', mode='w', index = False, header= None)




#rant()

#Return()

#reset_rent_csv()