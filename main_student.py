from tkinter import*
from tkinter import ttk
from pil import Image,ImageTk
from tkinter import messagebox
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from helpdesk import Help
from time import strftime
from datetime import datetime
import sqlite3
import tkinter
import webbrowser
import os
import pyttsx3
import sqlite3
import mysql.connector
import cv2
import csv
import bcrypt
from tkinter import filedialog




class Face_Recognition_System_student:##for window
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")#for window size
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("icon-1.ico")
        
        
        #bg image
        img3=Image.open(r"FRS_images\background.jpg")
        img3=img3.resize((1520,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1520,height=790)
        
        
        ########time 
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(bg_img,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()   
        
        lblportal=Label(bg_img,text="Student Portal",font=('times new roman',14,'bold'),background='white',foreground='blue')
        lblportal.place(x=1000,y=0,width=210,height=50) 
        
        #details button
        img4=Image.open(r"FRS_images\student_details.png")
        img4=img4.resize((140,190),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=220)
        
        b2=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2")
        b2.place(x=100,y=300,width=220,height=40)
        
        #Detect face button
        img5=Image.open(r"FRS_images\attendance.png")
        img5=img5.resize((160,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b3=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b3.place(x=400,y=100,width=220,height=220)
        
        b4=Button(bg_img,text="Take attendance",cursor="hand2",command=self.face_data)
        b4.place(x=400,y=300,width=220,height=40)
        
        #Attendance button
        img6=Image.open(r"FRS_images\attendance_report.jpg")
        img6=img6.resize((160,190),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b5=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.Attendance_data)
        b5.place(x=700,y=100,width=220,height=220)
        
        b6=Button(bg_img,text="Attedance Report",cursor="hand2",command=self.Attendance_data)
        b6.place(x=700,y=300,width=220,height=40)
        
        #Developer Button
       
       
        img11=Image.open(r"FRS_images\dev.jpg")
        img11=img11.resize((160,190),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b13=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.open_Linkedin)
        b13.place(x=1000,y=100,width=220,height=220)
        
        b14=Button(bg_img,text="Developer",cursor="hand2",command=self.open_Linkedin)
        b14.place(x=1000,y=300,width=220,height=40)
        
       
        
        #Train face button
        
        img8=Image.open(r"FRS_images\train_dataset.jpg")
        img8=img8.resize((200,190),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b9=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b9.place(x=100,y=380,width=220,height=220)
        
        b10=Button(bg_img,text="Train System",cursor="hand2",command=self.train_data)
        b10.place(x=100,y=580,width=220,height=40)
        
        #help desk button

        img7=Image.open(r"FRS_images\help_desk.jpg")
        img7=img7.resize((160,190),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b7=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.helpdesk_data)
        b7.place(x=400,y=380,width=220,height=220)
        
        b8=Button(bg_img,text="Help Desk",cursor="hand2",command=self.helpdesk_data)
        b8.place(x=400,y=580,width=220,height=40)
        
       
        
        #EXIT
       
        img10=Image.open(r"FRS_images\exit.png")
        img10=img10.resize((160,190),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b11=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.exit)
        b11.place(x=700,y=380,width=220,height=220)
        
        b12=Button(bg_img,text="EXIT",cursor="hand2",command=self.exit)
        b12.place(x=700,y=580,width=220,height=40)
        
        
         
        
    
       
        
    #_______________________buttons functions______________#
    
   
    def open_Linkedin(self):
        webbrowser.open_new("https://www.linkedin.com/in/jahnavi-bethapudi/") 
   
        
    def student_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Student_win(self.new_window)  
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)  
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)  
    def Attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window) 
    def helpdesk_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window) 
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want exit this application",parent=self.root)  
        if self.exit>0:
            self.root.destroy()
        else:
            return     







class Student_win:##for window
    def __init__(self,root):
        self.root=root
        self.root.attributes('-fullscreen', True)#for window size
        self.root.title("Student details")
        #root.mainloop()
        self.root.wm_iconbitmap("icon-1.ico")
        #==============variables==============#
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
       

        
        
        #bg image
        img3=Image.open(r"FRS_images\bg-1.jpg")
        img3=img3.resize((1520,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1520,height=790)
        
        
        title_label=Label(bg_img,text="Student details",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1410,height=45)
        quit=Button(title_label, text="Back", command=self.root.destroy,bg="Red")
        quit.place(x=1150,y=10,width=70,height=35)
        
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=100,width=1480,height=600) 
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=650,height=580)
        
        img_left=Image.open(r"FRS_images\studentbg.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        
        frame_label=Label(Left_frame,image=self.photoimg_left)
        frame_label.place(x=5,y=0,width=720,height=130)
       
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=635,height=150)
        
        
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer Science","CS/IT","Civil","Mechanical","Electrionics")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Courses","DBMS","OS","MATHS","CNS")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        
        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)
        
        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=5,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="read only")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)
        
        #class student information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=290,width=635,height=260)
        
        #student ID label
        studentId_label=Label(class_Student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)
        
        studentId_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        #student name
        studentname_label=Label(class_Student_frame,text="Student name:",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,sticky=W)
        
        studentname_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,sticky=W)
        
        #class division
        class_div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
       
        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="read only")
        div_combo["values"]=("Select Division","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=9,pady=5,sticky=W)
        
        
        #Roll NO
       
        roll_no_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Gender
       
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="read only")
        gender_combo["values"]=("Select Gender","Female","Male","others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=9,pady=5,sticky=W)
        
        #DOB
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Email
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #phone number
        phone_label=Label(class_Student_frame,text="Phone:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_phone,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #Address
        
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_address,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Teacher name
        
        teacher_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="take Photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo sample",value="No")
        radiobtn2.grid(row=6,column=1)
        #bbuttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=195,width=630,height=40)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=23,font=("times new roman",12,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3)
        
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take photo sample",width=23,font=("times new roman",12,"bold"),bg="green",fg="white")
        take_photo_btn.grid(row=0,column=4)
        
        update_photo_btn=Button(btn_frame,text="Update photo sample",command=self.generate_dataset,width=23,font=("times new roman",12,"bold"),bg="green",fg="white")
        update_photo_btn.grid(row=0,column=5)
        
        
        
        #Right label frame
       
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=580,height=580)
        
        img_right=Image.open(r"FRS_images\studentbg.jpg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        
        frame_label=Label(Right_frame,image=self.photoimg_right)
        frame_label.place(x=5,y=0,width=720,height=130)
        
        
        #---------------Search system----------------#
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=570,height=70)
        
        Search_label=Label(Search_frame,text="Search By:",bg="powder blue",font=("times new roman",12,"bold"))
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        #search
        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_com_search,state="readonly",font=("times new roman",12,"bold"),width=17)
        search_combo["values"]=("Select","Roll","Phone","Name","Dep")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        self.var_search=StringVar()
        Search_entry=ttk.Entry(Search_frame,textvariable=self.var_search,width=15,font=("times new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        Search_btn=Button(Search_frame,text="Search",command=self.search_data,font=("times new roman",12,"bold"),bg="green",fg="white")
        Search_btn.grid(row=0,column=4,padx=4)
        
        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=570,height=340)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","rollNo","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("rollNo",text="Rollnumber")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="SampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("rollNo",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        #-----------function declaration-----------#
        
  
     
    
    
    #========================fetch data===============#
    def fetch_data(self):
        conn=sqlite3.connect(r'database\face_recognition.db')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
   
        
    #==================get cursor===========================#
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
        #++++++++++++++++++++++++++++++UPADTE FUNCTION+++++++++++++++++++++++++++#
  
      ################# delete ##########################
    #reset 
    def reset_data(self):
         self.var_dep.set("Select Department"),
         self.var_course.set("Select Course"),
         self.var_year.set("Select Year"),
         self.var_semester.set("Select Semester"),
         self.var_std_id.set(""),
         self.var_std_name.set(""),
         self.var_div.set("Select Division"),
         self.var_roll.set(""),
         self.var_gender.set("Male"),
         self.var_dob.set(""),
         self.var_email.set(""),
         self.var_phone.set(""),
         self.var_address.set(""),
         self.var_teacher.set(""),
         self.var_radio1.set("")
         
    #search
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=sqlite3.connect(r'database\face_recognition.db')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                        
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
                
    #generating data set or take photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                #messagebox.showinfo("Instructions","1.Show your face to camera in correct angle\n2.Please dont close camera button while it is taking photosamples",parent=self.root)
                conn=sqlite3.connect(r'database\face_recognition.db')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=?,course=?,Year=?,Semester=?,Name=?,Division=?,Roll=?,gender=?,Dob=?,Email=?,Phone=?,Address=?,Teacher=?,PhotoSample=? where Student_id=?",(
                                                                                                                                                                                                                  
                                                                                                             self.var_dep.get(),
                                                                                                             self.var_course.get(),
                                                                                                             self.var_year.get(),
                                                                                                             self.var_semester.get(),
                                                                                                             self.var_std_name.get(),
                                                                                                             self.var_div.get(),
                                                                                                             self.var_roll.get(),
                                                                                                             self.var_gender.get(),
                                                                                                             self.var_dob.get(),
                                                                                                             self.var_email.get(),
                                                                                                             self.var_phone.get(),
                                                                                                             self.var_address.get(),
                                                                                                             self.var_teacher.get(),
                                                                                                             self.var_radio1.get(), 
                                                                                                             self.var_std_id.get()==id+1
                                                                                                                                           
                                                                                                                           ))             
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
                
                    
                    
                    #===============Load predefined data on face frontals form oepncv+++++++++++++++
                face_classifier=cv2.CascadeClassifier(r"xmlfiles\haarcascade_frontalface_default.xml")
                    
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor-1.3
                        #Minimum Neoghbor=5
                        
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w] 
                        return face_cropped
                        
                capture=cv2.VideoCapture(0) 
                img_id=0
                while True:
                    ret,my_frame=capture.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450)) 
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face", face)
                        
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  
                
                
    ################## attendance report #############


