import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",password="localhost")
cur=mycon.cursor()
#----------------------DATABASE SETUP---------------------------
def data_setup():
    cur.execute("create database if not exists hotel_management_")
    cur.execute("use hotel_management_")
    #--------------guests table------------------
    g="""
    create table if not exists guests (
         guest_id int primary key,
         first_name varchar(20) not null,
         last_name varchar(20),
         c_in date not null,
         c_out date,
         room_number int not null,
         email varchar(50),
         phone_number varchar(15)
    );
    """
    cur.execute(g)
    #---------------rooms table----------------
    r="""
    create table if not exists rooms (
         room_number int primary key,
         room_type varchar(20) not null,
         tariff decimal(10,2) not null,
         status varchar(10) default 'Available'
    );
    """
    cur.execute(r)
    #--------------employee table----------------
    e="""
    create table if not exists employees (
         employee_id int primary key,
         first_name varchar(20) not null,
         last_name varchar(20),
         position varchar(20) not null,
         department varchar(20) not null,
         hire_date date not null,
         salary int not null,
         email varchar(50),
         phone_number varchar(15) not null
    );
    """
    cur.execute(e)
def add_room():
    while True:
        rn=int(input("Enter room number="))
        rt=input("Enter room type=")
        t=int(input("Enter tariff="))
        s=input("Enter status of room=")
        q=cur.execute(("insert into rooms values({},'{}',{},'{}')").format(rn,rt,t,s))
        cur.execute(q)
        mycon.commit()
        ch=input("Do you want to continue (y/n)?")
        if ch in "nN":
            break
                
#----------------------GUEST MANAGEMENT-------------------------
def find_guest_details():
    print('-------------------------------------------')
    gid=int(input("Enter the guest id="))
    cur.execute(("select * from guests where guest_id={}").format(gid))
    i=cur.fetchone()
    row=cur.rowcount
    if row>0 and row>(-1):
        print("\n \t GUEST DETAILS")
        print("First name:",i[1])
        print("Last name:",i[2])
        print("Check in date:",i[3])
        print("Check out date:",i[4])
        print("Room number:",i[5])
        print("Email:",i[6])
        print("Phone number:",i[7])
    else:
        print("Record not found")
        
def guest_check_in():
    print('------------GUEST CHECK IN-------------')
    gid=int(input("Enter guest id="))
    f=input("Enter first name of the guest=")
    l=input("Enter last name of the guest=")
    cur.execute("select room_number , room_type , tariff from rooms where status='available'")
    available_rooms=cur.fetchall()
    if not available_rooms:
        print("Room not available currently")
    print("\n Available rooms")
    for i in available_rooms:
        print("ROOM",i[0],"|",i[1],"|","Price:Rs.",i[2],"/night")
    r=int(input("Enter room number to be assigned="))
    c_in=input("Enter check in date of the guest=")
    e=input("Enter email of guest=")
    p=input("Enter phone number of guest=")
    cur.execute("insert into guests (guest_id,first_name,last_name,c_in,room_number,email,phone_number) values(%s,%s,%s,%s,%s,%s,%s)",(gid,f,l,c_in,r,e,p))
    cur.execute("update rooms set status='occupied' where room_number={}".format(r))
    mycon.commit()
    print("Guest checked in")
    print

def guest_check_out():
     r=int(input("Enter room number checking out="))
     cur.execute("select guest_id , first_name , last_name , phone_number from guests where room_number=%s",(r,))
     guest=cur.fetchone()
     guest_id,First_name,Last_name,Phone_number=guest
     cur.execute(("select tariff from rooms where room_number={}").format(r))
     t=cur.fetchone()[0]
     days=int(input("Enter number of days stayed by the guest="))
     total_bill=int(t)*days
     print("\n\n===========================================")
     print("-------------------INVOICE---------------------")
     print("===============================================")
     print("Guest name:",guest[1]+" "+guest[2])
     print("Room number:",r)
     print("Duration:",days)
     print("-------------------------")
     print("Total amount to be payed:",total_bill)
     print("-------------------------")
     p=input("Payment received (y/n)?")
     if p in "yY":
         d=input("Enter date=")
         cur.execute(("update guests set c_out='{}' where room_number={}").format(d,r))
         print("Check out successful")
     else:
         cur.execute(("update rooms set status='available' where room_number={}").format(r))
         print("Check out cancelled")

