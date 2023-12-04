#__________________________________________________________________________________________________
# Imports
import tkinter as tk 
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import messagebox 
import tkinter.font as font 
import mysql.connector as mys 
import time 
from time import sleep
from mysql.connector import Error
#__________________________________________________________________________________________________
## Definition 1
def frmInsert():
    def submit():
        Sno=txtSno.get()
        Passengers=txtPassengers.get()
        Distance=txtDistance.get()
        Cargo=txtCargo.get()
        Aircraft=txtAircraft.get()
        print(Sno,Passengers,Distance,Cargo,Aircraft)
        Insert(Sno,Passengers,Distance,Cargo,Aircraft)
    def clear():
        txtSno.delete(0,END)
        txtPassengers.delete(0,END)
        txtDistance.delete(0,END)
        txtCargo.delete(0,END)
        txtAircraft.delete(0,END)      
    root = tk.Tk()
    root.geometry("300x300")
    root.title("DBMS Insert Page")
    root.configure(bg='#272936')
    Label(root, bg ="cyan", height = 500, width = 600)
    lblSno = tk.Label(root, text ="Sno",bg='#272936',fg ='#bababa',font=("Calibri", 10) )
    lblSno.place(x = 50, y = 20)
    txtSno= tk.Entry(root, width = 35,bg='#414141',fg ='#bababa',font=("Calibri", 10))
    txtSno.place(x = 150, y = 20, width = 100)
    lblPassengers = tk.Label(root, text ="Passengers",bg='#272936',fg ='#bababa',font=("Calibri", 10))
    lblPassengers.place(x = 50, y = 50)
    txtPassengers = tk.Entry(root, width = 35,bg='#414141',fg ='#bababa',font=("Calibri", 10))
    txtPassengers.place(x = 150, y = 50, width = 100)
    lblDistance = tk.Label(root, text ="Distance",bg='#272936',fg ='#bababa',font=("Calibri", 10) )
    lblDistance.place(x = 50, y = 80)
    txtDistance= tk.Entry(root, width = 35,bg='#414141',fg ='#bababa',font=("Calibri", 10))
    txtDistance.place(x = 150, y = 80, width = 100)
    lblCargo = tk.Label(root, text ="Cargo",bg='#272936',fg ='#bababa',font=("Calibri", 10) )
    lblCargo.place(x = 50, y = 110)
    txtCargo= tk.Entry(root, width = 35,bg='#414141',fg ='#bababa',font=("Calibri", 10))
    txtCargo.place(x = 150, y = 110, width = 100)
    lblAircraft = tk.Label(root, text ="Aircraft",bg='#272936',fg ='#bababa',font=("Calibri", 10) )
    lblAircraft.place(x = 50, y = 140)
    txtAircraft= tk.Entry(root, width = 35,bg='#414141',fg ='#bababa',font=("Calibri", 10))
    txtAircraft.place(x = 150, y = 140, width = 100)
    btnsubmit = tk.Button(root, text ="Submit",
                    bg='#272936',fg ='#bababa',font=("Calibri", 10),command=submit)
    btnsubmit.place(x = 100, y = 170, width = 60)
    btnclear = tk.Button(root, text ="Clear",
                    bg='#272936',fg ='#bababa',font=("Calibri", 10),command=clear)
    btnclear.place(x = 200, y = 170, width = 60)
def Insert(Sno,Passengers,Distance,Cargo,Aircraft):
    try:
        myconn=mys.connect(host='localhost',user="root",\
                           passwd="1234",database="adis")
        if myconn.is_connected():
            print("connection successful")
        mycur=myconn.cursor()
        query="insert into AMAS values \
                   ({},{},{},'{}','{}')".format(Sno,Passengers,Distance,Cargo,Aircraft)
        mycur.execute(query)
        myconn.commit()
        print("Aircraft Details saved")
        displayall()
   
    except Exception as e:
        print(e)


