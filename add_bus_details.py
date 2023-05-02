from tkinter import *
from tkinter.messagebox import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
    
        
img=PhotoImage(file='//192.168.4.11/211b076/AP/PROJECT AP/Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=10,padx=w//3)
Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 14 bold').grid(row=1,column=0,columnspan=15)
Label(root,text='Add Bus Details',fg='green',font='Arial 11 bold').grid(row=2,column=0,columnspan=15,pady=20)
Label(root,text='Bus Id').grid(row=3,column=0)
Entry(root).grid(row=3,column=1)
Label(root,text='Bus Type').grid(row=3,column=2)
bus_type=StringVar()
bus_type.set('Bus type')
option=['AC 2x2','AC 3x2','Non AC 2x2','Non AC 3x2','AC Sleeper 2x1','Non AC Sleeper 2x1']
menu=OptionMenu(root,bus_type,*option)
menu.grid(row=3,column=3)

Label(root,text='Capacity').grid(row=3,column=4)
Entry(root).grid(row=3,column=5)
Label(root,text='Fare Rs').grid(row=3,column=6)
Entry(root).grid(row=3,column=7)
Label(root,text='Oprator Id').grid(row=3,column=8)
Entry(root).grid(row=3,column=9)
Label(root,text='Route Id').grid(row=3,column=10)
Entry(root).grid(row=3,column=11)
def fun():
    showinfo('bus entry','Bus record added')
Button(root,text='Add Bus',bg='light green',font='Calibri 11',command=fun).grid(row=4,column=6)
Button(root,text='Edit Bus',bg='Light green',font='Calibri 11').grid(row=4,column=7)
home=PhotoImage(file='//192.168.4.11/211b076/AP/PROJECT AP/home.png')
def fun1():
    root.destroy()
    import home_page
Button(root,image=home,command=fun1).grid(row=4,column=8)