def upg_guest_info():
    while True:
        print("\n\t\t Press 1 to change first name \n\t\t Press 2 to change last name \n Press 3 to change check out date \n Press 4 to change room number \n Press 5 to change email \n Press 6 to change phone number \n Press 7 to exit")
        print('--------------------------------------')
        ch=int(input("Enter your choice="))
        if ch==1:
            gid=int(input("Enter guest id="))
            f1=input("Enter new first name=")
            q=("update guests set first_name='{}' where guest_id={}").format(f1,gid)
            cur.execute(q)
            mycon.commit()
            print("Data updated")
        elif ch==2:
            gid=int(input("Enter guest id="))
            l1=input("Enter new last name=")
            q=("update guests set last_name='{}' where guest_id={}").format(l1,gid)
            cur.execute(q)
            mycon.commit()
            prupgint("Data updated")
        elif ch==3:
            gid=int(input("Enter guest id="))
            c_in1=input("Enter new check out date=")
            q=("update guests set c_in='{}' where guest_id={}").format(c_in1,gid)
            cur.execute(q)
            mycon.commit()
            print("Data updated")
        elif ch==4:
            gid=int(input("Enter guest id="))
            r1=int(input("Enter new room number="))
            q=("update guests set room_number={} where guest_id={}").format(r1,gid)
            cur.execute(q)
            mycon.commit()
            print("Data updated")
        elif ch==5:
            gid=int(input("Enter guest id="))
            e1=input("Enter new email=")
            q=("update guests set email='{}' where guest_id={}").format(e1,gid)
            cur.execute(q)
            mycon.commit()
            print("Data updated")
        elif ch==6:
            gid=int(input("Enter guest is="))
            n1=int(input("Enter new number="))
            q=("update guests set email='{}' where guest_id={}").format(e1,gid)
            cur.execute(q)
            mycon.commit()
            print("Data updated")
        elif ch==7:
            break
        else:
            print("invalid input")
            o=input("do you want to continue y or n?")
            if o in "nN":
                break