## Definition 2
def frmUpdate():
    def search():
        try:
            myconn=mys.connect(host='localhost',user="root",\
                         passwd="1234",database="adis")
            if myconn.is_connected():
                print("Connection Has Been Established With The Secure Server")
            mycur=myconn.cursor()
            rno=txtSno.get()
            query="select * from AMAS where Sno={}".format(rno)
            mycur.execute(query)
            print(query)
            rs=mycur.fetchone()
            print(rs)
            rs=list(rs)
            Sno=rs[0]
            Passengers=rs[1]
            Distance=rs[2]
            Cargo=rs[3]
            Aircraft=rs[4]
            s=" "
            print(Sno,Passengers,Distance,Cargo,Aircraft)
            if rs==None:
                messagebox.showinfo("No Such Aircraft is registered to AMAS")
            else:
                s+=str(Sno)+"\t"+str(Passengers)+"|\t"+str(Distance)+"|\t"+str(Cargo)+"|\t"+str(Aircraft)
                s+="\n"
                lbldisp=tk.Label(root, text =s )
                lbldisp.place(x=5,y=200)     
        except Exception as e:
            print(e)
    def clear():
        txtSno.delete(0,END)
        txtPassengers.delete(0,END)
        txtDistance.delete(0,END)
        txtCargo.delete(0,END)
        txtAircraft.delete(0,END)
       
       
    def submit():
        Sno=txtSno.get()
        Passengers=txtPassengers.get()
        Distance=txtDistance.get()
        Cargo=txtCargo.get()
        Aircraft=txtAircraft.get()
        print(Sno,Passengers,Distance,Cargo,Aircraft)
        update(Sno,Passengers,Distance,Cargo,Aircraft)
        
    def update(Sno,Passengers,Distance,Cargo,Aircraft):
        myconn=mys.connect(host='localhost',user='root',passwd='1234',database='adis')
        if myconn.is_connected():
            print('Connection successful')
        mycur=myconn.cursor()
        query="update AMAS set Passengers={},Distance={},Cargo='{}',Aircraft='{}' where Sno={}".format(Passengers,Distance,Cargo,Aircraft,Sno)
        mycur.execute(query)
        myconn.commit()
        print("AMAS Aircraft Database updated")
        displayall()
    
    def exe(value):
        global op
        op=aoption.get()
        if (op=='Search'):
            search()
        elif (op=='Update'):
            submit()
        elif (op=='Clear'):
            clear()
        elif (op=='Close'):
            root.destroy()      
    root = tk.Tk()
    root.geometry("300x200")
    root.title("DBMS Update Page")
    root.configure(bg='#272936')
    Label(root, bg ="cyan", height = 500, width = 600)
    lblSno = tk.Label(root, text ="Sno",bg='#272936',fg ='#bababa',font=("Calibri", 10) )
    lblSno.place(x = 50, y = 20)
    txtSno= tk.Entry(root, width = 35,bg='#414141',fg ='#bababa',font=("Calibri", 10))
    txtSno.place(x = 150, y = 20, width = 100)
    lblPassengers = tk.Label(root, text ="Passengers",bg='#272936',fg ='#bababa',font=("Calibri", 10))
    lblPassengers.place(x = 50, y = 50)
    txtPassengers = tk.Entry(root, width = 35,bg='#414141',fg ='#bababa',font=("Calibri", 10))
    txtPassengers.place(x = 150, y = 50, width = 100)
    lblDistance = tk.Label(root, text ="Distance",bg='#272936',fg ='#bababa',font=("Calibri", 10) )
    lblDistance.place(x = 50, y = 80)
    txtDistance= tk.Entry(root, width = 35,bg='#414141',fg ='#bababa',font=("Calibri", 10))
    txtDistance.place(x = 150, y = 80, width = 100)
    lblCargo = tk.Label(root, text ="Cargo",bg='#272936',fg ='#bababa',font=("Calibri", 10) )
    lblCargo.place(x = 50, y = 110)
    txtCargo= tk.Entry(root, width = 35,bg='#414141',fg ='#bababa',font=("Calibri", 10))
    txtCargo.place(x = 150, y = 110, width = 100)
    lblAircraft = tk.Label(root, text ="Aircraft",bg='#272936',fg ='#bababa',font=("Calibri", 10) )
    lblAircraft.place(x = 50, y = 140)
    txtAircraft= tk.Entry(root, width = 35,bg='#414141',fg ='#bababa',font=("Calibri", 10))
    txtAircraft.place(x = 150, y = 140, width = 100)
    
    OPTIONS = [
    "Select an option",
    "Search",
    "Update",
    "Clear"
    ] #etc
    aoption = StringVar(root)
    aoption.set(OPTIONS[0]) # default value
    OptionMenu(root, aoption, *OPTIONS,command=exe).grid(row=2,column=0,sticky=W)
    mainloop()
