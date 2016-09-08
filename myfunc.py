myData={}
myDataList=[]

def input_data():
    print("1.입력")
    input_continue = 'y'


    while input_continue != 'n':
        name = input("이름:")
        age = input("나이:")
        addr = input("주소:")
        myData = {'name':name, 'age':age, 'addr':addr}
        #print(myData)
        myDataList.append(myData)
        
        #print(myDataList)
        
        input_continue = input("계속 입력하시겠습니까(y/n)?")
        if input_continue =='y':
            continue
        else:
            break    
        
    
def print_data():
    print("2.출력")
    print("--------------------------")
    print(" 이름           나이            주소      ")
    print("--------------------------")
    for n in myDataList:
        print("%(name)s     %(age)s    %(addr)s" % n ) 
    
def search_data():
    print("3.검색")
    keyword = input("검색할 이름을 입력하세요:")
    print("--------------------------")
    print(" 이름           나이            주소      ")
    print("--------------------------")
     
    for n in myDataList:
        if n['name']==keyword:
             print("%(name)s     %(age)s    %(addr)s" % n )
        else:
            print("데이터가 없습니다.")
    
    
        