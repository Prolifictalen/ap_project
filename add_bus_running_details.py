from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file="//192.168.4.11/211b076/AP/PROJECT AP/Bus_for_project.png")
home=PhotoImage(file="//192.168.4.11/211b076/AP/PROJECT AP/home.png")
Label(root,image=img).grid(row=0,column=1,columnspan=11,pady=20)
Label(root,text='Online Bus Booking System',font='Arial 14 bold', bg='cadetblue1',fg='red').grid(row=1,column=1,columnspan=11)
Label(root,text='Add Bus Running Details',font='Arial 14 bold',fg='green4').grid(row=2,column=1,columnspan=11,pady=20)
Label(root,text='BusID').grid(row=4,column=0,padx=(300,0),pady=40)
Entry(root).grid(row=4,column=1,padx=10)
Label(root,text='Running Date').grid(row=4,column=2)
Entry(root).grid(row=4,column=3,padx=10)
Label(root,text='Seat Available').grid(row=4,column=4)
Entry(root).grid(row=4,column=5,padx=10)
Button(root,text='Add Run',bg='SpringGreen2').grid(row=4,column=6)
Button(root,text='Delete Run',bg='SpringGreen2').grid(row=4,column=7,padx=10)

def fun():
    root.destroy()
    import home_page
Button(root,image=home,command=fun).grid(row=5,column=6)
