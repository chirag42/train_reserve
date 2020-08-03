from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import random
import requests as HTTP
import webbrowser
import re
import smtplib
from tkinter import messagebox as ms
root=Tk()
root.title("Reservation System")
root.wm_iconbitmap('y.ico')
flg=0
otpver=StringVar()
login_usr=StringVar()
login_password=StringVar()
EMAIL=StringVar()
PHONE=StringVar()
val1=StringVar()
val2=StringVar()
signup_name=StringVar()
signup_username=StringVar()
signup_password=StringVar()
signup_phone=StringVar()
signup_email=StringVar()
r_train=StringVar()
r_from=StringVar()
r_to=StringVar()
r_n1=StringVar()
r_n2=StringVar()
r_n3=StringVar()
r_n4=StringVar()
r_date=StringVar()
r_var=IntVar()
r_var1=IntVar()
r_var2=IntVar()
r_var3=IntVar()
r_age1=IntVar()
r_age2=IntVar()
r_age3=IntVar()
r_age4=IntVar()
#OTP VERIFICATION

    

def payment():
    def verification():
        top7.destroy()
        import random
        trn=r_train.get()
        usr=login_usr.get()
        date=r_date.get()
        frm=r_from.get()
        print(frm)
        to=r_to.get()
        print(to)
        n1=r_n1.get()
        n1=n1.upper()
        n2=r_n2.get()
        n2=n2.upper()
        n3=r_n3.get()
        n3=n3.upper()
        n4=r_n4.get()
        n4=n4.upper()
        age1=r_age1.get()
        age2=r_age2.get()
        age3=r_age3.get()
        age4=r_age4.get()
        v=r_var.get()
        v1=r_var1.get()
        v2=r_var2.get()
        v3=r_var3.get()
        from email.mime.text import MIMEText

        n= random.randint(1000,10000)
        
        body=""""Dear Customer,
                 Your one time password for payment is
        """ + str(n)
        msg=MIMEText(body)
        fromaddr="railwaybookingapp@gmail.com"
        toaddr="chiragnagpal39@gmail.com"
        
        msg['From']=fromaddr
        msg['To']=toaddr
        msg['subject']="OTP"
        server=smtplib.SMTP('smtp.gmail.com',587)
        
        server.starttls()
        
        server.login(fromaddr,"gulandas77!")
        
        server.send_message(msg)
        print('Mail sent....')
        
        server.quit()
        def last_mssg():
            print(otpver.get())
            if str(otpver.get())==str(n):
                ms.showinfo("success","payment sucessful")
                conn5=sqlite3.connect('login.db')
                with conn5:
                    cursor=conn5.cursor()
                def generate_pnr():
                    pnr=random.randint(80000,99999)
                    find_pnr=('SELECT * FROM booking1 WHERE PNR = ? ')
                    cursor.execute(find_pnr,[(pnr)])
                    if (find_pnr!=pnr):
                        print(pnr)
                        return pnr
                p=generate_pnr()
                p=str(p)
                print(p)
                
                cursor.execute('CREATE TABLE IF NOT EXISTS booking1 (USERNAME TEXT,PNR TEXT,TRAIN_NO TEXT,NAME TEXT,FROM_STAT TEXT,TO_STAT TEXT,DOJ TEXT,GENDER INT ,AGE INT)')
                if(n1!=''):
                    cursor.execute('INSERT INTO booking1 (USERNAME,PNR,TRAIN_NO,NAME,FROM_STAT,TO_STAT,DOJ,GENDER,AGE) VALUES(?,?,?,?,?,?,?,?,?)',(usr,p,trn,n1,frm,to,date,v,age1))
                    conn5.commit()
                if(n2!=''):
                    cursor.execute('INSERT INTO booking1 (USERNAME,PNR,TRAIN_NO,NAME,FROM_STAT,TO_STAT,DOJ,GENDER,AGE) VALUES(?,?,?,?,?,?,?,?,?)',(usr,p,trn,n2,frm,to,date,v1,age2))
                    conn5.commit()
                if(n3!=''):
                    cursor.execute('INSERT INTO booking1 (USERNAME,PNR,TRAIN_NO,NAME,FROM_STAT,TO_STAT,DOJ,GENDER,AGE) VALUES(?,?,?,?,?,?,?,?,?)',(usr,p,trn,n3,frm,to,date,v2,age3))
                    conn5.commit()
                if(n3!=''):
                    cursor.execute('INSERT INTO booking1 (USERNAME,PNR,TRAIN_NO,NAME,FROM_STAT,TO_STAT,DOJ,GENDER,AGE) VALUES(?,?,?,?,?,?,?,?,?)',(usr,p,trn,n4,frm,to,date,v3,age4))
                    conn5.commit()
                find=('SELECT * FROM booking1 WHERE USERNAME=? AND PNR = ? ')
                cursor.execute(find,[(usr),(p)])
                fetch=cursor.fetchall()
                conn5.close()
                
                from email.mime.text import MIMEText
                body=""""Dear Customer,
                Your is ticket  booked. PLEASE CARRY YOUR ID(AADHAR CARD, PAN CARD, etc.) AS A PROOF OF YOUR DETAILS. 
                your pnr is :""" +str(p)
                msg=MIMEText(body)
                fromaddr="railwaybookingapp@gmail.com"
                toaddr="chiragnagpal39@gmail.com"
                msg['From']=fromaddr
                msg['To']=toaddr
                msg['subject']="TICKET CONFIRMATION"
                body1=""""Dear Customer,
                Your is ticket  booked. PLEASE CARRY YOUR ID(AADHAR CARD, PAN CARD, etc.) AS A PROOF OF YOUR DETAILS. 
                details are:[username,pnr,train no.,name, from station, to stataion, date of journey, gender,age]
                """ + str(fetch)
                msg1=MIMEText(body1)
                fromaddr="railwaybookingapp@gmail.com"
                toaddr="chiragnagpal39@gmail.com"
                msg1['From']=fromaddr
                msg1['To']=toaddr
                msg1['subject']="TICKET CONFIRMATION"
                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(fromaddr,"gulandas77!")
                server.send_message(msg1)
                
                print('Mail sent....')
                
                server.quit()
                top8.destroy()
                login()
                
            else:
                ms.showerror("sorry!","wrong otp")
                top8.destroy()
                user_details()
        top8=Toplevel(width=2000,height=2000)
        img=ImageTk.PhotoImage(Image.open("payment.jpg"))
        l1= Label(top8,image=img)
        l1.image=img
        l1.place(x=0, y=0, relwidth=1, relheight=1)
        
        l2=Label(top8,text="Enter One Time Password: ",width=35,height=1,font=('Arial',-25,'bold'))
        l2.place(x=200,y=200)
        
        e1=Entry(top8,width=8,bg="white",textvar=otpver,font=('Courier',-27,'bold'))
        e1.place(x=750,y=200)
        b11=Button(top8,text="Submit",width=20,height=1,bg="azure",fg="black",activebackground="white",activeforeground="black",font=('Arial','-15','bold'),command=last_mssg)
        b11.place(x=500,y=350)
    top7=Toplevel(width=2000,height=2000)

    img=ImageTk.PhotoImage(Image.open("payment.jpg"))
    l1= Label(top7,image=img)
    l1.image=img
    l1.place(x=0, y=0, relwidth=1, relheight=1)
    
    l2=Label(top7,text="Checkout",width=20,height=1,bg="azure",fg="black",font=('Arial',-27,'bold',"underline"))
    l2.place(x=550,y=100)
    
    l3=Label(top7,text="Name On Card",width=20,height=1,bg="azure",fg="black",font=('Arial',-20,'bold'))
    l3.place(x=300,y=200)
    
    e1=Entry(top7,width=45,bg="white",font=('Courier',-27,'bold'))
    e1.place(x=300,y=235)
    
    l3=Label(top7,text="Card Number",width=15,height=1,bg="azure",fg="black",font=('Arial',-20,'bold'))
    l3.place(x=300,y=282)
    
    e2=Entry(top7,width=20,bg="white",font=('Courier',-27,'bold'))
    e2.place(x=300,y=320)
    
    l3=Label(top7,text="Expiry date",width=20,height=1,bg="azure",fg="black",font=('Arial',-20,'bold'))
    l3.place(x=680,y=320)
    
    e2=Entry(top7,width=10,bg="white",font=('Courier',-27,'bold'))
    e2.place(x=950,y=320)
    
    
    l4=Label(top7,text="CVV",width=5,height=1,bg="azure",fg="black",font=('Arial',-20,'bold'))
    l4.place(x=300,y=380)
    
    e2=Entry(top7,width=5,bg="white",font=('Courier',-27,'bold'),show="*")
    e2.place(x=400,y=380)
    
    
    b9=Button(top7,text="Submit",width=10,height=1,bg="azure",fg="black",activebackground="white",activeforeground="black",font=('Arial','-15','bold'),command=verification)
    b9.place(x=300,y=550)
    
    b10=Button(top7,text="Back",width=10,height=1,bg="azure",fg="black",activebackground="white",activeforeground="black",font=('Arial','-15','bold'),command=top7.destroy)
    b10.place(x=100,y=10)
    
    
    
