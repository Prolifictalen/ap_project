from tkinter import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))    
img=PhotoImage(file="//192.168.4.11/211b076/AP/PROJECT AP/Bus_for_project.png")
Label(root,image=img).grid(row=0,column=0,columnspan=3,padx=500)
Label(root,text="ONLINE BUS BOOKING SYSTEM",font='Arial 14 bold',bg='sky blue',fg='red').grid(row=1,column=1)
Label(root,text="NAME: ASTHA SINGH",font='Arial 12',fg='blue').grid(row=2,column=1,pady=20)
Label(root,text="ER NO: 211B076",font='Arial 12',fg='blue').grid(row=3,column=1,pady=15)
Label(root,text="MOBILE: 7007055629 ",font='Arial 12',fg='blue').grid(row=4,column=1,pady=15)
Label(root,text="Submitted To: DR. MAHESH KUMAR",font='Arial 14 bold',bg='sky blue',fg='red').grid(row=5,column=1,pady=25)
Label(root,text="Project Based Learning",font='Arial 12',fg='red').grid(row=6,column=1)

def fun(self):
    root.destroy()
    import home_page
root.bind('<KeyPress>',fun)    
    

root.mainloop()
