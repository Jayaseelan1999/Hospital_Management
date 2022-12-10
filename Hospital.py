import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector as sql

conn=sql.connect (host='Localhost',user='root',passwd="",database='jaya_hospital')
if conn.is_connected() :
    print( 'successfully connected')
c1=conn.cursor()
print('-----------------------------')
print("HOSPITAL MANAGEMENT SYSTEM")
print('-----------------------------')
print('1.About the Project')
print('2.Create Table doctor details')
print('3. Describe doctor_ details')
print('4. Register Doctor details')
print('5.ALL doctor details')
print('6.Create Table patient_details')
print('7. Describe patient _details')
print('8.Register patient details')
print('9.ALL patient details')
print('10.Create Table worker details')
print('11. Describe worker_details')
print('12.Register worker details')
print('13.ALL worker details')
print('14. Search Doctor details')
print('15. Search Patient details')
print('16.Search Worker details')
print('17. Update Patient details')
print('18. Update Doctor details')
print('19. Update Worker details')
print('20. Bill_details ')
print('21. ENTER CHARGES of PATIENT for BiLL_details')
print('22. Show records of Bill')
print('23. Delete a Column')
print('24. Delete a Record')
print('25. Sort Workers')
print('26. Total bills')
print('27. Line Plot ')
print('28. Pie Plot')
print('29. Bar Plot')
print('30. Horizontal Bar Plot')



def about () :
    print( 'You are working in HOSPITAL MANAGEMENT SYSTEM Project. It has 30 options to run including 4 plots')



def create_doctor_details():
    c1=conn. cursor ()
    c1. execute('create table doctor details (d_id int (5), d_name varchar (25) primary key,d_age int(3),d_department '
                'varchar (25),d_phono int(10)')
    print( 'table created')



def desc_doctor_details():
    print ('show structure of doctor_details table')
    df=pd.read_sq1("desc worker_details", conn)
    print(df)



def insert_doctor_details():
    print('Enter Details of New Doctor')
    d_id=int (input('Enter ID of Doctor: '))
    d_name=input ('Enter Doctor Name: ')
    d_age=int (input ('Enter Age: '))
    d_department=input ('Enter the Department: ')
    d_phono=int (input ('Enter Phone number: '))
    sql_insert=("insert into doctor_details values("""+str(d_id)+", , '"+d_name+"', "+str(d_age)+", ,'"+d_department+"',"+str(d_phono)+")")
    c1. execute (sql_insert)
    print('Registered new Doctor')
    conn.commit ()



def show_records_doctor_details():
    print('ALL records of doctors')
    df=pd.read_sq1("select * from doctor_details", conn)
    print(df)



def create_patient_details ():
    print( 'Create table for Patients')
    c1=conn.cursor ()
    c1.execute('create table patient_details (P_id int (5), p_name varchar (25) primary key,p_age int(3),p_problems '
               'varchar(10)')
    print( 'table created')



def desc_patient_details():
    print ('show structure of patient_details table')
    df=pd.read_sql("desc patient_details", conn)
    print (df)



def insert_patient_details():
    print ('Enter New patient Information')
    p_id=int(input('Enter ID of Patient:'))
    p_name=input ('Enter Patient Name:')
    p_age=int (input ('Enter Age: '))
    p_problems=input ('Enter the Problem/Disease:')
    p_phono=int (input ('Enter Phone number: '))
    sql_insert=("insert into patient_details values("+str(p_id)+", "+p_name+","+str(p_age)+","+p_problems+","+str(p_phono)+")")
    c1.execute(sql_insert)
    print( 'SUCCESSFULLY REGISTERED')
    conn. commit ()



def show_records_patient_details():
    print('Records of All patients')
    df=pd.read_sql("select * from patient_details", conn)
    print(df)



def create_worker_details():
    c1=conn.cursor()
    c1.execute('create table worker_details(w_id int (5), w_name varchar (25) primary key,w_age int(3),w_work_name varchar(25),w_phono int(10)')
    print('table created')



def desc_worker_details():
    print('show structure of worker_details table')
    df=pd.read_sq1("desc worker_details", conn)
    print (df)



def insert_worker_details():
    print('Enter New patient Information')
    w_id=int(input ('Enter ID of Patient:'))
    w_name=input ('Enter Worker Name: ')
    w_age=int(input ('Enter Age:'))
    w_work_name=input ('Enter type of work:')
    w_phono=int (input( 'Enter Phone number: '))
    sql_insert="insert into worker_details values("+str (w_id)+", "+w_name+","+str(w_age)+","+w_work_name+","+str(w_phono)+")"
    c1.execute(sql_insert)
    print( 'SUCCESSFULLY REGISTER')
    conn. commit ()



def show_records_worker_details():
    print('All record of worker_details')
    df=pd.read_sql("select * from worker _details", conn)
    print(df)



def search_doctor_details():
    print('Search Doctor Record by entering ID')
    exp = float(input("Enter Doctor id"))
    qry = "select * from doctor_details where d_id-%s; " % (exp,)
    df=pd.read_sql(qry,conn)
    print(df)


def search_patient_details():
    print('Search Patient Record by entering ID')
    exp = float(input("Enter patient id:"))
    qry = "select * from patient_details where p_id-%s; " % (exp,)
    df = pd.read_sq1(qry, conn)
    print(df)


def search_worker_details():
    print('Search Worker Record by entering ID')
    w = float(input("Enter Worker id:"))
    qry = "select * from worker_details where w_ id-%s; " % (w,)
    df=pd.read_sq1(qry, conn)
    print(df)


def update_patient_details():
    print("Change phone no.of Patient")
    c1 = conn.cursor()
    c1.execute("update patient _details set p_phono =2123450 where p_id= '201'")
    print("Phone no. Updated")
    conn.commit()
    df= pd.read_sq1("select * from patient_details", conn)
    print(df)