def user_details():
    def cancel():
        trn=r_train.get()
        usr=login_usr.get()
        date=r_date.get()
        frm=r_from.get()
        to=r_to.get()
        n1=r_n1.get()
        n1=n1.upper()
        n2=r_n2.get()
        n2=n2.upper()
        n3=r_n3.get()
        n3=n3.upper()
        n4=r_n4.get()
        n4=n4.upper()
        age1=r_age1.get()
        age2=r_age2.get()
        age3=r_age3.get()
        age4=r_age4.get()
        v=r_var.get()
        v1=r_var1.get()
        v2=r_var2.get()
        v3=r_var3.get()
        z=input("enter your pnr:")
        conn9 = sqlite3.connect('login.db')
        with conn9:
            cursor=conn9.cursor()
        res1 = ('SELECT * FROM booking1 WHERE PNR = ? AND NAME=? AND FROM_STAT=? AND TO_STAT=? AND DOJ=?')
        cursor.execute(res1,[(z),(n1),(frm),(to),(date)])
        result1 = cursor.fetchall()
        res2 = ('SELECT * FROM booking1 WHERE PNR = ? AND NAME=? AND FROM_STAT=? AND TO_STAT=? AND DOJ=?')
        cursor.execute(res2,[(z),(n2),(frm),(to),(date)])
        result2 = cursor.fetchall()
        res3 = ('SELECT * FROM booking1 WHERE PNR = ? AND NAME=? AND FROM_STAT=? AND TO_STAT=? AND DOJ=?')
        cursor.execute(res3,[(z),(n3),(frm),(to),(date)])
        result3 = cursor.fetchall()
        res4 = ('SELECT * FROM booking1 WHERE PNR = ? AND NAME=? AND FROM_STAT=? AND TO_STAT=? AND DOJ=?')
        cursor.execute(res4,[(z),(n4),(frm),(to),(date)])
        result4 = cursor.fetchall()
        if(result1):
            cursor.execute('DELETE FROM booking1 WHERE PNR=? AND NAME=? AND FROM_STAT=? AND TO_STAT=? AND DOJ=?', (z,n1,frm,to,date))
            warn151=Label(top6,text="TICKET CANCELLED",width=50,height=2,font=("bold",15),bg="black",fg="green")
            warn151.place(x=920,y=290)
        elif(n1!=''):
            warn155=Label(top6,text="RECORD NOT FOUND[RECHECK ENTERIES]",width=50,height=1,font=("bold",15),bg="black",fg="green")
            warn155.place(x=920,y=290)
        if(result2):
            cursor.execute('DELETE FROM booking1 WHERE PNR=? AND NAME=? AND FROM_STAT=? AND TO_STAT=? AND DOJ=?', (z,n2,frm,to,date))
            warn152=Label(top6,text="TICKET CANCELLED",width=50,height=2,font=("bold",15),bg="black",fg="green")
            warn152.place(x=920,y=350)
        elif(n2!=''):
            warn156=Label(top6,text="RECORD NOT FOUND[RECHECK ENTERIES]",width=50,height=1,font=("bold",15),bg="black",fg="green")
            warn156.place(x=920,y=350)
        if(result3):
            cursor.execute('DELETE FROM booking1 WHERE PNR=? AND NAME=? AND FROM_STAT=? AND TO_STAT=? AND DOJ=?', (z,n3,frm,to,date))
            warn153=Label(top6,text="TICKET CANCELLED",width=50,height=2,font=("bold",15),bg="black",fg="green")
            warn153.place(x=920,y=410)
        elif(n3!=''):
            warn157=Label(top6,text="RECORD NOT FOUND[RECHECK ENTERIES]",width=50,height=1,font=("bold",15),bg="black",fg="green")
            warn157.place(x=920,y=410)
        if(result4):
            cursor.execute('DELETE FROM booking1 WHERE PNR=? AND NAME=? AND FROM_STAT=? AND TO_STAT=? AND DOJ=?', (z,n4,frm,to,date))
            warn154=Label(top6,text="TICKET CANCELLED",width=50,height=2,font=("bold",15),bg="black",fg="green")
            warn154.place(x=920,y=470)
        elif(n4!=''):
            warn158=Label(top6,text="RECORD NOT FOUND[RECHECK ENTERIES]",width=50,height=1,font=("bold",15),bg="black",fg="green")
            warn158.place(x=920,y=470)
        
        conn9.commit()
        conn9.close()
        from email.mime.text import MIMEText
        body=""""Dear Customer,
        Your is ticket  cancelled. 
        """ 
        msg=MIMEText(body)
        fromaddr="railwaybookingapp@gmail.com"
        toaddr="chiragnagpal39@gmail.com"
                
        msg['From']=fromaddr
        msg['To']=toaddr
        msg['subject']="TICKET CANCELLED"
        server=smtplib.SMTP('smtp.gmail.com',587)
                
        server.starttls()
                
        server.login(fromaddr,"gulandas77!")
                
        server.send_message(msg)
        print('Mail sent....')
        
        server.quit()
    def booking():
        trn=r_train.get()
        usr=login_usr.get()
        date=r_date.get()
        frm=r_from.get()
        to=r_to.get()
        n1=r_n1.get()
        n2=r_n2.get()
        n3=r_n3.get()
        n4=r_n4.get()
        age1=r_age1.get()
        age2=r_age2.get()
        age3=r_age3.get()
        age4=r_age4.get()
        v=r_var.get()
        v1=r_var1.get()
        v2=r_var2.get()
        v3=r_var3.get()
        total=5
        conn7=sqlite3.connect('login.db')
        with conn7:
            cursor=conn7.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS booking1 (USERNAME TEXT,PNR TEXT,TRAIN_NO TEXT,NAME TEXT,FROM_STAT TEXT,TO_STAT TEXT,DOJ TEXT,GENDER INT ,AGE INT)')
        cursor.execute("SELECT * from booking1")
        results = cursor.fetchall()
        rem=total-len(results)
        if(rem<4 and n1!='' and n2!='' and n3!='' and n4!=''):
            warn1=Label(top6,text="SEAT NOT AVAILABLE FOR ALL PASSENGERS\nTOTAL AVAILABLE SEATS ARE:",width=50,height=2,font=("bold",15),bg="black",fg="green")
            warn1.place(x=920,y=290)
            warn2=Label(top6,text=rem,width=50,height=1,font=("bold",15),bg="black",fg="green")
            warn2.place(x=920,y=350)
            return
        if(rem<3 and n1!='' and n2!='' and n3!=''):
            warn1=Label(top6,text="SEAT NOT AVAILABLE FOR ALL PASSENGERS\nTOTAL AVAILABLE SEATS ARE:",width=50,height=2,font=("bold",15),bg="black",fg="green")
            warn1.place(x=920,y=290)
            warn2=Label(top6,text=rem,width=50,height=1,font=("bold",15),bg="black",fg="green")
            warn2.place(x=920,y=350)
            return
        if(rem<2 and n1!='' and n2!=''):
            warn1=Label(top6,text="SEAT NOT AVAILABLE FOR ALL PASSENGERS\nTOTAL AVAILABLE SEATS ARE:",width=50,height=2,font=("bold",15),bg="black",fg="green")
            warn1.place(x=920,y=290)
            warn2=Label(top6,text=rem,width=50,height=1,font=("bold",15),bg="black",fg="green")
            warn2.place(x=920,y=350)
            return
        if(rem<1 and n1!=''):
            warn1=Label(top6,text="SEAT NOT AVAILABLE FOR ALL PASSENGERS\nTOTAL AVAILABLE SEATS ARE:",width=50,height=2,font=("bold",15),bg="black",fg="green")
            warn1.place(x=920,y=290)
            warn2=Label(top6,text=rem,width=50,height=1,font=("bold",15),bg="black",fg="green")
            warn2.place(x=920,y=350)
            return
        if (trn=='' ):
            warn11=Label(top6,text="BLANK ENTRY FIELDS",width=50,height=2,font=("bold",15),bg="black",fg="green")
            warn11.place(x=100,y=700)
        
        elif(frm==to):
            warn12=Label(top6,text="SAME STATION",width=50,height=2,font=("bold",15),bg="black",fg="green")
            warn12.place(x=800,y=100)
        elif(n1==''):
            warn15=Label(top6,text="BLANK ENTRY FIELDS",width=50,height=2,font=("bold",15),bg="black",fg="green")
            warn15.place(x=100,y=700)
        else:
            payment()
            
            
    
    top6=Toplevel(width=2000,height=2000)
    
    img=ImageTk.PhotoImage(Image.open("new.jpg"))
    l1= Label(top6,image=img)
    l1.image=img
    l1.place(x=0, y=0, relwidth=1, relheight=1)
    
    l2=Label(top6,text="ENTER TRAIN NO:",width=20,height=1,font=('Arial',-21,'bold'))
    l2.place(x=100,y=50)
    
    e1=Entry(top6,bd=3,width=15,textvar=r_train,font=('Courier',-20,'bold'),fg="black",bg="white")    
    e1.place(x=420,y=50)
    
    l3=Label(top6,text="DATE OF JOURNEY:",width=20,height=1,font=('Arial',-21,'bold'))
    l3.place(x=100,y=90)
    
    e2=Entry(top6,bd=3,width=15,textvar=r_date,font=('Courier',-20,'bold'),fg="black",bg="white")    
    e2.place(x=420,y=90)
    
    s2=Spinbox(top6,bd=3,textvar=r_from,values=("DELHI","MUMBAI CENTRAL","MUMBAI(CSMT)","DADAR(CR)","PUNE","KOLKATA","CHENNAI","NAGPUR","SOLAPUR"),bg="white",fg="black",font=('Arial',-21,'bold'),width=25)
    s3=Spinbox(top6,bd=3,textvar=r_to,values=("DELHI","MUMBAI CENTRAL","MUMBAI(CSMT)","DADAR(CR)","PUNE","KOLKATA","CHENNAI","NAGPUR","SOLAPUR"),bg="white",fg="black",font=('Arial',-21,'bold'),width=25)
    
    text1=Text(top6,font=('Courier',-22,'bold'),width=20,height=1,fg="black",bg="grey95")
    text1.insert(END,'FROM STATION')
    text1.place(x=100,y=130)
    
    
    text2=Text(top6,font=('Courier',-22,'bold'),width=20,height=1,fg="black",bg="grey95")
    text2.insert(END,'TO STATION')
    text2.place(x=100,y=180)
    
    
    s2.place(x=420,y=130)
    s3.place(x=420,y=180)
    
    
    l4=Label(top6,text="SR NO",width=8,height=1,font=('Arial',-19,'bold'))
    l4.place(x=100,y=230)
    l5=Label(top6,text="NAME",width=27,height=1,font=('Arial',-19,'bold'))
    l5.place(x=250,y=230)
    l6=Label(top6,text="M/F",width=7,height=1,font=('Arial',-19,'bold'))
    l6.place(x=630,y=230)
    l7=Label(top6,text="AGE",width=8,height=1,font=('Arial',-19,'bold'))
    l7.place(x=800,y=230)
    

	
    l8=Label(top6,text="1",width=5,height=1,font=('Arial',-21,'bold'))
    l8.place(x=100,y=290)
    l9=Label(top6,text="2",width=5,height=1,font=('Arial',-21,'bold'))
    l9.place(x=100,y=350)
    l10=Label(top6,text="3",width=5,height=1,font=('Arial',-21,'bold'))
    l10.place(x=100,y=410)
    l11=Label(top6,text="4",width=5,height=1,font=('Arial',-21,'bold'))
    l11.place(x=100,y=470)
    
	
	
    e2=Entry(top6,bd=3,width=27,textvar=r_n1,font=('Courier',-20,'bold'),fg="black",bg="white")    
    e2.place(x=250,y=290)
    e3=Entry(top6,bd=3,width=27,textvar=r_n2,font=('Courier',-20,'bold'),fg="black",bg="white")    
    e3.place(x=250,y=350)
    e4=Entry(top6,bd=3,width=27,textvar=r_n3,font=('Courier',-20,'bold'),fg="black",bg="white")    
    e4.place(x=250,y=410)
    e5=Entry(top6,bd=3,width=27,textvar=r_n4,font=('Courier',-20,'bold'),fg="black",bg="white")    
    e5.place(x=250,y=470)
    
    
    r1=Radiobutton(top6,text="Male",fg="black",bg="white",variable=r_var,value=1,font=('Georgia',-15,"italic"))
    r2=Radiobutton(top6,text="Female",fg="black",bg="white",variable=r_var,value=2,font=('Georgia',-15,"italic"))
    
    r1.place(x=630,y=290)
    r2.place(x=700,y=290)
    
    r3=Radiobutton(top6,text="Male",fg="black",bg="white",variable=r_var1,value=1,font=('Georgia',-15,"italic"))
    r4=Radiobutton(top6,text="Female",fg="black",bg="white",variable=r_var1,value=2,font=('Georgia',-15,"italic"))
    
	
    r3.place(x=630,y=350)
    r4.place(x=700,y=350)
	
    r5=Radiobutton(top6,text="Male",fg="black",bg="white",variable=r_var2,value=1,font=('Georgia',-15,"italic"))
    r6=Radiobutton(top6,text="Female",fg="black",bg="white",variable=r_var2,value=2,font=('Georgia',-15,"italic"))
    
    r5.place(x=630,y=410)
    r6.place(x=700,y=410)
    
    r7=Radiobutton(top6,text="Male",fg="black",bg="white",variable=r_var3,value=1,font=('Georgia',-15,"italic"))
    r8=Radiobutton(top6,text="Female",fg="black",bg="white",variable=r_var3,value=2,font=('Georgia',-15,"italic"))
    
    r7.place(x=630,y=470)
    r8.place(x=700,y=470)
    
    e6=Entry(top6,bd=3,width=8,textvar=r_age1,font=('Courier',-20,'bold'),fg="black",bg="white")    
    e6.place(x=800,y=290)
    
    e7=Entry(top6,bd=3,width=8,textvar=r_age2,font=('Courier',-20,'bold'),fg="black",bg="white")    
    e7.place(x=800,y=350)
    
    e8=Entry(top6,bd=3,width=8,textvar=r_age3,font=('Courier',-20,'bold'),fg="black",bg="white")    
    e8.place(x=800,y=410)
    
    e9=Entry(top6,bd=3,width=8,textvar=r_age4,font=('Courier',-20,'bold'),fg="black",bg="white")    
    e9.place(x=800,y=470)
    
	
    b1=Button(top6,text="Reservation",width=20,height=1,bg="azure",fg="black",activebackground="white",activeforeground="black",font=('Arial','-20','bold'),command=booking)
    b1.place(x=250,y=630)

    b2=Button(top6,text="Cancellation",width=20,height=1,bg="azure",fg="black",activebackground="white",activeforeground="black",font=('Arial','-20','bold'),command=cancel)
    b2.place(x=570,y=630)
    
    b3=Button(top6,text="Back",width=10,height=1,bg="white",fg="black",activebackground="white",activeforeground="black",font=('Arial','-13','bold'),command=top6.destroy)
    b3.place(x=10,y=15)
    
    
    
    
        
