from tkinter import *
root=Tk()
def fun():
    root.destroy()
    import seat_booking_3
    
def fun2():
    root.destroy()
    import check_booking
    
def fun3():
    root.destroy()
    import add_bus_details
    
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=3,padx=w//2.5)
Label(root,text="Online Bus Booking System",fg="Red",bg="LightBlue",font="Arial 20 bold").grid(row=1,column=0,columnspan=3)
Button(root,text="Seat Booking", font='Arial 15 bold',bg='lime green',command=fun).grid(row=2,column=0)
Button(root,text="Check Booked Seat", font='Arial 15 bold',bg='lime green',command=fun2).grid(row=2,column=1)
Button(root,text="Add Bus Details", font='Arial 15 bold',bg='lime green',command=fun3).grid(row=2,column=2,pady=h//15)
Label(root,text="For Admin Only",font='Arial 10 bold',fg="Red").grid(row=5,column=2)
root.mainloop()
