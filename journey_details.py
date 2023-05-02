
from tkinter import *
from tkinter.messagebox import *
import sqlite3
con=sqlite3.connect('BUS MS')
cur=con.cursor()
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

def fun1():
    conn=sqlite3.connect('BUS MS')
    cur=conn.cursor()
    cur.execute("""select opr.name,bus.type,bus.capacity,runs.available,runs.fare from operator as opr,bus,runs,route where route.destination="{}" and route.source="{}" and runs.date="{}" and bus.busid=runs.busid and route.rid=runs.routeid;""".format(a.get(),b.get(),c.get()))
    res=cur.fetchall()
    #query_fetch_one=cursor.fetchall()
    
    final=res[0][4]
    Label(root,text=res[0][0],font='black 8').grid(row=6,column=1)
    Label(root,text=res[0][1],font='black 8').grid(row=6,column=2)
    Label(root,text=res[0][2],font='black 8').grid(row=6,column=3)
    Label(root,text=res[0][3],font='black 8').grid(row=6,column=4)
    Label(root,text=res[0][4],font='black 8').grid(row=6,column=5)

    final_str=str(final)
    print(final_str)


    
   
    if len(a.get())==0:
        showerror('Value Missing','Please Enter Destination')
    elif len(b.get())==0:
        showerror('Value Missing','Please Enter From')
    elif len(c.get())==0:
        showerror('Value Missing','Please Enter Date')
    else:
        showbus()




img=PhotoImage(file="//192.168.4.11/211b076/AP/PROJECT AP/Bus_for_project.png")
Label(root,text='                 ').grid(row=0,column=0)
Label(root,image=img).grid(row=0,column=2,columnspan=8)
Label(root,text='                 ').grid(row=1,column=0)
Label(root,text='Online Bus Booking System',font='Arial 14 bold', bg='cadetblue1',fg='red').grid(row=1,column=2,columnspan=8)
Label(root,text='                 ').grid(row=3,column=0)
Label(root,text='').grid(row=2,column=1)
Label(root,text='Enter Journey Details',font='Arial 14 bold',fg='green4').grid(row=3,column=2,columnspan=8,pady=10)
Label(root,text='To').grid(row=4,column=1, padx=(250,0))
a=Entry(root)
a.grid(row=4,column=2)
a_str=a.get()
Label(root,text='From').grid(row=4,column=3)
b=Entry(root)
b.grid(row=4,column=4)
b_str=b.get()
Label(root,text='Journey Date').grid(row=4,column=5)
c=Entry(root)
c.grid(row=4,column=6)
c_str=c.get()
home=PhotoImage(file='//192.168.4.11/211b076/AP/PROJECT AP/home.png')
Button(root,image=home).grid(row=4,column=8,padx=30)  
Button(root,text='Show Bus', bg='springgreen4',command=fun1).grid(row=4,column=7,padx=30)




def showbus():
    Label(root,text='Select Bus',fg='green4').grid(row=5,column=1, padx=(150,20),pady=10)
    Label(root,text='Operator',fg='green4').grid(row=5,column=2, pady=10)
    Label(root,text='Bus Type',fg='green4').grid(row=5,column=3, padx=20,pady=10)
    Label(root,text='Available/Capacity',fg='green4').grid(row=5,column=4, pady=10)
    Label(root,text='Fare',fg='green4').grid(row=5,column=5, padx=20,pady=10)
    Button(root,text='Proceed To Book', bg='green2', command=passenger).grid(row=6,column=7)
def fun2():
    if len(name.get())==0:
        showerror('Value Missing','Please Enter Name')
    elif len(no.get())==0:
        showerror('Value Missing','Please Enter No. of Seats')
    elif len(mobile.get())==0:
        showerror('Value Missing','Please Enter Mobile Number')
    elif len(age.get())==0:
        showerror('Value Missing','Please Enter Age')
    else:
        askyesno('Fare Confirm','Total amount to be paid while boarding!!!! ')
def passenger():
    Label(root,text='Fill Passenger Details to book the bus ticket',font='Arial 16 bold', bg='cadetblue1',fg='red').grid(row=8,column=1,columnspan=10,pady=20)
    Label(root,text='').grid(row=9,column=1)
    Label(root,text='Name').grid(row=10,column=1, padx=(50,0))
    name=Entry(root)
    name.grid(row=10,column=2)
    Label(root,text='Gender').grid(row=10,column=3)
    gender=StringVar()
    gender.set('Select Gender')
    opt=["Male","female","other"]
    d_menu=OptionMenu(root,gender,*opt).grid(row=10,column=4)
    Label(root,text='No of seats').grid(row=10,column=5)
    no=Entry(root)
    no.grid(row=10,column=6)
    Label(root,text='Mobile No').grid(row=10,column=7)
    mobile=Entry(root)
    mobile.grid(row=10,column=8)
    Label(root,text='Age').grid(row=10,column=9)
    age=Entry(root)
    age.grid(row=10,column=10)
def fun3():    
    askyesno('Fare confirmed','total ammount to be paid 3000')
Button(root,text='Book seat', bg='green2',command=fun3).grid(row=10,column=11)

def fun4():
    root.destroy()
    import home_page
home=PhotoImage(file='//192.168.4.11/211b076/AP/PROJECT AP/home.png')
Button(root,image=home,command=fun4).grid(row=4,column=8,padx=30)  