def update_doctor_details():
    print('Change Department of Doctor')
    c1 = conn.cursor()
    c1.execute("update doctor_details set d_ department = 'Neuro' where d_id='102'")
    conn.commit()
    df = pd.read_sq1("select * from doctor_details", conn)
    print(df)
    print("Department Updated")



def update_worker_details():
    print("Change Age of Worker")
    c1 = conn.cursor()
    c1.execute("update worker_details set w_age =3% where w_id= '302'")
    print("Age Updated")
    conn.commit()
    df=pd.read_sq1("select * from worker_details", conn)
    print(df)



def create_bill_details():
    c1 = conn.cursor()
    c1.execute('create table bill (p_id int (5), P_name varchar(25) primary key, p_age int(5),visit int(5),medicines int(5),room(5)')
    print('table created')


def insert_bill_details():
    print('Enter Charges of patient in Bill')
    p_id = int(input('Enter ID of Patient:'))
    p_name = input('Enter Patient Name: ')
    p_age = int(input('Enter Age: '))
    visit = int(input('Enter Fee of Dr. Visits: '))
    medicines=int(input('Enter the cost of medicines: '))
    room = int(input('Enter Room Charges: '))
    sql_insert = ("insert into bill values("+str(p_id)+","+p_name+","+str(p_age)+","+str(visit)+","+str(medicines)+","+str(room)+")")
    c1.execute(sql_insert)
    conn.commit()



def show_records_bi11():
    print('All record of Bill')
    df = pd.read_sq1("select from bill", conn)
    print(df)


def del_col():
    df=pd.read_sql("select * from bill", conn)
    print(df)
    print()
    print()
    print('Column deleted')
    del df['total_bill']
    print(df)


def del_record_worker():
    c1 = conn.cursor()
    c1.execute("delete from worker_details where W_name= 'Neena'")
    print("Record of Neena Deleted")
    conn.commit()


def sort_workers():
    print('sorting Workers names in Ascending order')
    print()
    df = pd.read_sq1("select * from worker_details ", conn)
    df = df.sort_values('w_name')
    print(df)


def total_bill():
    print('Records of charges without Total ')
    print()
    df = pd.read_sql("select * from billi", conn)
    print(df)
    print()
    column_list = list(df)
    print(column_list)
    print()
    column_list.remove(p_id)
    df["total_bill"] = df[column_list].sum(axis=1)
    print(df)


def line_plot():
    print('Line plot')
    df = pd.read_sql("select * from bill", conn)
    x1 = df['p_name ']
    y1 = df['medicines']
    plt.plot(x1, y1, color='r', linewidth=5, marker='o', markerfacecolor='blue')
    plt.show()

def pie_plot():
    print('Pie plot')
    df = pd.read_sql("select * from bill",conn)
    print(df)
    plt.title(' Charges on Room, Medicine, Dr. Visit on the items')
    z=eval(input( 'enter charges of Room, Medicine, Visit in sq brackets'))
    color = ['red', 'green', 'blue']
    items = ['medicines', 'room', 'visit']
    exp1=[0,0,0.2]
    plt.pie(z, colors=color, labels=items, explode=exp1, autopct="5.1f%%")
    plt.show()

def bar_plot():
    print('bar plot')
    df = pd.read_sql("select * from bill", conn)
    x1 = df['P_name ']
    y1 = df['medicines']
    plt.xlabel('Patient Name', fontsize=14, color="~")
    plt.ylabel('medicines', fontsize=14, color="r")
    plt.title('Paid for Medicines ', fontsize = 14, color="blue")
    plt.xticks(fontsize=14, rotation=30)
    plt.bar(x1, y1, width=0.5, facecolor='r', edgecolor='green')
    plt.show()

def barh_plot():
    print('Horizontal bar plot')
    df = pd.read_sql("select * from bill", conn)
    x = df['p_name']
    y = df['room ']
    plt.xlabel('Patient Name', fontsize=14, color="p")
    plt.ylabel('Room', fontsize=14, color="r")
    plt.title('Paid for Room',fontsize=14, color= "blue")
    plt.barh (x,y, color= 'orange')
    plt. show()


opt = ""
opt = int(input("enter your choice : "))
if opt == 1:
    about()
elif opt == 2:
    create_doctor_details()
elif opt == 3:
    desc_doctor_details()
elif opt == 4:
    insert_doctor_details()
elif opt == 5:
    show_records_doctor_details()
elif opt == 6:
    create_patient_details()
elif opt == 7:
    desc_patient_details()
elif opt == 8:
    insert_patient_details()
elif opt == 9:
    show_records_patient_details()
elif opt == 10:
    create_worker_details()
elif opt == 11:
    desc_worker_details()
elif opt == 12:
    insert_worker_details()
elif opt == 13:
    show_records_worker_details()
elif opt == 14:
    search_doctor_details()
elif opt == 15:
    search_patient_details()
elif opt == 16:
   search_worker_details()
elif opt == 17:
    update_patient_details()
elif opt == 18:
    update_doctor_details()
elif opt == 19:
    update_worker_details()
elif opt == 20:
    create_bill_details()
elif opt == 21:
    insert_bill_details()
elif opt == 22:
    show_records_bi11()
elif opt == 23:
    del_col()
elif opt == 24:
    del_record_worker()
elif opt == 25:
    sort_workers()
elif opt == 26:
    total_bill()
elif opt == 27:
    line_plot()
elif opt == 28:
    pie_plot()
elif opt == 29:
    bar_plot()
elif opt == 30:
    barh_plot()
else:
    print('invalid_option')

