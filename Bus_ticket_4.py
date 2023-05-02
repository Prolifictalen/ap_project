from tkinter import*
from tkinter.messagebox import*
import sqlite3
from datetime import date

con=sqlite3.connect('BUS MS')
cur=con.cursor()
def mainline(my_list):
    root=Tk()
    root.title('Bus_ticket')
    h,w=root.winfo_screenheight(),root.winfo_screenwidth()
    root.geometry('%dx%d+0+0'%(w,h))
    bus=PhotoImage(file='//192.168.4.11/211b076/AP/PROJECT AP/Bus_for_project.png')
    Label(root,image=bus).grid(row=0,column=0,columnspan=50,padx=w//3)

    Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 14 bold').grid(row=1,column=0,columnspan=100,pady=40)
    Label(root,text='Bus Ticket').grid(row=2,columnspan=100)

    #cur.execute("""SELECT pass.name,pass.gender,pay.no_of_seats,pass.contact,pass.age,pay.amount,pay.payid,bus.type,runs.date,pay.paydate,route.source FROM payment as pay,passenger as pass,route,runs,bus WHERE pay.payed_route=route.rid AND pay.passid=pass.id AND route.rid=runs.routeid;""")
    #print(cur.fetchall())

    fr=Frame(root,relief='groove',bd=3)
    fr.grid(row=4,column=0,columnspan=50,padx=(w/15,0))

    Label(fr,text='Passengers :',font='Arial 10 bold').grid(row=3,column=1)
    Label(fr,text="{}".format(my_list[0]),font='Arial 10 bold').grid(row=3,column=2)
    Label(fr,text='Gender :',font='Arial 10 bold').grid(row=3,column=4)
    Label(fr,text="{}".format(my_list[6]),font='Arial 10 bold').grid(row=3,column=5)
    Label(fr,text='No of seats:',font='Arial 10 bold').grid(row=4,column=1)
    Label(fr,text="{}".format(my_list[1]),font='Arial 10 bold').grid(row=4,column=2)
    Label(fr,text='Phone:',font='Arial 10 bold').grid(row=4,column=4)
    Label(fr,text="{}".format(my_list[2]),font='Arial 10 bold').grid(row=4,column=5)
    Label(fr,text='Age :',font='Arial 10 bold').grid(row=5,column=1)
    Label(fr,text="{}".format(my_list[3]),font='Arial 10 bold').grid(row=5,column=2)
    Label(fr,text='Fare Rs :',font='Arial 10 bold').grid(row=5,column=4)
    Label(fr,text="{}".format(my_list[7]),font='Arial 10 bold').grid(row=5,column=5)
    Label(fr,text='Booking Ref :',font='Arial 10 bold').grid(row=6,column=1)
    cur.execute("SELECT MAX(payid) FROM payment;")
    ref=cur.fetchall()
    f_ref=int(ref[0][0])
    final_v=f_ref+1
    Label(fr,text="{}".format(final_v),font='Arial 10 bold').grid(row=6,column=2)
    Label(fr,text='Bus Detail :',font='Arial 10 bold').grid(row=6,column=4)
    Label(fr,text="{}".format(my_list[8]),font='Arial 10 bold').grid(row=6,column=5)
    Label(fr,text='Travel on :',font='Arial 10 bold').grid(row=7,column=1)
    Label(fr,text="{}".format(my_list[5]),font='Arial 10 bold').grid(row=7,column=2)
    Label(fr,text='Booked On :',font='Arial 10 bold').grid(row=7,column=4)
    Label(fr,text="{}".format(date.today()),font='Arial 10 bold').grid(row=7,column=5)
    Label(fr,text='No of Seats:',font='Arial 10 bold').grid(row=8,column=1)
    Label(fr,text="{}".format(my_list[1]),font='Arial 10 bold').grid(row=8,column=2)
    Label(fr,text='Boarding point :',font='Arial 10 bold').grid(row=8,column=4)
    Label(fr,text="{}".format(my_list[4]),font='Arial 10 bold').grid(row=8,column=5)
    Label(fr,text='* Total amount of Rs 1000.00/- to be paid at the time of boarding',font='Arial 8').grid(row=9,columnspan=100,pady=10)

    showinfo('Success','Seat Booked')
    def bookWin_closehandler():
        answer= askyesnocancel(
            title="Closing Confirmation",
            message="For exiting press Yes or No to return to main menu"
        )

        if answer is True:
            showinfo(
                title="Thanks Screen",
                message="Thank you for using my Bus MS Service!!"
                )
            root.destroy()

        elif answer is None:
            print("Pressed Cancel Option")

        else:
            root.destroy()
            import Details_2

    root.protocol("WM_DELETE_WINDOW", bookWin_closehandler)
    con.close()
