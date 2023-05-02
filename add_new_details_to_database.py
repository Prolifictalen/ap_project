from tkinter import *
root = Tk()

h,w = root.winfo_screenheight(),root.winfo_screenwidth(),
root.geometry('%dx%d+0+0'%(w,h))
img = PhotoImage(file="//192.168.4.11/211b076/AP/PROJECT AP/Bus_for_project.png")
frame1= Frame(root)
frame1.grid(row=0, column=1, columnspan=6)
Label(frame1, image=img).grid(row=0, column=1, columnspan=6, padx=w//3)
Label(frame1, text = "ONLINE BUS BOOKING SYSTEM", font = 'Arial 14 bold', bg = 'sky blue', fg = 'red').grid(row=1, column=1, padx=w//3, pady=10)
Label(frame1, text = "Add New Details To Database", font = 'Arial 14 bold', fg = 'dark green').grid(row=2, column=1, padx=w//3, pady=10)





def newoperator():
    root.destroy()
    import add_bus_operator_details
Button(root, text = "New Operator", font = 'Arial 12',bg = 'light green', fg = 'black',command=newoperator).grid(row=3, column=1, padx=100)
def newbus():
    import add_bus_detail
    root.destroy()
Button(root, text = "New Bus", font = 'Arial 12', bg = 'coral2', fg = 'black',command=newbus).grid(row=3, column=2, padx=50)
def newroute():
    root.destroy()
    import add_bus_route_details
Button(root, text = "New Route", font = 'Arial 12',bg = 'sky blue', fg = 'black',command=newroute).grid(row=3, column=3, padx=50)
def newrun():
    root.destroy()
    import add_bus_running_details
Button(root, text = "New Run", font = 'Arial 12', bg = 'pink3', fg = 'black',command=newrun).grid(row=3, column=4, padx=50)
root.mainloop()