# COMPLAINT    

def complain():
    
    top5=Toplevel(width=2000,height=2000)
    
    def mssg():
        
        import smtplib
        from email.mime.text import MIMEText
        
        body=""""Dear Customer,
         
        Thank you for writing to Railway  Support.
         
        This is with reference to your complain, we have registered your complain and as soon as we get 
        solution we will get back to you.
         
        
        We appreciate your patience in the interim."""
        
        msg=MIMEText(body)
        fromaddr="railwaybookingapp@gmail.com"
        toaddr="chiragnagpal39@gmail.com"
        msg['From']=fromaddr
        msg['To']=toaddr
        msg['subject']="Complain Registration"
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(fromaddr,"gulandas77!")
        server.send_message(msg)
        server.quit()


        
    
    img=ImageTk.PhotoImage(Image.open("feed.jpg"))
    l1= Label(top5,image=img)
    l1.image=img
    l1.place(x=0, y=0, relwidth=1, relheight=1)
    
    l2=Label(top5,text="Please Enter Here: ",width=25,height=1,font=('Courier',-14,'bold'))
    l2.place(x=550,y=20)
    text = Text(top5)
    text.place(x=800,y=2)    

    
    
    
    b9=Button(top5,text="Submit",width=10,height=1,bg="azure",fg="black",activebackground="white",activeforeground="black",font=('Arial','-15','bold'),command=mssg)
    b9.place(x=800,y=600)
    b10=Button(top5,text="Back",width=10,height=1,bg="azure",fg="black",activebackground="white",activeforeground="black",font=('Arial','-15','bold'),command=top5.destroy)
    b10.place(x=100,y=10)
    
    


