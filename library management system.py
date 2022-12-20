import matplotlib.pyplot as plt
import pymysql
connection = pymysql.connect(host="localhost",user="root",passwd="root",database="library")


def login():
    username=input("enter your username")
    password=input("enter password")
    if password=="sacs1234":
        main()
    else:
        print("Wrong Password")
        login()
        
def main():
    print("\t \t \t WELCOME !!!!!!!!!!")
    print("*"*80)
    print("\t \t \t Library Management System")
    print("*"*80)
    print("""choose from the following: \n 1. display available books \n 2. issue book \n 3. return book  \n 4. add book \n 5.Show Stats \n 6.exit""")
    choice=int(input("enter choice"))
    if choice==1:
        displaybook()
    elif choice==2:
        issuebook()
    elif choice==3:
        returnbook()
    elif choice==4:
        addbook()
    elif choice==5:
        stats()
        main()
    elif choice==6:
        print("thank you for visiting")
    else:
        print("invalid choice")
        
def addbook():
    bookname=input("Enter book name")
    aname=input("enter authorname")
    code=input("enter book code")
    tot=int(input("enter total"))
    data=(bookname,aname,code,tot)
    sql='insert into books values(%s,%s,%s,%s)'
    cursor = connection.cursor()
    cursor.execute(sql,data)
    connection.commit()
    print("book added successfully")
    main()

def issuebook():
    name=input("enter student name")
    reg=input("enter registeration number")
    code=input("enter book code")
    issue=input("enter issue date")
    data=(name,reg,code,issue)
    sql='insert into issue values(%s,%s,%s,%s)'
    cursor = connection.cursor()
    cursor.execute(sql,data)
    connection.commit()
    print("book issued by",name,"successfully")
    bookcount(code,-1)

def returnbook():
    name=input("enter student name")
    reg=input("enter registeration number")
    code=input("enter book code")
    submit=input("enter return date")
    data=(name,reg,code,submit)
    sql='insert into submit values(%s,%s,%s,%s)'
    cursor = connection.cursor()
    cursor.execute(sql,data)
    connection.commit()
    print("book submitted by",name,"successfully")
    bookcount(code,1)

def bookcount(code,u):
    a='select total from books where bcode = %s'
    data=(code,)
    cursor = connection.cursor()
    cursor.execute(a,data)
    result=cursor.fetchone()
    tot=result[0]+u
    sql='update books set total=%s where bcode=%s'
    d=(tot,code)
    cursor.execute(sql,d)
    connection.commit()
    main()


def displaybook():
    sql='select * from books'
    cursor = connection.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:
        print("book name:",row[0])
        print("author name:",row[1])
        print("book code:",row[2])
        print("total no. of books:",row[3])
        print("*"*80)
    main()


def jgraph():
    x=['issue','return']
    y=[7,5]
    c=["blue","red"]
    w=[0.2,0.2]
    plt.bar(x,y,width=w,color=c)
    plt.xlabel("status")
    plt.ylabel("number of books")
    plt.title("books issued and returned by justin till date")
    plt.show()

def lgraph():
     x=['issue','return']
     y=[5,2]
     c=["blue","red"]
     w=[0.2,0.2]
     plt.bar(x,y,width=w,color=c)
     plt.xlabel("status")
     plt.ylabel("number of books")
     plt.title("books issued and returned by lakshya till date")
     plt.show()

def stats():
    username=input("enter username")
    if username=='justin':
        jgraph()
    elif username=='lakshya':
        lgraph()
    else:
        print("no stats available")

login()
        
        

    
    
    
    

    
