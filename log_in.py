# ⚪️ log in system using tkinter
from tkinter import *
import sqlite3 
from tkinter import messagebox
from PIL import ImageTk,Image

root=Tk()
root.resizable(False,False)
root.title("Log in")
root.configure(bg='white')

bg_image=ImageTk.PhotoImage(Image.open("/Users/mohdanas/Desktop/🐍 projects/⚪️ Log in system💻🔐 /l1.jpeg")) #image address
label=Label(image=bg_image)
label.grid(row=0,column=0,padx=20,pady=20)

lf=LabelFrame(root,text="log in window",bg="white")
lf.config(font=("Courier",16))
lf.grid(row=0,column=1,padx=20,pady=20)

#⚪️--------labels----------- 
log_l=Label(lf,text="Log in",bg="white")
log_l.config(font=("Courier",30))
log_l.grid(row=0,column=0,columnspan=2,padx=20,pady=20)

new=Label(lf,text="New User?",bg="white")
new.config(font=("Courier",16))
new.grid(row=4,column=0,pady=(0,20))

email_l=Label(lf,text="email :",bg="white")
email_l.config(font=("Courier",16))
email_l.grid(row=1,column=0,padx=2,pady=20)

pswrd_l=Label(lf,text="password :",bg="white")
pswrd_l.config(font=("Courier",16))
pswrd_l.grid(row=2,column=0,padx=2,pady=(1,5))

#⚪️ ----------inputs-------------
email_i=Entry(lf)
email_i.grid(row=1,column=1,padx=(3,10))

pswrd_i=Entry(lf)
pswrd_i.grid(row=2,column=1,padx=(3,10),pady=(1,5))
#⚪️ ------------- function -------------
    # ⚪️ funtion to pop up new window to create acount
def account():
    global name_i
    global email_iac
    global pswrd_iac
    global acnt_win
    global lf2
    global bg2_image
    global label2
    
    conn=sqlite3.connect('customer.db')
    c=conn.cursor()
    
    acnt_win=Tk()
    acnt_win.title("New Account")
    acnt_win.config(bg="white")

    lf2=LabelFrame(acnt_win,text="Account window",bg="white")
    lf2.config(font=("Courier",16))
    lf2.grid(row=0,column=1,padx=20,pady=20)
    
    #⚪️ ---labels----- 
    wlcm_l=Label(lf2,text="Create an account",bg="white")
    wlcm_l.config(font=("Courier",30))
    wlcm_l.grid(row=0,column=0,columnspan=2,padx=20,pady=20)
    
    name_l=Label(lf2,text="Full name :",bg="white")
    name_l.config(font=("Courier",16))
    name_l.grid(row=1,column=0,padx=2,pady=(20,5))

    email_ac=Label(lf2,text="email :",bg="white")
    email_ac.config(font=("Courier",16))
    email_ac.grid(row=2,column=0,padx=2,pady=(1,5))

    pswrd_ac=Label(lf2,text="password :",bg="white")
    pswrd_ac.config(font=("Courier",16))
    pswrd_ac.grid(row=3,column=0,padx=2,pady=(1,20))

    #⚪️ -------inputs-------
    name_i=Entry(lf2,bg="white")
    name_i.grid(row=1,column=1,padx=(3,10),pady=(20,5))
    
    email_iac=Entry(lf2,bg="white")
    email_iac.grid(row=2,column=1,padx=(3,10),pady=(1,5))

    pswrd_iac=Entry(lf2,bg="white")
    pswrd_iac.grid(row=3,column=1,padx=(3,10),pady=(1,20))

    #⚪️ -------buttons-----
    create_btn=Button(lf2,text="Create",width=17,command=create,bg="white")
    create_btn.config(font=("Courier",18))
    create_btn.grid(row=5,column=0,columnspan=2,pady=(0,20))
    
    conn.commit()
    conn.close()
    
    #⚪️ --- create new acount function ----
def create():
    try:
        if (len(name_i.get())>=1 and len(email_iac.get())>=1 and len(pswrd_iac.get())>=8) :
            
            conn=sqlite3.connect('customer.db')
            c=conn.cursor()
            #⚪️ insert into table
            c.execute("INSERT INTO log_in Values (:name,:email,:pswrd)",
                    {
                    
                        'name':name_i.get(),
                        'email':email_iac.get(),
                        'pswrd':pswrd_iac.get()
                    } )
            
            conn.commit()
            conn.close()
            acnt_win.destroy()
            messagebox.showinfo("Congo🥳","⚪️Thank you for creating an account")
        else:
            messagebox.showerror("oops!","⚪️All fields are mendatory \n\n ⚪️Password minimum length should be 8 ")
    except:
            Label(acnt_win,text="email already in use").grid(row=4,column=0,columnspan=2,padx=2,pady=(1,20))
        
    #⚪️ --- log in function ---
def log():
    
    if (len(email_i.get())>=1 and len(pswrd_i.get())>=8) :
        conn=sqlite3.connect('customer.db')
        c=conn.cursor()
        c.execute("select * from log_in")
        data=c.fetchall()
        s=True
        for i in data:
            if i[1]==email_i.get() and i[2]==pswrd_i.get():
                messagebox.showinfo("Welcome","Welcome You are logged in")
                s=False
                break
        if s:
            messagebox.showerror("Invalid credentials","Invalid passwrod/email")
            
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Error","Incomplete Credentials\n\n⚪️Password minimum length should be 8")
    
#⚪️ -------buttons-------
    # ⚪️---log in button---
log_btn=Button(lf,text="Log in",width=26,command=log,bg="white")
log_btn.config(font=("Courier",16))
log_btn.grid(row=3,column=0,columnspan=2,padx=5,pady=20)

    #⚪️----- create new acnt button----
acnt_btn=Button(lf,text="Create an account ",width=17,command=account,bg="white")
acnt_btn.config(font=("Courier",14))
acnt_btn.grid(row=4,column=1,pady=(0,20))

root.mainloop()