# RESERVATION
def reserve():
    #background image placed
    user_details()


#CHECK TRAIN
def enquiry():
        
    #background image placed
    top1=Toplevel(width=2000,height=2000)
    img=ImageTk.PhotoImage(Image.open("7.jpg"))
    l1= Label(top1,image=img)
    l1.image=img
    l1.place(x=0, y=0, relwidth=1, relheight=1)
    

    
    s2=Spinbox(top1,bd=5,values=("DELHI","MUMBAI CENTRAL","MUMBAI(CSMT)","DADAR(CR)","PUNE","KOLKATA","CHENNAI","NAGPUR","SOLAPUR"),textvariable=val1,bg="white",fg="black",font=('Arial',-20,'bold'),width=25)
    s3=Spinbox(top1,bd=5,values=("DELHI","MUMBAI CENTRAL","MUMBAI(CSMT)","DADAR(CR)","PUNE","KOLKATA","CHENNAI","NAGPUR","SOLAPUR"),textvariable=val2,bg="white",fg="black",font=('Arial',-20,'bold'),width=25)
    
    
    text1=Text(top1,font=('Courier',-20,'italic'),bd=5,width=10,height=1,fg="gold",bg="dark slate grey")
    text1.insert(END,'FROM')
    text1.place(x=70,y=100)
    
    
    text2=Text(top1,font=('Courier',-20,'italic'),bd=5,width=10,height=1,fg="gold",bg="dark slate grey")
    text2.insert(END,'TO')
    text2.place(x=70,y=150)
    
    
    s3.place(x=300,y=150)
    s2.place(x=300,y=100)
    b9=Button(top1,text="Back",width=10,height=1,bg="dark slate grey",fg="gold",activebackground="white",activeforeground="black",font=('Arial','-15','bold'),command=top1.destroy)
    b9.place(x=30,y=50)
    
    def traindisplay():
        fromstat=val1.get()
        tostat=val2.get()
        conn2=sqlite3.connect('login.db')
        with conn2:
            cursor3=conn2.cursor()
        find_train = ('SELECT * FROM traininfo WHERE FROM_STATION = ? and TO_STATION= ?')
        cursor3.execute(find_train,[(fromstat),(tostat)])
        result=cursor3.fetchall()
        total=('SELECT * FROM booking1')
        cursor3.execute(total)
        avail=cursor3.fetchall()
        i=40
        k=0
        z=i-len(avail)
        z=str(z)
        if result:
            Mylabel=Label(top1,text="TRAIN\nNO.",bg="gold",font=('Arial','-15','bold'),bd=2,width=10,height=3).place(x=10,y=250)
            Mylabel=Label(top1,text="NAME",bg="gold",font=('Arial','-15','bold'),width=55,height=3).place(x=110,y=250)
            Mylabel=Label(top1,text="FROM\nSTATION",bg="gold",font=('Arial','-15','bold'),width=19,height=3).place(x=620,y=250)
            Mylabel=Label(top1,text="TO\nSTATION",bg="gold",font=('Arial','-15','bold'),width=19,height=3).place(x=800,y=250)
            Mylabel=Label(top1,text="DISTANCE\n[IN KM]",bg="gold",font=('Arial','-15','bold'),width=10,height=3).place(x=980,y=250)
            Mylabel=Label(top1,text="DEPARTURE\nTIME\n(Source)",bg="gold",font=('Arial','-15','bold'),width=10,height=3).place(x=1080,y=250)
            Mylabel=Label(top1,text="ARRIVAL\nTIME\n(Destination)",bg="gold",font=('Arial','-15','bold'),width=10,height=3).place(x=1180,y=250)
            Mylabel=Label(top1,text="AVAILABILITY",bg="gold",font=('Arial','-15','bold'),width=20,height=3).place(x=1280,y=250)
            for i in range(7):
                for j in range(7):
                    if(i<len(result)):
                        if(j==0):
                            Mylabel=Label(top1,text=result[i][j],bg="goldenrod",font=('Arial','-15','bold'),width=10,height=2).place(x=10,y=350+k)
                        elif(j==1):
                            Mylabel=Label(top1,text=result[i][j],bg="goldenrod",font=('Arial','-15','bold'),width=55,height=2).place(x=110,y=350+k)
                        elif(j==2):
                            Mylabel=Label(top1,text=result[i][j],bg="goldenrod",font=('Arial','-15','bold'),width=19,height=2).place(x=620,y=350+k)
                        elif(j==3):
                            Mylabel=Label(top1,text=result[i][j],bg="goldenrod",font=('Arial','-15','bold'),width=19,height=2).place(x=800,y=350+k)
                        elif(j==4):
                            Mylabel=Label(top1,text=result[i][j],bg="goldenrod",font=('Arial','-15','bold'),width=10,height=2).place(x=980,y=350+k)
                        elif(j==5):
                            Mylabel=Label(top1,text=result[i][j],bg="goldenrod",font=('Arial','-15','bold'),width=10,height=2).place(x=1080,y=350+k)
                        elif(j==6):
                            Mylabel=Label(top1,text=result[i][j],bg="goldenrod",font=('Arial','-15','bold'),width=10,height=2).place(x=1180,y=350+k)
                        if(i-len(avail)!=0):
                            Mylabel=Label(top1,text=z,bg="goldenrod",font=('Arial','-15','bold'),width=20,height=2).place(x=1280,y=350+k)
                            
                    if(i>len(result)-1):
                        if(j==0):
                            Mylabel=Label(top1,text="",bg="goldenrod",font=('Arial','-15','bold'),width=10,height=2).place(x=10,y=350+k)
                        elif(j==1):
                            Mylabel=Label(top1,text="",bg="goldenrod",font=('Arial','-15','bold'),width=55,height=2).place(x=110,y=350+k)
                        elif(j==2):
                            Mylabel=Label(top1,text="",bg="goldenrod",font=('Arial','-15','bold'),width=19,height=2).place(x=620,y=350+k)
                        elif(j==3):
                            Mylabel=Label(top1,text="",bg="goldenrod",font=('Arial','-15','bold'),width=19,height=2).place(x=800,y=350+k)
                        elif(j==4):
                            Mylabel=Label(top1,text="",bg="goldenrod",font=('Arial','-15','bold'),width=10,height=2).place(x=980,y=350+k)
                        elif(j==5):
                            Mylabel=Label(top1,text="",bg="goldenrod",font=('Arial','-15','bold'),width=10,height=2).place(x=1080,y=350+k)
                        elif(j==6):
                            Mylabel=Label(top1,text="",bg="goldenrod",font=('Arial','-15','bold'),width=10,height=2).place(x=1180,y=350+k)
                        if(1):
                            Mylabel=Label(top1,text="",bg="goldenrod",font=('Arial','-15','bold'),width=20,height=2).place(x=1280,y=350+k)
                k+=50  
        return      
    b46=Button(top1,text="submit",bg="dark slate grey",fg="gold",width=20,font=('Courier','-20','italic'),command=traindisplay)
    b46.place(x=70,y=200)
    
    