def Delete(Sno):
        try:
            myconn=mys.connect(host='localhost',user="root",\
                             passwd="1234",database="adis")
            if myconn.is_connected():
                print("connection successful")
            mycur=myconn.cursor()   
            query="Delete from AMAS where Sno={}".format(Sno)
            mycur.execute(query)
            myconn.commit()
            print("Records Deleted  Successfully..")
            displayall()
        except Exception as e:
            print(e)
            
## Definition 3
def frmDelete():
    def search(): 
        try:
            myconn=mys.connect(host='localhost',user="root",\
                         passwd="1234",database="adis")
            if myconn.is_connected():
                print("Connection Has Been Established With The Secure Server")
            mycur=myconn.cursor()
            sno=txtSno.get()
            query="select * from AMAS where Sno={}".format(sno)
            mycur.execute(query)
            print(query)
            rs=mycur.fetchone()
            print(rs)
            rs=list(rs)
            Sno=rs[0]
            Passengers=rs[1]
            Distance=rs[2]
            Cargo=rs[3]
            Aircraft=rs[4]
            s=" "
            s+=str(Sno)+"\t"+str(Passengers)+"|\t"+str(Distance)+"|\t"+Cargo+"\t"+Aircraft
            print(Sno,Passengers,Distance,Cargo,Aircraft)
            if rs==None:
                messagebox.showinfo("No Such Aircraft is registered to AMAS")
            else:
                
                messagebox.showinfo("Info", s)
                
        except Exception as e:
            print(e)
            
    
    def clear():
        txtSno.delete(0,END)
        txtPassengers.delete(0,END)
        txtDistance.delete(0,END)
        txtCargo.delete(0,END)
        txtAircraft.delete(0,END)       
    def submit():
        Sno=txtSno.get()
        Passengers=txtPassengers.get()
        Distance=txtDistance.get()
        Cargo=txtCargo.get()
        Aircraft=txtAircraft.get()
        print(Sno,Passengers,Distance,Cargo,Aircraft)
        Delete(Sno)
       
        
       
    root = tk.Tk()
    root.geometry("300x300")
    root.title("DBMS Delete Page")
    root.configure(bg='#272936')
    Label(root, bg ="cyan", height = 500, width = 600)
    lblSno = tk.Label(root, text ="Sno",bg='#272936',fg ='#bababa',font=("Calibri", 10) )
    lblSno.place(x = 50, y = 20)
    txtSno= tk.Entry(root, width = 35,bg='#414141',fg ='#bababa',font=("Calibri", 10))
    txtSno.place(x = 150, y = 20, width = 100)
    lblPassengers = tk.Label(root, text ="Passengers",bg='#272936',fg ='#bababa',font=("Calibri", 10))
    lblPassengers.place(x = 50, y = 50)
    txtPassengers = tk.Entry(root, width = 35,bg='#414141',fg ='#bababa',font=("Calibri", 10))
    txtPassengers.place(x = 150, y = 50, width = 100)
    lblDistance = tk.Label(root, text ="Distance",bg='#272936',fg ='#bababa',font=("Calibri", 10) )
    lblDistance.place(x = 50, y = 80)
    txtDistance= tk.Entry(root, width = 35,bg='#414141',fg ='#bababa',font=("Calibri", 10))
    txtDistance.place(x = 150, y = 80, width = 100)
    lblCargo = tk.Label(root, text ="Cargo",bg='#272936',fg ='#bababa',font=("Calibri", 10) )
    lblCargo.place(x = 50, y = 110)
    txtCargo= tk.Entry(root, width = 35,bg='#414141',fg ='#bababa',font=("Calibri", 10))
    txtCargo.place(x = 150, y = 110, width = 100)
    lblAircraft = tk.Label(root, text ="Aircraft",bg='#272936',fg ='#bababa',font=("Calibri", 10) )
    lblAircraft.place(x = 50, y = 140)
    txtAircraft= tk.Entry(root, width = 35,bg='#414141',fg ='#bababa',font=("Calibri", 10))
    txtAircraft.place(x = 150, y = 140, width = 100)
    btnclear = tk.Button(root, text ="Clear",
                    bg='#272936',fg ='#bababa',font=("Calibri", 10),command=clear)
    btnclear.place(x = 100, y = 170, width = 60)
    btndelete = tk.Button(root, text ="Delete",
                   bg='#272936',fg ='#bababa',font=("Calibri", 10),command=submit)
    btndelete.place(x = 200, y = 170, width = 60)
    btnsearch=tk.Button(root, text ="Search",
                    bg='#272936',fg ='#bababa',font=("Calibri", 10),command=search)
    btnsearch.place(x=150,y=210,width=60)
    
