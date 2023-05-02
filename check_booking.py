from tkinter import*
from tkinter.messagebox import*
root=Tk()

h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='//192.168.4.11/211b076/AP/PROJECT AP/Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=w//3)

Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 14 bold').grid(row=1,column=0,columnspan=10,pady=40)
Label(root,text='Check Your Booking',bg='light green',fg='dark green',font='Arial 12 bold').grid(row=2,column=0,columnspan=10,pady=10)


fr=Frame(root,relief='groove',bd=3)
fr.grid(row=4,column=0,columnspan=50,padx=(w/15,0))
Label(root,text='Enter Your Mobile No:').grid(row=3,column=0,padx=(w/3,0))
a=Entry(root)
a.grid(row=3,column=1)
def fun1() :
    Label(fr,text='Passengers :',font='Arial 10 bold').grid(row=4,column=0)
    Label(fr,text='Astha Singh',font='Arial 10 bold').grid(row=4,column=1)
    Label(fr,text='Gender :',font='Arial 10 bold').grid(row=4,column=2)
    Label(fr,text='Female',font='Arial 10 bold').grid(row=4,column=3)
    Label(fr,text='No of seats:',font='Arial 10 bold').grid(row=5,column=0)
    Label(fr,text='2',font='Arial 10 bold').grid(row=5,column=1)
    Label(fr,text='Phone:',font='Arial 10 bold').grid(row=5,column=2)
    Label(fr,text='7007055629',font='Arial 10 bold').grid(row=5,column=3)
    Label(fr,text='Age :',font='Arial 10 bold').grid(row=6,column=0)
    Label(fr,text='20',font='Arial 10 bold').grid(row=6,column=1)
    Label(fr,text='Fare Rs :',font='Arial 10 bold').grid(row=6,column=2)
    Label(fr,text='1000.00',font='Arial 10 bold').grid(row=6,column=3)
    Label(fr,text='Booking Ref :',font='Arial 10 bold').grid(row=7,column=0)
    Label(fr,text='3',font='Arial 10 bold').grid(row=7,column=1)
    Label(fr,text='Boarding point :',font='Arial 10 bold').grid(row=8,column=2)
    Label(fr,text='Guna',font='Arial 10 bold').grid(row=8,column=3)
    Label(fr,text='Destination point :',font='Arial 10 bold').grid(row=9,column=0)
    Label(fr,text='Bhopal',font='Arial 10 bold').grid(row=9,column=1)

    Label(fr,text='* Total amount of Rs 3000.00/- to be paid at the time of boarding',font='Arial 8').grid(row=10,columnspan=100,pady=10)
    askyesno('No Booking Record','Do you want to book seat now?')
Button(root,text='Check Booking',command=fun1).grid(row=3,column=2)
def fun2():
    root.destroy()
    import home_page
home=PhotoImage(file='//192.168.4.11/211b076/AP/PROJECT AP/home.png')
Button(root,image=home,command=fun2).grid(row=4,column=0,padx=30) 
