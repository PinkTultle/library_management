import pandas as pd

book_field = ['BOOK_ISBN', 'BOOK_TITLE', 'BOOK_AUTHOR','BOOK_PUB','BOOK_PRICE','BOOK_LINK','BOOK_IMAGE', 'BOOK_DESCRIPTION', 'BOOK_PRE']
#필드 명

book_table = pd.read_csv('csv/BOOK.csv', names = book_field ,encoding= 'utf-8', dtype= str) #csv파일 

book_table = book_table.set_index('BOOK_ISBN', drop= False)


def add_book() : 
    ISBN = int(input('도서 ISBN :'))
    TITLE = input('도서 명 :')
    AUTHOR = input('도서 저자 :')
    PUB = input('도서 출판사 :')
    PRICE = input('도서 가격 :')
    LINK = input('도서 관련링크 :')
    IMAGE = input('도서 사진 :')
    DESCRIPTION = input('도서 도서설명 :')
    PRE = True

    #현재 위치에 데이터 값을 판별하여 기본값, NULL값등을 설정

    newbook = pd.DataFrame({'BOOK_ISBN' : [ISBN], 'BOOK_TITLE' : [TITLE],'BOOK_AUTHOR' : [AUTHOR],'BOOK_PUB' : [PUB],'BOOK_PRICE' : [PRICE],'BOOK_LINK' : [LINK],
    'BOOK_IMAGE' : [IMAGE],'BOOK_DESCRIPTION' : [DESCRIPTION],'BOOK_PRE' : [PRE]})
    newbook.to_csv('csv/BOOK.csv', mode='a', index = False, header= None)
    #BOOK.csv파일에 누적 저장 형식으로 도서 값을 저장한다. mode = 'a' >> append

    #정상적으로 저장되었는지 확인을 위한 read_csv와 이후 출력문
    HA = pd.read_csv('csv/BOOK.csv', names = book_field ,encoding= 'utf-8', dtype= str) #csv파일
    print(HA)

def reset_book_csv() : #csv파일을 초기화 시키는 함수 
    rsbook = pd.DataFrame(columns= book_field)
    rsbook.to_csv('csv/BOOK.csv', mode='w', index = False, header= True)


def search_book() : # csv파일안에서 원하는 값을 찾는다.
    property = input("1 : 도서 명 \n2 : 저자\n>>")
    keyword = input("키워드를 입력하시오. \n>>")

    if property == '1':
        search = book_table[book_table['BOOK_TITLE'] == keyword]
    elif property == '2' :
        search = book_table[book_table['BOOK_AUTHOR'] == keyword]

    if search.empty:
        print("검색 결과가 없습니다.")
    else :
        print(search)



def edit_book() :
    book_table = pd.read_csv('csv/BOOK.csv', names = book_field ,encoding= 'utf-8', dtype= str)
    # book_table = book_table.set_index('BOOK_ISBN', drop=False)
    st_book = input("수정할 도서의 이름을 입력하시오.\n>>")
    print(book_table)
    if st_book in book_table['BOOK_TITLE'].values :
        what_edit = int(input("수정할 목록의 번호를 입력하세요 \n1: 도서 ISBM \n2: 도서명 \n3: 도서 저자\
             \n4: 도서 출판사 \n5: 도서가격 \n6: 도서 관련링크 \n7: 도서 사진 \n8: 도서설명 \n9: 도서존재여부 \n>> "))
        if what_edit == 1:
            colums = 'BOOK_ISBN'
        elif what_edit == 2:
            colums = 'BOOK_TITLE'
        elif what_edit == 3:
            colums = 'BOOK_AUTHOR'
        elif what_edit == 4:
            colums = 'BOOK_PUB'
        elif what_edit == 5:
            colums = 'BOOK_PRICE'
        elif what_edit == 6:
            colums = 'BOOK_LINK'
        elif what_edit == 7:
            colums = 'BOOK_IMAGE'
        elif what_edit == 8:
            colums = 'BOOK_DESCRIPTION'
        elif what_edit == 9:
            colums = 'BOOK_PRE'

        edit_info(st_book,colums)                 
    else:
        print("저장되지 않은 책입니다. 확인 후 다시 입력하세요.")
        
def edit_info(book, what_edit):
    book_table = pd.read_csv('csv/BOOK.csv', names = book_field, encoding= 'utf-8', dtype= str, skiprows = [0])
    book_table = book_table.set_index('BOOK_ISBN', drop=False)
    '''if what_edit == 'BOOK_ISBN':
        book_table = book_table.reset_index()'''
    abc=str(int(book_table[book_table['BOOK_TITLE'] == book]['BOOK_ISBN']))
    print(abc)
    # print(book_table[book_table['BOOK_TITLE'] == book]['BOOK_ISBN'])
    new_values = input("새로운 값을 입력: ")
    book_table[what_edit].loc[abc] = new_values
    book_table.to_csv('csv/BOOK.csv', index=False, header=None, encoding='utf-8')


def remove_book():
    book_table = pd.read_csv('csv/BOOK.csv', encoding= 'utf-8', dtype= str)
    book_table = book_table.set_index('BOOK_ISBN', drop=False)
    del_book = input("삭제할 도서의 이름을 입력하시오.\n>>")
    if del_book in book_table['BOOK_TITLE'].values :
            abc = str(int(book_table[book_table['BOOK_TITLE'] == del_book]['BOOK_ISBN']))
            book_table.drop(index=abc, axis=0, inplace=True)
            book_table.to_csv('csv/BOOK.csv', index=False, header= True, encoding='utf-8')
    else:
        print("존재 하지 않는 책입니다.")


def inquire_book_csv():
    print(book_table[:])

    




#search_book()
#add_book()
#edit_book()
#remove_book()
#reset_book_csv() 
#inquire_book_csv()








# data = pd.read_csv("../test.csv", sep=",") csv파일 데이터 프레임에 읽어오기
# data.to_csv("test_modified.csv", sep=",", index = False)  csv 파일에 데이터 플레임 쓰기
