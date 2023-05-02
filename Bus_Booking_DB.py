import sqlite3
con=sqlite3.connect('BUS MS')
cur=con.cursor()
'''
#create table bus_details
cur.execute('create table IF NOT EXISTS bus_details(busid int(1) primary key,type varchar(15),capacity int(3),fare int(4),opid int(1),routeid int(1))')

#create table operator 
cur.execute('create table IF NOT EXISTS operator(opid int, name varchar(20),address varchar(20),phone int(10),email varchar(20))')

#create table route
cur.execute('create table IF NOT EXISTS route(routeid,sid int,station_name char(20))')

#create table runs
cur.execute('create table IF NOT EXISTS runs(busid int, runsdate date,seatavail int(2))')

#create table passenger_details

#add to bus_details

cur.execute('insert into bus_details(busid,type,capacity,fare,opid,routeid)values(1,"AC 2X2",20,1000,1,1)')
cur.execute('insert into bus_details(busid,type,capacity,fare,opid,routeid)values(2,"AC 3X2",20,800,1,2)')
cur.execute('insert into bus_details(busid,type,capacity,fare,opid,routeid)values(3," NON AC 2X2",20,500,1,3)')
cur.execute('insert into bus_details(busid,type,capacity,fare,opid,routeid)values(4," NON AC 2X2",20,500,1,4)')

#add to operator
cur.execute('insert into operator(opid,name,address,phone,email)values(1,"Samay Shatabdi","AB Road Guna",55629,"samyashatabdi@gmail.com")')
cur.execute('insert into operator(opid,name,address,phone,email)values(2,"Hans Travels","AB Road Guna",66629,"hanstravels@gmail.com")')
cur.execute('insert into operator(opid,name,address,phone,email)values(3,"kamla","AB Road Guna",77629,"kamla@gmail.com")')
cur.execute('insert into operator(opid,name,address,phone,email)values(4,"Raj Ratan","AB Road Guna",88629,"rajratan@gmail.com")')

#add to route


cur.execute('insert into route(routeid,sid,station_name)values(1,1,"Guna")')
cur.execute('insert into route(routeid,sid,station_name)values(1,2,"JP Collage")')
cur.execute('insert into route(routeid,sid,station_name)values(1,3,"Binaganj")')
cur.execute('insert into route(routeid,sid,station_name)values(1,4,"Biora")')
cur.execute('insert into route(routeid,sid,station_name)values(1,5,"Bhopal")')
cur.execute('insert into route(routeid,sid,station_name)values(2,1,"Bhopal")')
cur.execute('insert into route(routeid,sid,station_name)values(2,2,"Biora")')
cur.execute('insert into route(routeid,sid,station_name)values(2,3,"Binaganj")')
cur.execute('insert into route(routeid,sid,station_name)values(2,4,"JP Collage")')
cur.execute('insert into route(routeid,sid,station_name)values(2,5,"Guna")')
cur.execute('insert into route(routeid,sid,station_name)values(3,1,"Kanpur")')
cur.execute('insert into route(routeid,sid,station_name)values(3,2,"Lacknow")')
cur.execute('insert into route(routeid,sid,station_name)values(3,3,"Agra")')
cur.execute('insert into route(routeid,sid,station_name)values(3,4,"Delhi")')
cur.execute('insert into route(routeid,sid,station_name)values(3,5,"Guna")')
cur.execute('insert into route(routeid,sid,station_name)values(3,6,"JP college")')
cur.execute('insert into route(routeid,sid,station_name)values(3,7,"Biora")')
cur.execute('insert into route(routeid,sid,station_name)values(3,8,"Binaganj")')
cur.execute('insert into route(routeid,sid,station_name)values(3,9,"Bhopal")')
cur.execute('insert into route(routeid,sid,station_name)values(4,1,"Bhopal")')
cur.execute('insert into route(routeid,sid,station_name)values(4,2,"Biora")')
cur.execute('insert into route(routeid,sid,station_name)values(4,3,"Binaganj")')
cur.execute('insert into route(routeid,sid,station_name)values(4,4,"JP College")')
cur.execute('insert into route(routeid,sid,station_name)values(4,5,"Guna")')
cur.execute('insert into route(routeid,sid,station_name)values(4,6,"Biora")')
cur.execute('insert into route(routeid,sid,station_name)values(4,7,"Shivpuri")')
cur.execute('insert into route(routeid,sid,station_name)values(4,8,"Jhasi")')
cur.execute('insert into route(routeid,sid,station_name)values(4,9,"Agra")')

#add to runs
cur.execute('insert into runs(busid,runsdate,seatavail)values(1,"18-11-2022",30)')
cur.execute('insert into runs(busid,runsdate,seatavail)values(1,"19-11-2022",30)')
cur.execute('insert into runs(busid,runsdate,seatavail)values(1,"20-11-2022",30)')
cur.execute('insert into runs(busid,runsdate,seatavail)values(1,"21-11-2022",30)')
cur.execute('insert into runs(busid,runsdate,seatavail)values(2,"22-11-2022",30)')
cur.execute('insert into runs(busid,runsdate,seatavail)values(2,"23-11-2022",30)')
cur.execute('insert into runs(busid,runsdate,seatavail)values(2,"24-11-2022",30)')
cur.execute('insert into runs(busid,runsdate,seatavail)values(2,"25-11-2022",30)')
cur.execute('insert into runs(busid,runsdate,seatavail)values(3,"26-11-2022",30)')
cur.execute('insert into runs(busid,runsdate,seatavail)values(3,"27-11-2022",30)')
cur.execute('insert into runs(busid,runsdate,seatavail)values(3,"28-11-2022",30)')
cur.execute('insert into runs(busid,runsdate,seatavail)values(3,"29-11-2022",30)')
cur.execute('insert into runs(busid,runsdate,seatavail)values(4,"30-11-2022",30)')
cur.execute('insert into runs(busid,runsdate,seatavail)values(4,"01-12-2022",30)')
cur.execute('insert into runs(busid,runsdate,seatavail)values(4,"02-12-2022",30)')
cur.execute('insert into runs(busid,runsdate,seatavail)values(4,"03-12-2022",30)')

#add to passenger_details
 '''
#cur.execute("alter table route RENAME COLUMN 'to' TO 'destination' ")
#cur.execute("alter table route RENAME COLUMN 'from' TO 'source'")

print(cur.execute('select * from bus').fetchall())
print(cur.execute('select * from operator').fetchall())

print(cur.execute('select * from route').fetchall())
cur.execute('select * from runs')
res=cur.fetchall()
print(res)
con.commit()


