## Definition 4 
def displayall():
    try:        
        myconn=mys.connect(host='localhost',user="root",\
                           passwd="1234",database="adis")
        if myconn.is_connected():
            print("connection succssful")   
        mycur=myconn.cursor()
        mycur.execute("select * from AMAS")
        rs=mycur.fetchall()
        root = Tk()
        root.geometry("500x200")
        root.title("Display Page")
        root.configure(bg='#272936')
        frame = Frame(root)
        frame.pack()
        tree = ttk.Treeview(frame, columns = (1,2,3,4,5), height = 200, show = "headings")
        tree.pack(side = 'left')
        tree.heading(1, text="Sno")
        tree.heading(2, text="Passengers")
        tree.heading(3, text="Distance")
        tree.heading(4, text="Cargo")
        tree.heading(5, text="Aircraft")
        tree.column(1, width = 100)
        tree.column(2, width = 100)
        tree.column(3, width = 100)
        tree.column(4, width = 100)
        tree.column(5, width = 100)
            
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side = 'right', fill = 'y')        
        for val in rs:
            tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4]))
    except Exception as e:
        print(e)
    
## Definition 5
def Assign():
# TE  Text Entry
# TEfn  Text Entry Flight number
# TEp Text Entry Passengers
# TEa Text Entry Airport
# TEd Text Entry Distance
    def computing():
        print('dwindow is called')#TEMP
        def com():
            global fin
            global AC
            global Ep
            if fin==6500:
                def Next():
                    window=Toplevel()
                    window.title("Completed")
                    window.configure(background='white')
                    photo1=PhotoImage(file='320 2.gif')
                    Label(image=photo1) 
                    Label(window,image=photo1).grid(row=0,column=0,sticky=W)
                    Button(window,text='Exit',width=12,command=window.destroy).place(x='200',y='320')
                    mainloop()
                AC='The Airbus A320 Family'
                window=Toplevel()
                window.title("Computed")
                window.configure(background='white')
                photo1=PhotoImage(file='320 1.gif')
                Label(image=photo1) 
                Label(window,image=photo1).grid(row=0,column=0,sticky=W)
                Button(window,text='Assign',width=12,command=Next).place(x='200',y='320')
                mainloop()
            elif fin==9000 and Ep==0:
                def Next():
                    window=Toplevel()
                    window.title("Completed")
                    window.configure(background='white')
                    photo1=PhotoImage(file='777F 2.gif')
                    Label(image=photo1) 
                    Label(window,image=photo1).grid(row=0,column=0,sticky=W)
                    Button(window,text='Exit',width=12,command=window.destroy).place(x='200',y='320')
                    mainloop()
                AC='Boeing 777 Freighter'
                window=Toplevel()
                window.title("Computed")
                window.configure(background='white')
                photo1=PhotoImage(file='777F 1.gif')
                Label(image=photo1) 
                Label(window,image=photo1).grid(row=0,column=0,sticky=W)
                Button(window,text='Assign',width=12,command=Next).place(x='200',y='320')
                mainloop()
            elif fin==9000 and Ep!=0:
                def Next():
                    window=Toplevel()
                    window.title("Completed")
                    window.configure(background='white')
                    photo1=PhotoImage(file='787 2.gif')
                    Label(image=photo1) 
                    Label(window,image=photo1).grid(row=0,column=0,sticky=W)
                    Button(window,text='Exit',width=12,command=window.destroy).place(x='200',y='320')
                    mainloop()
                AC='Boeing 777 Freighter'
                window=Toplevel()
                window.title("Computed")
                window.configure(background='white')
                photo1=PhotoImage(file='787 1.gif')
                Label(image=photo1) 
                Label(window,image=photo1).grid(row=0,column=0,sticky=W)
                Button(window,text='Assign',width=12,command=Next).place(x='200',y='320')
                mainloop()
            elif fin==12700:
                def Next():
                    window=Toplevel()
                    window.title("Completed")
                    window.configure(background='white')
                    photo1=PhotoImage(file='380 2.gif')
                    Label(image=photo1) 
                    Label(window,image=photo1).grid(row=0,column=0,sticky=W)
                    Button(window,text='Exit',width=12,command=window.destroy).place(x='200',y='320')
                    mainloop()
                AC='Airbus A380'
                window=Toplevel()
                window.title("Computed")
                window.configure(background='white')
                photo1=PhotoImage(file='380 1.gif')
                Label(image=photo1) 
                Label(window,image=photo1).grid(row=0,column=0,sticky=W)
                Button(window,text='Assign',width=12,command=Next).place(x='200',y='320')
                mainloop()
            elif fin==11400:
                def Next():
                    window=Toplevel()
                    window.title("Completed")
                    window.configure(background='white')
                    photo1=PhotoImage(file='787 2.gif')
                    Label(image=photo1) 
                    Label(window,image=photo1).grid(row=0,column=0,sticky=W)
                    Button(window,text='Exit',width=12,command=window.destroy).place(x='200',y='320')
                    mainloop()
                AC='Boeing 787'
                window=Toplevel()
                window.title("Computed")
                window.configure(background='white')
                photo1=PhotoImage(file='787 1.gif')
                Label(image=photo1) 
                Label(window,image=photo1).grid(row=0,column=0,sticky=W)
                Button(window,text='Assign',width=12,command=Next).place(x='200',y='320')
                mainloop()
            elif fin==15900:
                def Next():
                    window=Toplevel()
                    window.title("Completed")
                    window.configure(background='white')
                    photo1=PhotoImage(file='777 2.gif')
                    Label(image=photo1) 
                    Label(window,image=photo1).grid(row=0,column=0,sticky=W)
                    Button(window,text='Exit',width=12,command=window.destroy).place(x='200',y='320')
                    mainloop()
                AC='Boeing 777'
                window=Toplevel()
                window.title("Computed")
                window.configure(background='white')
                photo1=PhotoImage(file='777 1.gif')
                Label(image=photo1) 
                Label(window,image=photo1).grid(row=0,column=0,sticky=W)
                Button(window,text='Assign',width=12,command=Next).place(x='200',y='320')
                mainloop()
                
            #results()                   # Window Number 6 is called  
        window=Toplevel()
        window.title("Computing")
        window.configure(background='white')
        photo1=PhotoImage(file='AMAS.gif')
        Label(image=photo1)
        Label(window,image=photo1,bg='white').grid(row=0,column=0,sticky=W)
        Label(window,text='Start The Service',bg='white',fg='black',font='none 12 bold').grid(row=1,column=0,sticky=W)
        Button(window,text='Compute',width=6,command=com).grid(row=3,column=0,sticky=W)
        mainloop()
        #toplevel.destroy()
        
    def dwindow():
        print('dwindow is called')
        def saveTEd():
            try:
                global Ed
                Ed=TEd.get()
                myconn=mys.connect(host='localhost',user="root",\
                               passwd="1234",database="adis")
                sql_select_Query = "select * from AMAS"
                cursor = myconn.cursor()
                cursor.execute(sql_select_Query)
                records = cursor.fetchall()
                print("Total number of rows in AMAS is: ", cursor.rowcount)

                print("\nPrinting each AMAS record")
                distance=int(Ed)
                com=[]
                for row in records:
                    com.append(row[2])    
                print(com)
                global fin
                fin=min(com, key=lambda x:abs(x-distance))
                print(fin)
            except Error as e:
                print("Error reading data from MySQL table", e)
            finally:
                if (myconn.is_connected()):
                    myconn.close()
                    cursor.close()
                    print("MySQL connection is closed")
            computing() # Window Number 5 is called Below
        window=Toplevel()
        window.title("Distance")
        window.configure(background='white')
        photo1=PhotoImage(file='Distance.gif')
        Label(image=photo1)
        Label(window,image=photo1,bg='white').grid(row=0,column=0,sticky=W)
        Label(window,text='Enter The Distance Travelled',bg='white',fg='black',font='none 12 bold').grid(row=1,column=0,sticky=W)
        TEd=Entry(window,width=20,bg='white')
        TEd.grid(row=2,column=0,sticky=W)
        Button(window,text='Enter',width=6,command=saveTEd).grid(row=3,column=0,sticky=W)
        mainloop()

    def awindow():
        print('awindow is called')
        def saveDDMo(value):
            global DDMo
            DDMo=aoption.get()
            print(DDMo)
            window.destroy()
            dwindow() # Window Number 4 is called 
        window=Toplevel()
        window.title("Destination Airport")
        window.configure(background='white')
        photo1=PhotoImage(file='airport.gif')
        Label(image=photo1)
        Label(window,image=photo1,bg='white').grid(row=0,column=0,sticky=W)
        Label(window,text='Enter The Destination',bg='white',fg='black',font='none 12 bold').grid(row=1,column=0,sticky=W)
        OPTIONS = ['Select an option','BNE','MEL','SYD','BAH','BRU','YYZ','PEK','PVG','CAI','MUC','ATH','AMD','BLR','DEL','COK','CCU','CCJ','BOM','TRV','CGK','NBO','KWI','LHR','MAN','ORG','LAX','JFK','DCA']
        aoption = StringVar(window)
        aoption.set(OPTIONS[0]) # default value
        OptionMenu(window, aoption, *OPTIONS,command=saveDDMo).grid(row=2,column=0,sticky=W)
        mainloop()
       


    def pwindow():
        print('pwindow is called')
        def saveTEp():
            global Ep
            Ep=TEp.get()
            print(Ep)
            window.destroy()
            awindow() # Window Number 3 is called.
        window=Toplevel()
        window.title("Passengers")
        window.configure(background='white')
        photo1=PhotoImage(file='passengers.gif')
        Label(image=photo1)
        Label(window,image=photo1,bg='white').grid(row=0,column=0,sticky=W)
        Label(window,text='Enter The Number Of Passengers',bg='white',fg='black',font='none 12 bold').grid(row=1,column=0,sticky=W)
        TEp=Entry(window,width=20,bg='white')
        TEp.grid(row=2,column=0,sticky=W)
        Button(window,text='Enter',width=6,command=saveTEp).grid(row=3,column=0,sticky=W)
        mainloop()
    def fnwindow():
        def saveTEfn():
            global Efn
            Efn=TEfn.get()
            print(Efn)
            window.destroy()
            pwindow() # Window Number 2 is called. 
        window=Toplevel()
        window.title("Flight Number")
        window.configure(background='white')
        photo1=PhotoImage(file='flightnumber.gif')
        Label(image=photo1)
        Label(window,image=photo1,bg='white').grid(row=0,column=0,sticky=W)
        Label(window,text='Enter the Flight Number',background='white',foreground='black',font='none 12 bold').grid(row=1,column=0,sticky=W)
        TEfn=Entry(window,width=20,bg='white')
        TEfn.grid(row=2,column=0,sticky=W)
        Button(window,text='Enter',width=6,command=saveTEfn).grid(row=3,column=0,sticky=W)
        mainloop()
    fnwindow()  # Window Number 1 is called.