#LIVE STATUS
def webpage():
    webbrowser.open_new("https://www.railyatri.in/live-train-status")
    
    

def live_status():
    top2=Toplevel()
    
    img=ImageTk.PhotoImage(Image.open("live.jpg"))
    l4= Label(top2,image=img)
    l4.image=img
    l4.place(x=0, y=0, relwidth=1, relheight=1)
    
    
    b=Button(top2,text="CLICK HERE TO GET LIVE STATUS......",width=45,height=2,font=('Arial',-20,'underline'),command=webpage,bg="DarkGoldenrod")
    b.place(x=400,y=300)
    
    
    b9=Button(top2,text="Back",width=10,height=1,bg="DarkGoldenrod",fg="black",activebackground="white",activeforeground="black",font=('Arial','-15','bold'),command=top2.destroy)
    
    b9.place(x=100,y=50)
    

#login page logic----

f=Frame(root,width=2000,height=2000)
f.propagate(0)
f.pack()


#database
def login():
    name=login_usr.get()
    passwd=login_password.get()
    if name=='' or passwd=='':
        check_login()
    else:
        conn=sqlite3.connect('login.db')
        with conn:
            cursor = conn.cursor()
        #Find user, If there is any take proper action 
        find_user = ('SELECT * FROM reservation21 WHERE USERNAME = ? AND PASSWORD=?')
        cursor.execute(find_user,[(name),(passwd)])
        result = cursor.fetchall()
        if result:
            
            top=Toplevel(width=2000,height=2000)
        
        

            img=ImageTk.PhotoImage(Image.open("2.jpg"))
            l4= Label(top,image=img)
            l4.image=img
            l4.place(x=0, y=0, relwidth=1, relheight=1)
        
        
            b5=Button(top,text="Reserve",width=30,height=2,bd=6,bg="light salmon",fg="black",activebackground="white",activeforeground="black",font=('Arial','-15','bold'),command=reserve)
            b6=Button(top,text="Train Search",width=30,height=2,bd=6,bg="light salmon",fg="black",activebackground="white",activeforeground="black",font=('Arial','-15','bold'),command=enquiry)
            b7=Button(top,text="Complain",width=30,height=2,bd=6,bg="light salmon",fg="black",activebackground="white",activeforeground="black",font=('Arial','-15','bold'),command=complain)
            b8=Button(top,text="Live status",width=30,height=2,bd=6,bg="light salmon",fg="black",activebackground="white",activeforeground="black",font=('Arial','-15','bold'),command=live_status)
        
            b9=Button(top,text="Back",width=10,height=1,bg="light salmon",fg="black",activebackground="white",activeforeground="black",font=('Arial','-15','bold'),command=top.destroy)
        
        
            b9.place(x=100,y=50)
            b5.place(x=400,y=300)
            b6.place(x=800,y=300)
            b7.place(x=400,y=500)
            b8.place(x=800,y=500)
        else:
            check_table()
            return
    
