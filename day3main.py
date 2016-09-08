import sqlite3

myDataList=[]

def select_menu():
    print("="*30)
    print("성적데이터 처리")
    print("="*30)
    print("1.입력")
    print("2.보기")
    print("3.삭제")
    print("4.수정")
    print("5.검색")
    print("6.정렬")
    print("7.종료")
    return int(input("메뉴를 선택하세요: "))

# DB by sqlite3 method
#테이블명: grade 필드명: name, kor,eng, math

def createTable():
    db = sqlite3.connect('day3main.db')
    try:
        cur = db.cursor()
        q="create table grade( name test, kor int, eng int, math int)"
        cur.execute(q)
        db.commit()
        db.close()
#         print("create success")
    except Exception as err:
        pass
    
def input_record():
#     print("input_record>")
    input_continue= 'y'
    
    while input_continue !='n':
        name= input("이름:")
        kor = int(input("국어:"))
        eng = int(input("영어:"))
        math= int(input("수학:"))
        myDataList.append((name, kor, eng, math))
        
        input_continue = input("계속 입력하시겠습니까?(y/n)")
        if input_continue =='y':
            continue
        else:
            break
    
    db = sqlite3.connect('day3main.db')
    try:
        cur = db.cursor()
        q="insert into grade(name,kor,eng,math) values(?,?,?,?)"
        cur.executemany(q,myDataList)
        db.commit()
        db.close()
#         print("insert success")
    except Exception as err:
        print("err",err)
    
def show_record():
#     print("show_record>")
    db = sqlite3.connect('day3main.db')
    try:
        cur = db.cursor()
        q = "select * from grade"
        cur.execute(q)
        data = cur.fetchall()           #모든 레코드를 추출
        print("="*50)
        print("이름\t","국어\t","영어\t","수학\t","총점\t","평균\t")
        print("="*50)
        for name,kor,eng,math in data:
            total = kor+eng+math
            avg = total/3
            print(name,"\t",kor,"\t",eng,"\t",math,"\t", total, "\t", avg,"\t")
        print("="*50)
            
        db.commit()
        db.close()
#         print("select success")
    except Exception as err:
        print("err",err)
    
def delete_record():
#     print("delete_record>")
    delete_name = input("삭제할 이름을 입력하세요:")
    
    db = sqlite3.connect('day3main.db')
    try:
        cur = db.cursor()
        q="delete from grade where name=?"
        cur.execute(q,(delete_name,) )
        db.commit()
        db.close()
        print("delete success")
    except Exception as err:
        print("err",err)

def update_record():
    print("update_record>")

def search_record():
#     print("search_record>")
    search_name = input("찾을 이름을 넣으세요:")
    
    db = sqlite3.connect('day3main.db')
    try:
        cur = db.cursor()
        q="select * from grade where name=?"
        cur.execute(q, (search_name,))
        data = cur.fetchall()           #모든 레코드를 추출
        print("="*50)
        print("이름\t","국어\t","영어\t","수학\t","총점\t","평균\t")
        print("="*50)
        for name,kor,eng,math in data:
            total = kor+eng+math
            avg = total/3
            print(name,"\t",kor,"\t",eng,"\t",math,"\t", total, "\t", avg,"\t")
        print("="*50)
            
        db.commit()
        db.close()
#         print("select success")
    except Exception as err:
        print("err",err)
    
def sort_record():
#     print("sort_record>")
    isSort = input("정렬하시겠습니까?(y/n)")
    db = sqlite3.connect('day3main.db')
    try:
        cur = db.cursor()
        if isSort == 'y':
            q = "select * from grade order by name asc"
        else:
            q = "select * from grade"
             
        cur.execute(q)
        data = cur.fetchall()           #모든 레코드를 추출
        print("="*50)
        print("이름\t","국어\t","영어\t","수학\t","총점\t","평균\t")
        print("="*50)
        for name,kor,eng,math in data:
            total = kor+eng+math
            avg = total/3
            print(name,"\t",kor,"\t",eng,"\t",math,"\t", total, "\t", avg,"\t")
        print("="*50)
            
        db.commit()
        db.close()
#         print("select success")
    except Exception as err:
        print("err",err)


def main():
    createTable()
    while True:
        sel = select_menu()
        if sel == 1:
            input_record()
        elif sel == 2:
            show_record()
        elif sel == 3:
            delete_record()
        elif sel == 4:
            update_record()
        elif sel == 5:
            search_record()
        elif sel == 6:
            sort_record()
        elif sel == 7:
            print("종료")
            exit()

if __name__ == '__main__':
    main()
    