#__________________________________________________________________________________________________
# Functions
def Intro():
    def itsloading():
        root1 = Tk()
        root1.title('Initialize')
        root1.configure(bg='#272936')
        progress = Progressbar(root1, orient = HORIZONTAL,length = 600, mode = 'indeterminate') 
        def bar(): 
            import time
            progress['value'] = 0
            root1.update_idletasks() 
            time.sleep(0.5)
            
            progress['value'] = 20
            root1.update_idletasks() 
            time.sleep(0.5) 
          
            progress['value'] = 40
            root1.update_idletasks() 
            time.sleep(0.5) 
          
            progress['value'] = 50
            root1.update_idletasks() 
            time.sleep(0.5) 
          
            progress['value'] = 60
            root1.update_idletasks() 
            time.sleep(0.5) 
          
            progress['value'] = 80
            root1.update_idletasks() 
            time.sleep(0.5)
            
            progress['value'] = 100
            root1.update_idletasks() 
            time.sleep(0.5)
            
            root1.destroy()
            window.destroy()
            
        progress.pack(pady = 4) 
        Button(root1, text = 'Initialize', command = bar).pack(pady = 10) 
    window=Tk()
    window.title("Start Program")
    window.configure(background='white')
    photo1=PhotoImage(file='AMAS.gif')
    Label(image=photo1) 
    Label(window,image=photo1).grid(row=0,column=0,sticky=W)
    Label(compound='center')
    Button(window,text='Start Program',width=12,command=itsloading).place(x='200',y='320')
    mainloop()
    