def signup():
    
    def check_entry():
        
        s_name=signup_name.get()
        s_username=signup_username.get()
        s_passwd=signup_password.get()
        s_phone=signup_phone.get()
        s_email=signup_email.get()
                
        if (s_name=='' or s_username=='' or s_passwd=='' or s_phone=='' or s_email==''):
            warn11=Label(top10,text="BLANK ENTRY FIELDS",width=50,height=2,font=("bold",15),bg="black",fg="green")
            warn11.place(x=200,y=700)
        elif(1):
            warn11=Label(top10,text="",width=50,height=2,font=("bold",15),bg="black",fg="green")
            warn11.place(x=200,y=700)
            s=signup_phone.get()
            s=str(s)
            s1=re.fullmatch('[6-9][0-9]{9}',s)
            if(s1!=None):
                l10=Label(top10,text="",bg="black",fg="green",width=40,height=1,font=('Arial',-20,'bold'))
                l10.place(x=900,y=420)
                pass
            else:
                l10=Label(top10,text="Please Enter Valid Mobile No!",bg="black",fg="green",width=40,height=1,font=('Arial',-20,'bold'))
                l10.place(x=900,y=420)
            
            s1=signup_email.get()
            s2=re.fullmatch('\w[a-zA-z0-9_.]*@gmail[.]com',str(s1))
            if(s2!=None):
                l10=Label(top10,text="",bg="black",fg="green",width=40,height=1,font=('Arial',-20,'bold'))
                l10.place(x=900,y=500)
                pass
            else:
                l10=Label(top10,text="Please Enter Valid Email-id!",width=40,height=1,bg="black",fg="green",font=('Arial',-20,'bold'))
                l10.place(x=900,y=500)
                return
            conn=sqlite3.connect('login.db')
            with conn:
                cursor=conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS reservation21 (NAME TEXT ,USERNAME TEXT,PASSWORD TEXT,PHONE_NUMBER TEXT ,EMAIL TEXT)')
            find_user=("SELECT * FROM reservation21 WHERE USERNAME=? ")
            cursor.execute(find_user,[(s_username)])
            result=cursor.fetchall()
            if result:
                warn12=Label(top10,text="USERNAME TAKEN, TRY DIFFERENT ONE",width=50,height=2,font=("bold",15),bg="black",fg="green")
                warn12.place(x=200,y=700)
            else:
                cursor.execute('CREATE TABLE IF NOT EXISTS reservation21 (NAME TEXT ,USERNAME TEXT,PASSWORD TEXT,PHONE_NUMBER TEXT ,EMAIL TEXT)')
                cursor.execute('INSERT INTO reservation21 (NAME,USERNAME,PASSWORD,PHONE_NUMBER,EMAIL) VALUES(?,?,?,?,?)',(s_name,s_username,s_passwd,s_phone,s_email))
                conn.commit()
                conn.close()
                warn13=Label(top10,text="SUCCESS!,ACCOUNT CREATED!",width=50,height=2,font=("bold",15),bg="black",fg="green")
                warn13.place(x=200,y=700)
                return
    if(True):
        
        top10=Toplevel(width=2000,height=2000)
        img=ImageTk.PhotoImage(Image.open("f.jpg"))
        l1= Label(top10,image=img)
        l1.image=img
        l1.place(x=0, y=0, relwidth=1, relheight=1)
        
        l4=Text(top10,width=15,bd=5,height=1,bg="dark slate grey",font=('Arial',-25,'bold'))
        l4.insert(END,'USERNAME')
        l4.place(x=200,y=270)


        l2=Text(top10,width=15,bd=5,height=1,bg="dark slate grey",font=('Arial',-25,'bold'))
        l2.insert(END,'NAME')
        l2.place(x=200,y=200)
            
        l5=Text(top10,width=15,bd=5,height=1,bg="dark slate grey",font=('Arial',-25,'bold'))
        l5.insert(END,'PASSWORD')
        l5.place(x=200,y=350)
            

        l6=Text(top10,width=15,bd=5,height=1,bg="dark slate grey",font=('Arial',-25,'bold'))
        l6.insert(END,'MOBILE NO.')
        l6.place(x=200,y=430)
            

        l3=Text(top10,width=15,bd=5,height=1,bg="dark slate grey",font=('Arial',-25,'bold'))
        l3.insert(END,'EMAIL ID')
        l3.place(x=200,y=500)
            
        e1=Entry(top10,width=25,bd=5,textvar=signup_name,font=('Courier',-25,'bold'),fg="black",bg="white")
        e2=Entry(top10,width=25,bd=5,textvar=signup_username,font=('Courier',-25,'bold'),fg="black",bg="white")
        e3=Entry(top10,width=25,bd=5,textvar=signup_password,font=('Courier',-25,'bold'),fg="black",bg="white",show="*")
        e4=Entry(top10,width=25,bd=5,textvar=signup_phone,font=('Courier',-25,'bold'),fg="black",bg="white")
        e5=Entry(top10,width=25,bd=5,textvar=signup_email,font=('Courier',-25,'bold'),fg="black",bg="white")
            
            
        e1.place(x=500,y=200)
        e2.place(x=500,y=270)
        e3.place(x=500,y=350)
        e4.place(x=500,y=430)
        e5.place(x=500,y=500)
        
            
        b1=Button(top10,text="Submit",width=10,height=1,bg="azure",fg="black",activebackground="white",activeforeground="black",font=('Arial','-15','bold'),command=check_entry)
        b1.place(x=300,y=650)
        b10=Button(top10,text="Back",width=10,height=1,bg="azure",fg="black",activebackground="white",activeforeground="black",font=('Arial','-15','bold'),command=top10.destroy)
        b10.place(x=100,y=10)
        
 
