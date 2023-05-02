from tkinter import*
import sqlite3
con=sqlite3.connect('BUS MS')
cur=con.cursor()

from tkinter.messagebox import*
root=Tk()
root.title('seat_book,check,add_details')
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='//192.168.4.11/211b076/AP\PROJECT AP/Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=w//3)
Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 14 bold').grid(row=1,column=0,columnspan=10,pady=40)
Label(root,text='Enter Journey Details',bg='chartreuse2',fg='dark green',font='Arial 10 bold').grid(row=2,column=0,columnspan=10,pady=10)
Label(root,text='To').grid(row=3,column=0)
a=Entry(root)
a.grid(row=3,column=1)
a_str=a.get()
Label(root,text='From').grid(row=3,column=2)
b=Entry(root)
b.grid(row=3,column=3)
b_str=b.get()
Label(root,text='Journey Date').grid(row=3,column=4)
c=Entry(root)
c.grid(row=3,column=5)
c_str=c.get()
#print(cur.execute("""select opr.name,bus.type,bus.capacity,runs.available,runs.fare from operator as opr,bus,runs,route where route.destination="{}" and route.origin="{}" and runs.date="{}" and bus.busid=runs.busid and route.rid=runs.routeid;""".format(a.get(),b.get(),c.get()))

mv_list=[]
mv_name=""
mv_seats=""
mv_mobile=""
mv_age=""
final_str=""
bus_type=""

def fun1():

    
    conn=sqlite3.connect('BUS MS')
    cur=conn.cursor()
    cur.execute("""select opr.name,bus.type,bus.capacity,runs.available,runs.fare from operator as opr,bus,runs,route where route.destination="{}" and route.source="{}" and runs.date="{}" and bus.busid=runs.busid and route.rid=runs.routeid;""".format(a.get(),b.get(),c.get()))
    res=cur.fetchall()
    #query_fetch_one=cursor.fetchall()
    
    final=res[0][4]
    bus=res[0][1]
    Label(root,text=res[0][0]).grid(row=5,column=1)
    Label(root,text=res[0][1]).grid(row=5,column=2)
    Label(root,text=res[0][2]).grid(row=5,column=3)
    Label(root,text=res[0][3]).grid(row=5,column=4)
    Label(root,text=res[0][4]).grid(row=5,column=5)
    
    global final_str
    final_str=str(final)

    global bus_type
    bus_type=str(bus)
    #print(final_str)
    #Label(root,text=final_str,font='black 8').grid(row=10,column=1)
    
    Label(root,text='Select Bus',font='Arial 10',fg='green').grid(row=4,column=1)
    Label(root,text='Operator',font='Arial 10',fg='green').grid(row=4,column=2)
    Label(root,text='Bus Type',font='Arial 10',fg='green').grid(row=4,column=3)
    Label(root,text='Available/Capacity',font='Arial 10',fg='green').grid(row=4,column=4)
    Label(root,text='Fare',font='Arial 10',fg='green').grid(row=4,column=5)

  
    Button(root,text='Proceed to Book',command=fun2,font='Arial 10',bg='light green').grid(row=5,column=7)
def fun2():
    Label(root,text='Fill Passenger Details To Book The Bus Ticket',bg='light blue',fg='red',font='Arial 14 bold').grid(row=6,column=0,columnspan=10,pady=10)
    Label(root,text='Name',font='Arial 8').grid(row=7,column=0)
    name_entry= Entry(root)
    name_entry.grid(row=7,column=1)
    
    Label(root,text='Gender',font='Arial 8').grid(row=7,column=2)
    Gender=StringVar()
    Gender.set('Select')
    option=['Male','Female']
    menu=OptionMenu(root,Gender,*option)
    menu.grid(row=7,column=3)
    Gender.get()

    Label(root,text='No of seats',font='Arial 8').grid(row=7,column=4)
    seats_entry= Entry(root)
    seats_entry.grid(row=7,column=5)
    
    Label(root,text='Mobile No',font='Arial 8').grid(row=7,column=6)
    mobile_entry=Entry(root)
    mobile_entry.grid(row=7,column=7)
    
    Label(root,text='Age',font='Arial 8').grid(row=7,column=8)
    age_entry=Entry(root)
    age_entry.grid(row=7,column=9)
    
    def fun4():
        mv_name=name_entry.get()
        mv_seats= seats_entry.get()
        mv_mobile=mobile_entry.get()
        mv_age=age_entry.get()
        b_str=b.get()
        c_str=c.get()
        gender= Gender.get()

        mv_list.append(mv_name)
        mv_list.append(mv_seats)
        mv_list.append(mv_mobile)
        mv_list.append(mv_age)
        mv_list.append(b_str)
        mv_list.append(c_str)
        mv_list.append(gender)
        mv_list.append(final_str)
        mv_list.append(bus_type)

        print(mv_list)
        fun3()
    Button(root,text='Book Seat',command=fun4,font='Arial 10',bg='light green').grid(row=7,column=10)
    
def fun3():
    answer=askyesno('Fare Confirm','Total amount to be paid while boarding')
    if answer:
        root.destroy()
        import Bus_ticket_4  as ticket
        ticket.mainline(mv_list)

        
Button(root,text='Show Bus',command=fun1,bg='light green').grid(row=3,column=7)

def fun4():
    root.destroy()
    import home_page



#home=PhotoImage(file='C:\\Users\\ayush\\OneDrive\\Desktop\\home\\home.png')
#Label(root,image=home).grid(row=3,column=8)
#home=PhotoImage(file='C:\\Users\\ayush\\OneDrive\\Desktop\\home\\home.png')
#Button(root,image=home,bg='Pale Green',command=fun4).grid(row=8,column=8)





































root.mainloop()
