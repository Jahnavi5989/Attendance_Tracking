from tkinter import*
from tkinter import ttk
from pil import Image,ImageTk
from tkinter import messagebox
from student import Student
from train import Train
from face_recognition import Face_Recognition
from main_win import Face_Recognition_System_admin
from main_faculty import Face_Recognition_System_faculty
from main_student import Face_Recognition_System_student
from attendance import Attendance
from helpdesk import Help
from time import strftime
from datetime import datetime
import mysql.connector
import bcrypt
import tkinter
import os
import pyttsx3
import re
import sqlite3



def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()
    

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")
        self.root.wm_iconbitmap("icon-1.ico")
        ## varibale
        
        self.var_roles="Faculty"
        self.var_roles_admin="Admin"
        self.var_roles_student="Student"
        
        
        ############### Student and Faculty Login Frame #########################
        
        img3=Image.open(r"FRS_images\newbg.jpg")
        img3=img3.resize((1520,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1520,height=790)
        frame=Frame(self.root,bg="powder blue")
        frame.place(x=150,y=120,width=400,height=480)
        
        img1=Image.open(r"FRS_images\feamle_user.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="powder blue",borderwidth=0)
        lblimg1.place(x=300,y=125,width=100,height=100)
        
        get_str=Label(frame,text="Login",font=("times new roman",15,"bold"),fg="black",bg="powder blue")
        get_str.place(x=170,y=110)
        #labels
        username=labl=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="powder blue")
        username.place(x=90,y=155)
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=70,y=190,width=280)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="powder blue")
        password.place(x=90,y=225)
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=70,y=250,width=280)
        self.txtpass.config(show=". ",font=("times new roman",15,"bold"))
        #Login Button 
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),border=3,relief=RIDGE,fg="black",bg="dark blue",activebackground="Dark blue",activeforeground="black")
        loginbtn.place(x=140,y=300,width=120,height=35)
        
        #Register Button
        Registerbtn=Button(frame,text="New user register",command=self.register_window,font=("times new roman",15,"bold"),borderwidth=0,fg="black",bg="powder blue",activebackground="powder blue",activeforeground="black")
        Registerbtn.place(x=20,y=350,width=160)
        
        #forgotpassword
        forgotpassbtn=Button(frame,text="forget Password",command=self.forgot_password_window,font=("times new roman",15,"bold"),borderwidth=0,fg="black",bg="powder blue",activebackground="powder blue",activeforeground="black")
        forgotpassbtn.place(x=10,y=385,width=160)
        
        #cancel button
        quit=Button(frame, text="Cancel", command=self.root.destroy,bg="Red",fg="Black")
        quit.place(x=140,y=420,width=120,height=35)
    
        
        
        ############## Admin Login frame ############################
        
        frame_admin=Frame(self.root,bg="powder blue")
        frame_admin.place(x=750,y=120,width=400,height=480)
       
        
        img2=Image.open(r"FRS_images\feamle_user.png")
        img2=img2.resize((100,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimg2,bg="powder blue",borderwidth=0)
        lblimg2.place(x=900,y=125,width=100,height=100)
        
        get_str_1=Label(frame_admin,text="Admin Login",font=("times new roman",15,"bold"),fg="black",bg="powder blue")
        get_str_1.place(x=135,y=110)
        #labels
        username_admin=labl=Label(frame_admin,text="Email",font=("times new roman",15,"bold"),fg="black",bg="powder blue")
        username_admin.place(x=90,y=155)
        
        self.txtuser_admin=ttk.Entry(frame_admin,font=("times new roman",15,"bold"))
        self.txtuser_admin.place(x=70,y=190,width=280)
        
        password_admin=lbl=Label(frame_admin,text="Password",font=("times new roman",15,"bold"),fg="black",bg="powder blue")
        password_admin.place(x=90,y=225)
        
        self.txtpass_admin=ttk.Entry(frame_admin,font=("times new roman",15,"bold"))
        self.txtpass_admin.place(x=70,y=250,width=280)
        self.txtpass_admin.config(show=". ",font=("times new roman",15,"bold"))
        #Login Button 
        loginbtn_admin=Button(frame_admin,command=self.login_admin,text="Login",font=("times new roman",15,"bold"),border=3,relief=RIDGE,fg="black",bg="dark blue",activebackground="Dark blue",activeforeground="black")
        loginbtn_admin.place(x=140,y=300,width=120,height=35)
        
        #Register Button
        Registerbtn_admin=Button(frame_admin,text="New user register",command=self.register_window,font=("times new roman",15,"bold"),borderwidth=0,fg="black",bg="powder blue",activebackground="powder blue",activeforeground="black")
        Registerbtn_admin.place(x=20,y=350,width=160)
        
        #forgotpassword
        forgotpassbtn_admin=Button(frame_admin,text="forget Password",command=self.forgot_password_window,font=("times new roman",15,"bold"),borderwidth=0,fg="black",bg="powder blue",activebackground="powder blue",activeforeground="black")
        forgotpassbtn_admin.place(x=10,y=385,width=160)
        
         #cancel button
        quit=Button(frame_admin, text="Cancel", command=self.root.destroy,bg="Red",fg="Black")
        quit.place(x=140,y=420,width=120,height=35)
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register( self.new_window)
        
    
    
        ###############  LOGIN for faculty and students #########################3
        
    def login(self): 
         
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","Please fill required fields")
        else:
            conn=sqlite3.connect(r'database\face_recognition.db')
            my_cursor=conn.cursor()
            my_cursor.execute("select * from users where email=? and password=?",(
                                                                                self.txtuser.get(),
                                                                                self.txtpass.get()
                                                                                
                                                                        ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                query=("select * from users where email=? and password=? and role LIKE '%"+str(self.var_roles)+"%'")
                value=(self.txtuser.get(),self.txtpass.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                query2=("select * from users where email=? and password=? and role LIKE '%"+str(self.var_roles_student)+"%'")
                value2=(self.txtuser.get(),self.txtpass.get(),)
                my_cursor.execute(query2,value2)
                row2=my_cursor.fetchone()
                #print(row)
                if row!=None:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System_faculty( self.new_window)
                elif row2!=None:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System_student( self.new_window)
                else:
                    messagebox.showerror("Error","Invalid crdentials")
                    
            conn.commit()
            conn.close()
     ###############  LOGIN for admin #########################3
        
    def login_admin(self): 
         
        if self.txtuser_admin.get()=="" or self.txtpass_admin.get()=="":
            messagebox.showerror("Error","Please fill required fields")
        else:
            conn=conn=sqlite3.connect(r'database\face_recognition.db')
            my_cursor=conn.cursor()
            my_cursor.execute("select * from users where email=? and password=?",(
                                                                                self.txtuser_admin.get(),
                                                                                self.txtpass_admin.get()
                                                                        ))
            row_1=my_cursor.fetchone()
            if row_1==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                query=("select * from users where email=? and password=? and role LIKE '%"+str(self.var_roles_admin)+"%'")
                value=(self.txtuser_admin.get(),self.txtpass_admin.get(),)
                my_cursor.execute(query,value)
                row_1=my_cursor.fetchone()
                #print(row)
                if row_1!=None:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System_admin( self.new_window)
                else:
                    messagebox.showerror("Error","Invalid Credentials for admin Login")
            conn.commit()
            conn.close()
            
            #self.root.destroy()
            #===========================    forgot password ===========================#
    def reset_password(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        elif self.txt_new_password.get().isalnum()>0 or len(self.txt_new_password.get())<8:
            messagebox.showerror("Error","password must contain numbers,alphabets and some special characters i.e, @#$%&\n atleast 8 characters should be there",parent=self.root2)
        else:
            conn=sqlite3.connect(r'database\face_recognition.db')
            my_cursor=conn.cursor()
            query=("select * from users where email=? and securityQ=? and securityA=?")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update users set password=? where email=?")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Information","Your password has reset successfully",parent=self.root2)
                self.root2.destroy()
                
            
############################forgot password ############
            
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Enter the email address to Reset password",parent=self.root)
        else:
            conn=sqlite3.connect(r'database\face_recognition.db')
            my_cursor=conn.cursor()
            query=("select *from users where email=?")
            value=(self.txtuser.get(),)
            my_cursor.execute( query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","please enter the valid Email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("forgot password")
                self.root2.geometry("400x480+270+120")
                self.root2.configure(bg='white')
                l=Label(self.root2,text="Forgot password",font=("times new roman",15,"bold"),fg="black",bg="Dark green")
                l.place(x=0,y=10,relwidth=1)
                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg='black')
                security_Q.place(x=50,y=80)
                self.combo_security_Q=ttk.Combobox(self.root2,font=("tomes new roman",15, "bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your friend name","Your Pet name","Your favorite food")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg='black')
                security_A.place(x=50,y=150)
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)
                self.txt_security.config(show="*")
                
                #####NEW PASSWORD
                new_password=Label(self.root2,text="New password",font=("times new roman",15,"bold"),bg="white",fg='black')
                new_password.place(x=50,y=220)
                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_new_password.place(x=50,y=250,width=250)
                self.txt_new_password.config(show="*")
                reset_btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15,"bold"),fg="white",bg="green")
                reset_btn.place(x=100,y=280)
               
                
                    
                    
                
                
            
        
            
            
            
            
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")
        self.root.wm_iconbitmap("icon-1.ico")
        
        #####variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_role=StringVar()  
        self.var_role_id=StringVar()  
        self.var_valid=int()
       
        
       
        
        img3=Image.open(r"FRS_images\newbg.jpg")
        img3=img3.resize((1520,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1520,height=790)
        #left image
        self.bg1=ImageTk.PhotoImage(file=r"FRS_images\face_scan_adobe.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=500)
        
        frame=Frame(self.root,bg="powder blue")
        frame.place(x=520,y=100,width=700,height=500)
        register_label=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="Black",bg="powder blue")
        register_label.place(x=20,y=20)
        #labels and entry field
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="Black",bg="powder blue")
        fname.place(x=50,y=80)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",17,"bold"))
        fname_entry.place(x=50,y=110,width=250)
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="Black",bg="powder blue")
        l_name.place(x=370,y=80)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=110,width=250)
        #row 2 labels
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="Black",bg="powder blue")
        contact.place(x=50,y=145)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",17,"bold"))
        self.txt_contact.place(x=50,y=170,width=250)
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="powder blue",fg='black')
        email.place(x=370,y=140)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",17,"bold"))
        self.txt_email.place(x=370,y=170,width=250)
        #--------row 3
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="powder blue",fg='black')
        security_Q.place(x=50,y=210)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("tomes new roman",15, "bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your friend name","Your Pet name","Your favorite food")
        self.combo_security_Q.place(x=50,y=240,width=250)
        self.combo_security_Q.current(0)
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="powder blue",fg='black')
        security_A.place(x=370,y=210)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=240,width=250)
        self.txt_security.config(show="*")
        
        ############## ROLE #######################################
        role_combo=Label(frame,text="Select Your Role",font=("times new roman",15,"bold"),bg="powder blue",fg='black')
        role_combo.place(x=50,y=340)
        self.combo_role=ttk.Combobox(frame,textvariable=self.var_role,font=("tomes new roman",15, "bold"),state="readonly")
        self.combo_role["values"]=("Select","Admin","Student","Faculty")
        self.combo_role.place(x=50,y=370,width=250)
        self.combo_role.current(0)
        role_label=Label(frame,text="Enter your id",font=("times new roman",15,"bold"),bg="powder blue",fg='black')
        role_label.place(x=370,y=340)
        self.var_role_entry=ttk.Entry(frame,textvariable=self.var_role_id,font=("times new roman",15))
        self.var_role_entry.place(x=370,y=370,width=250)
        
        
        
        #row 4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="powder blue",fg="black")
        pswd.place(x=50,y=280)
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
       
        
        self.txt_pswd.place(x=50,y=310,width=250)
        self.txt_pswd.config(show="*")
       
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="powder blue",fg="black")
        confirm_pswd.place(x=370,y=270)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=310,width=250)
        self.txt_confirm_pswd.config(show="*")
        
        
        
         
         
        ##########checkbutton
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="By clicking on this you are Agreeing to our terms and conditions",font=("times new roman",12,"bold"),bg="powder blue",fg="black",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=400)
        
        #buttons
        #register button
        #img=Image.open(r"FRS_images\register-now-button-sign-key-push-banner-180929040.jpg")
        #img=img.resize((100,50),Image.ANTIALIAS)
        #self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,text="Register",command=self.register_data,borderwidth=0,bg="Dark blue",fg="black",font=("times new roman",15,"bold"),cursor="hand2",)
        b1.place(x=50,y=450,width=200,height=35)
        #login button
        #img1=Image.open(r"FRS_images\login.jpg")
        #img1=img1.resize((100,50),Image.ANTIALIAS)
        #self.photoimage1=ImageTk.PhotoImage(img1)
        #b2=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        #b2.place(x=330,y=420,width=200)
        
        
        
        
        ################ cancel ##################################
        
        quit=Button(frame,text="Cancel", command=self.root.destroy,bg="Red",fg="Black")
        quit.place(x=480,y=450,width=200,height=35)
        #########33 email validation ##############
    
        
      
        
  
        
        
        
        #======function decalration

    def register_data(self):
        register= messagebox.askyesno("Warning","Are you sure that you have given your data accurately you cannot modify this again",parent=self.root)
        if register==0:
            return
        else:
            self.isValid(self.var_email.get())
            if(self.var_valid==1):
                messagebox.showerror("Error","Enter email in correct format",parent=self.root)
            
            elif self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="" or self.var_securityQ.get()=="Select" or self.var_securityA.get()=="" or self.var_role.get()=="" or self.var_role_id.get()=="" or self.var_pass.get()=="" or self.var_confpass.get()=="":
                messagebox.showerror("Error","Please fill All fields",parent=self.root)
            elif any(ch.isdigit() for ch in self.var_fname.get()):
                messagebox.showerror("Error","Name cant have numbers",parent=self.root)
            elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","Enter same password",parent=self.root)
            elif self.var_pass.get().isalnum()>0 or len(self.var_pass.get())<8:
                messagebox.showerror("Error","password must contain numbers,alphabets and some special characters i.e, @#$%&\n atleast 8 characters should be there",parent=self.root)
        
            elif self.var_check.get()==0:
                messagebox.showerror("Error","Agree our terms and conditions",parent=self.root)
        
            else:
                conn=sqlite3.connect(r'database\face_recognition.db')
                my_cursor=conn.cursor()
                query=("select * from users where email=?")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                query2=("select * from users where roleid=?")
                value2=(self.var_role_id.get(),)
                my_cursor.execute(query2,value2)
                row2=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email",parent=self.root)
                if row2!=None:
                    messagebox.showerror("Error","Existing ID Given",parent=self.root)
                else:
                    my_cursor.execute("insert into users values(?,?,?,?,?,?,?,?,?)",(
                                                                        
                                                                        self.var_fname.get(),
                                                                        self.var_lname.get(),
                                                                        self.var_contact.get(),
                                                                        self.var_email.get(),
                                                                        self.var_securityQ.get(),
                                                                        self.var_securityA.get(),
                                                                        self.var_pass.get(),
                                                                        self.var_role.get(),
                                                                        self.var_role_id.get()
                                                                       
                                                                                        
                    ))
                    messagebox.showinfo("Success","Successfully registered",parent=self.root)
                    self.root.destroy()
                conn.commit()
                conn.close()
            
                    
    
    
    def isValid(self,email):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            self.var_valid=0
        else:
            self.var_valid=1
            
         

        

                  
            
            
            
        
        
       
        
        
if __name__ == "__main__":
    main()
    
    