#background image placed
img=ImageTk.PhotoImage(Image.open("f.jpg"))
l1= Label(f,image=img)
l1.place(x=0, y=0, relwidth=1, relheight=1)


t1=Text(f,bd=5,font=('Courier',-20,'bold'),width=15,height=1,fg="grey",bg="dark slate grey")
t1.insert(END,'Username')
t1.place(x=500,y=500)

t2=Text(f,bd=5,font=('Courier',-20,'bold'),width=15,height=1,fg="grey",bg="dark slate grey")
t2.insert(END,'Password')
t2.place(x=500,y=600)


e1=Entry(f,width=20,bd=5,font=('Courier',-20,'bold'),fg="grey",bg="white",textvar=login_usr)
e2=Entry(f,width=20,bd=5,font=('Courier',-20,'bold'),fg="grey",bg="white",show="*",textvar=login_password)

e1.place(x=750,y=500)
e2.place(x=750,y=600)

#tittle logic
ttitle=Text(f,font=('Courier',-35,'italic'),bd=5,width=35,height=1,fg="grey",bg="dark slate grey")
ttitle.insert(END,'    WELCOME TO INDIAN RAILWAYS')
ttitle.place(x=400,y=200)


text1=Text(f,font=('Courier',-20,'italic'),bd=5,width=15,height=1,fg="grey",bg="dark slate grey")
text1.insert(END,'    Safety')
text1.place(x=450,y=350)