mydata=[]
class Attendance:##for window
    def __init__(self,root2):
        self.root2=root2
        self.root2.attributes('-fullscreen', True)#for window size
        self.root2.title("Attendance Report")
        self.root2.wm_iconbitmap("icon-1.ico")
        #variables########
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        #bg image
        img3=Image.open(r"FRS_images\bg-1.jpg")
        img3=img3.resize((1520,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root2,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1520,height=790)
        
        
        title_label=Label(bg_img,text="My Attendance Report",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1410,height=45)
        quit=Button(title_label, text="<<Back", command=self.root2.destroy,bg="Red")
        quit.place(x=1150,y=10,width=70,height=35)
        
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=100,width=1480,height=600) 
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=625,height=550)
        img_left=Image.open(r"FRS_images\attendancereportbg.jpg")
        img_left=img_left.resize((700,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        frame_label=Label(Left_frame,image=self.photoimg_left)
        frame_label.place(x=5,y=0,width=610,height=130)
        
        Left_inside_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE)
        Left_inside_frame.place(x=0,y=135,width=615,height=385)
        #attendance id
        attendanceId_label=Label(Left_inside_frame,text="AttendanceId:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceId_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_atten_id,width=22,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,pady=5,sticky=W)
        
        
        #student name
        name_label=Label(Left_inside_frame,text="Student name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0)
        
        name_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_atten_name,width=22,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,pady=8,sticky=W)
        #Department
        depLabel=Label(Left_inside_frame,text="Department:",bg="white",font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2)
        atten_dep=ttk.Entry(Left_inside_frame,textvariable=self.var_atten_dep,width=22,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3,pady=8)
        
        #Roll
        rollLabel=Label(Left_inside_frame,text="Roll:",bg="white",font="comicsansns 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)
        atten_roll=ttk.Entry(Left_inside_frame,textvariable=self.var_atten_roll,width=22,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)
        
        
        
        #time
        timeLabel=Label(Left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)
        atten_time=ttk.Entry(Left_inside_frame,textvariable=self.var_atten_time,width=22,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)
        #date
        dateLabel=Label(Left_inside_frame,text="Date:",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2,padx=20)
        atten_date=ttk.Entry(Left_inside_frame,textvariable=self.var_atten_date,width=22,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8)
        #attendance
        attendanceLabel=Label(Left_inside_frame,text="Attendance status",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(Left_inside_frame,textvariable=self.var_atten_attendance,width=20,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        
        #bbuttons frame
        btn_frame=Frame(Left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=350,width=620,height=100)
        
        
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=35,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        reset_btn.grid(row=0,column=0)
        
        showAll_btn=Button(btn_frame,text="Show all",command=self.fetch_data,width=35,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        showAll_btn.grid(row=0,column=2)
        
        
        
        
        
        
        
        
        
        
        
        #Right label frame
       
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=660,y=10,width=600,height=550)
        ############### table ###################
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=120,width=580,height=410)
        
        ########### Search System #################
       
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=5,width=570,height=100)
        
        Search_label=Label(Search_frame,text="Search By:",bg="powder blue",font=("times new roman",12,"bold"))
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        #search
        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_com_search,state="readonly",font=("times new roman",12,"bold"),width=17)
        search_combo["values"]=("Select","id","date")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,sticky=W)
        
        self.var_search=StringVar()
        Search_entry=ttk.Entry(Search_frame,textvariable=self.var_search,width=15,font=("times new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        Search_btn=Button(Search_frame,text="Search",command=self.search_data,font=("times new roman",12,"bold"),bg="yellow",fg="black",width=10)
        Search_btn.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        Search_label_id=Label(Search_frame,text="Id of the student:",bg="powder blue",font=("times new roman",12,"bold"))
        Search_label_id.grid(row=1,column=0,sticky=W)
        
        self.var_search_id=StringVar()
        Search_entry=ttk.Entry(Search_frame,textvariable=self.var_search_id,width=15,font=("times new roman",12,"bold"))
        Search_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        Search_label_date=Label(Search_frame,text="dd/mm/yy:",bg="powder blue",font=("times new roman",12,"bold"))
        Search_label_date.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        self.var_search_date=StringVar()
        Search_entry=ttk.Entry(Search_frame,textvariable=self.var_search_date,width=15,font=("times new roman",12,"bold"))
        Search_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
        
        
        
        #+++++++++++++++scroll bar+++++++++++++++
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Deaprtment")
        self.AttendanceReportTable.heading("time",text="time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=150)
        self.AttendanceReportTable.column("roll",width=150)
        self.AttendanceReportTable.column("name",width=150)
        self.AttendanceReportTable.column("department",width=150)
        self.AttendanceReportTable.column("time",width=150)
        self.AttendanceReportTable.column("date",width=150)
        self.AttendanceReportTable.column("attendance",width=150)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        #+++++++++++fetch data++++++++++++++++++++
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
            
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])        
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")        
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")
       
        
    
    ###############fetch data#####################
    def fetch_data(self):
        conn=sqlite3.connect(r'database\face_recognition.db')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from attendance")
        data=my_cursor.fetchall()
        
        
        if len(data)!=0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in data:
                self.AttendanceReportTable.insert("",END,values=i)
            conn.commit()
        conn.close() 
        ###########################UPDATE FUCNTION$############################

                
    #search
    def search_data(self):
        #if self.var_com_search.get()=="" or self.var_search.get()=="":
            #messagebox.showerror("Error","Please select option")
        #else:
            try:
                conn=sqlite3.connect(r'database\face_recognition.db')
                my_cursor=conn.cursor()
                
                if self.var_com_search.get()=="" or self.var_search.get()=="" and self.var_search_id.get()!="" and self.var_search_date.get()!="" :
                    my_cursor.execute("select * from attendance where id LIKE '%"+str(self.var_search_id.get())+"%' and date LIKE '%"+str(self.var_search_date.get())+"%'")
                elif self.var_com_search.get()!="" or self.var_search.get()!="":
                    my_cursor.execute("select * from attendance where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                else:
                    messagebox.showerror("Error","Enter valid data")
                    
                data=my_cursor.fetchall()
                if len(data)==0:
                    messagebox.showerror("Error","Data Not found",parent=self.root2)
                
                if len(data)!=0:
                    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                    for i in data:
                        self.AttendanceReportTable.insert("",END,values=i)
                        
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root2) 
                
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System_student(root)
    root.mainloop()