def stopwatch(seconds):
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print("loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed)) 
        time.sleep(1)
        
def displayimage():
    Initimage=Tk()
    Initimage.title('Initializing')
    photo1=PhotoImage(file='AMAS.gif')
    Label(Initimage,image=photo1,fg='black',bg='black').grid(row=0,column=0,sticky=E)
    button = Button (Initimage,text ="Start",command=Initimage.destroy).grid(row=0,column=0,sticky=S)
    Initimage.resizable(0,0)
    Initimage.mainloop()
    
def menu():
    root = tk.Tk() 
    root.geometry("600x500") 
    root.title("DBMS Menu Page")
    root.configure(bg='#272936')
    Label(root, bg='#272936', height = 240, width = 300)
    btninsert = tk.Button(root, text ="Insert", 
                    bg='#272936',fg="#bababa",font=("Calibri", 20),command=frmInsert) 
    btninsert.place(x=240, y = 100, width = 140)
    btnupdate = tk.Button(root, text ="Update", 
                    bg='#272936',fg="#bababa",font=("Calibri", 20),command=frmUpdate) 
    btnupdate.place(x=240, y = 175, width = 140)
    btnassign = tk.Button(root, text ="Assign", 
                    bg='#272936',fg="white",font=("Calibri Bold", 20),command=Assign) 
    btnassign.place(x=240, y = 250, width = 140)
    btndisplay = tk.Button(root, text ="Display", 
                    bg='#272936',fg="#bababa",font=("Calibri", 20),command=displayall) 
    btndisplay.place(x=240, y = 325, width = 140)
    btndelete = tk.Button(root,text='Delete',
                    bg='#272936',fg="#bababa",font=('Calibri', 20),command=frmDelete)
    btndelete.place(x=240,y=400, width= 140)
    
def clearlogin():
    txtUser.delete(0,END)
    txtpass.delete(0,END)
 
def submitact(): 
    user = txtUser.get() 
    passw = txtpass.get() 
    print(f"The ID-pw entered by you is {user} {passw}") 
    logintodb(user, passw)
    
def logintodb(user, passw):
    if passw: 
        db = mys.connect(host ="localhost", 
                                    user = user, 
                                    password = passw, 
                                    db ="adis") 
        cursor = db.cursor() 
    else: 
        db = mys.connect(host ="localhost", 
                                    user = root, 
                                    database ="adis") 
        cursor = db.cursor()       
#A Table in the database       
    savequery = "show tables" 
    try: 
        cursor.execute(savequery) 
        myresult = cursor.fetchall() 
        print("Query Excecuted succesfully")
        messagebox.showinfo("Login ", "Login Successful")    
    except: 
        db.rollback() 
        print("Error occured")
    menu()
#__________________________________________________________________________________________________
# Main program
Intro()
root = tk.Tk() 
root.geometry("300x300") 
root.title("DBMS Login Page")
root.configure(bg='#272936')
lbluser = tk.Label(root, text ="Username",bg='#272936',fg="#bababa",font=("Calibri", 11) ) 
lbluser.place(x = 50, y = 20) 
txtUser = tk.Entry(root, width = 35,bg='#414141',fg="#bababa",font=("Calibri", 11)) 
txtUser.place(x = 150, y = 20, width = 100) 
lblpass = tk.Label(root, text ="Password",bg='#272936',fg="#bababa",font=("Calibri", 11)) 
lblpass.place(x = 50, y = 50) 
txtpass = tk.Entry(root,show="*", width = 35,bg='#414141',fg="#bababa",font=("Calibri", 11)) 
txtpass.place(x = 150, y = 50, width = 100) 
 
submitbtn = tk.Button(root, text ="Login", 
                    bg='#272936',fg ='#bababa', font=("Calibri", 11),command = submitact) 
submitbtn.place(x = 100, y = 135, width = 55)
clearbtn = tk.Button(root, text ="Clear", 
                    bg='#272936',fg ='#bababa', font=("Calibri", 11),command = clearlogin) 
clearbtn.place(x = 200, y = 135, width = 55)
root.mainloop()