text2=Text(f,font=('Courier',-20,'italic'),bd=5,width=15,height=1,fg="grey",bg="dark slate grey")
text2.insert(END,'    Security')
text2.place(x=650,y=350)


text3=Text(f,font=('Courier',-20,'italic'),bd=5,width=15,height=1,fg="grey",bg="dark slate grey")
text3.insert(END,'  Punctuality')
text3.place(x=850,y=350)

back=Button(f,text="back",bg="light grey",fg="black",width=20,font=('Courier','-14','bold'),command=root.destroy)
back.place(x=50,y=50)

b1=Button(f,text="login",bg="light grey",fg="black",width=20,font=('Courier','-14','bold'),command=login)
b1.place(x=900,y=680)

b2=Button(f,text="Signup",bg="light grey",fg="black",width=20,font=('Courier','-14','bold'),command=signup)
b2.place(x=700,y=680)
def check_login():
    warn1=Label(f,text="BLANK USERNAME OR PASSWORD!",width=50,height=2,font=("bold",15),bg="black",fg="green")
    warn1.place(x=400,y=750)
def check_table():
    warn1=Label(f,text="INVALID USERNAME OR PASSWORD!",width=50,height=2,font=("bold",15),bg="black",fg="green")
    warn1.place(x=400,y=750)
root.mainloop()