#---------------------EMPLOYEE MANAGEMENT----------------------------
def add_employee_info():
    while True:
        print("--------------------------------")
        eid=int(input("Enter employee id="))
        f=input("Enter first name:")
        l=input("Enter last name:")
        p=input("Enter position:")
        d=input("Enter department:")
        h=input("Enter hire date:")
        s=int(input("Enter salary:"))
        e=input("Enter email:")
        pn=input("Enter phone number:")
        cur.execute("insert into employees values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(eid,f,l,p,d,h,s,e,pn))
        mycon.commit()
        print("Data successfully added")
        c=input("Do you want to continue (y/n)?")
        if c in "nN":
              break
def upg_employee_info():
    while True:
        print("\n\t\t Press 1 to change first name \n Press 2 to change last name \n Press 3 to change position \n Press 4 to change department \n Press 5 to change salary \n\t\t Press 6 to change email \n\t\t Press 7 to change phone number \n Press 8 to exit")
        print("------------------------------------")
        ch=int(input("Enter your choice="))
        if ch==1:
            eid=int(input("Enter employee id="))
            f1=input("Enter new first name=")
            q=("update employees set first_name='{}' where employee_id={}").format(f1,eid)
            cur.execute(q)
            mycon.commit()
            print("Data updated")
        elif ch==2:
            eid=int(input("Enter employee id="))
            l1=input("Enter new last name=")
            q=("update employees set last_name='{}' where employee_id={}").format(l1,eid)
            cur.execute(q)
            mycon.commit()
            print("Data updated")
        elif ch==3:
            eid=int(input("Enter employee id="))
            p1=input("Enter new position=")
            q=("update employees set position='{}' where employee_id={}").format(p1,eid)
            cur.execute(q)
            mycon.commit()
            print("Data updated")
        elif ch==4:
            eid=int(input("Enter employee id="))
            d1=input("Enter new department=")
            q=("update employees set department='{}' where employee_id={}").format(d1,eid)
            cur.execute(q)
            mycon.commit()
            print("Data updated")
        elif ch==5:
            eid=int(input("Enter employee id="))
            n=int(input("Enter percent of salary to be decreased or increased="))
            o=input("Enter if salary to be incremented or decremented (i/d)=")
            if o in "Ii":
                q=("update employees set salary=salary+({}/100)*salary where employee_id={}").format(n,eid)
            elif o in "Dd":
                q=("update employees set salary=salary-({}/100)*salary where employee_id={}").format(n,eid)
            else:
                print("wrong input")
            cur.execute(q)
            mycon.commit()
            print("Data updated")
        elif ch==6:
            eid=int(input("Enter employee id="))
            e1=input("Enter new email=")
            q=("update employees set email='{}' where employee_id={}").format(e1,eid)
            cur.execute(q)
            mycon.commit()
            print("Data updated")
        elif ch==7:
            eid=int(input("Enter employee id="))
            p1=int(input("Enter new phone number="))
            q=("update employees set phone_number={} where employee_id={}").format(p1,eid)
            cur.execute(q)
            mycon.commit()
            print("Data updated")
        elif ch==8:
            break
        else:
            print("invalid input")
            c=input("Do you want to continue (y/n)?")
            if c in "nN":
                break

def delete_employee_info():
    print('--------------------------------')
    eid=int(input("Enter employee id="))
    cur.execute(("delete from employees where employee_id={}").format(eid))
    mycon.commit()
    print("Data cleared")

def display_employee_info():
    print('--------------------------------')
    eid=int(input("Enter employee id="))
    cur.execute("select * from employees where employee_id={}".format(eid))
    d=cur.fetchone()
    row=cur.rowcount
    if row>0 and row>-1:
        print("\n\t EMPLOYEE DETAILS")
        print("First name:",d[1])
        print("Last name:",d[2])
        print("Position:",d[3])
        print("Department:",d[4])
        print("Hire date:",d[5])
        print("Salary:",d[6])
        print("Email:",d[7])
        print("Phone number:",d[8])
    else:
        print("Record not found")

#--------------------MAIN MENU---------------------
data_setup()
print("=======================================================")
print("-------------------HOTEL MANAGEMENT--------------------")
print("=======================================================")
print("Create list of rooms first")
c=input("do you want to add rooms (y/n)?")
if c in "yY":
    add_room()
while True:
    ch=int(input("Enter you choice \n Press 1 for guest management \n Press 2 for employee management \n Press 3 to exit"))   
    if ch==1:
        while True:
            print("--------------------------------------------------")
            ch1=int(input("Press 1 for guest check in\nPress 2 to find a guest's details\nPress 3 to update a guest's info \n Press 4 for check out \n Press 5 to exit"))
            if ch1==1:
                guest_check_in()
            elif ch1==2:
                find_guest_details()
            elif ch1==3:
                upg_guest_info()
            elif ch1==4:
                guest_check_out()
            elif ch1==5:
                break
            else:
                p=input("Do you want to continue (y/n)?")
                if p in "nN":
                    break
            print("--------------------------------------------------")
    elif ch==2:
         while True:
             print("----------------------------------------------------")
             ch2=int(input("Enter your choice \n Press 1 to add info of an employee \n Press 2 to upgrade an employee's info \n Press 3 to delete an employee's info \n Press 4 to display an employee's info \n Press 5 to exit"))
             if ch2==1:
                 add_employee_info()
             elif ch2==2:
                 upg_employee_info()
             elif ch2==3:
                 delete_employee_info()
             elif ch2==4:
                 display_employee_info()
             elif ch2==5:
                 break
             else:
                 p=input("Do you want to continue (y/n)?")
                 if p in "nN":
                     break
             print("----------------------------------------------------")
    elif ch==3:
        break
    else:
        p=input("Do you want to continue (y/n)?")
        if p in "nN":
            break
