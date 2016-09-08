from myfunc import * 

def print_menu():
    print("메인메뉴)")
    print("    1.입력")
    print("    2.출력")
    print("    3.검색")
    print("    4.종료")
    print("    번호를 입력하세요")

print_menu()
select = int(input("입력) "))

while select != 4:
    if(select == 1):
        input_data()
        print_menu()
        select = int(input("입력) "))
    elif(select == 2):
        print_data()
        print_menu()
        select = int(input("입력) "))
    elif(select == 3):
        search_data()
        print_menu()
        select = int(input("입력) "))
    else:
        break

print("4.종료")