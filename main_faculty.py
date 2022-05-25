from tkinter import*
from tkinter import ttk
from pil import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from helpdesk import Help
from employee import Employee
from train_faculty_data import Train_faculty
from face_recognition_faculty import Face_Recognition_faculty
from attendance_faculty import Attendance_Faculty
import csv
from tkinter import filedialog
from time import strftime
from datetime import datetime
import tkinter
import os
import pyttsx3
import cv2
import mysql.connector
from tkinter import messagebox


class Face_Recognition_System_faculty:##for window
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
        lbl=Label(bg_img,font=('times new roman',14,'bold'),foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        lblportal=Label(bg_img,text="Fcaulty Portal",font=('times new roman',14,'bold'),background='white',foreground='blue')
        lblportal.place(x=1000,y=0,width=210,height=50)     
        
        #details button
        img4=Image.open(r"C:\Face_Recognization\FRS_images\student_details.png")
        img4=img4.resize((140,190),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=220)
        
        b2=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",bg="white")
        b2.place(x=100,y=300,width=220,height=40)
        
        #Photos button
        img9=Image.open(r"C:\Face_Recognization\FRS_images\dataset.jpg")
        img9=img9.resize((160,190),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b11=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.faculty_details)
        b11.place(x=400,y=100,width=220,height=220)
        
        b12=Button(bg_img,text="Faculty Details",cursor="hand2",bg="white",command=self.faculty_details)
        b12.place(x=400,y=300,width=220,height=40)
        
        #Detect face button
        img5=Image.open(r"FRS_images\attendance.png")
        img5=img5.resize((160,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b3=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.faculty_attendance)
        b3.place(x=400,y=380,width=220,height=220)  
        
        b4=Button(bg_img,text="Take My attendance",cursor="hand2",bg="white",command=self.faculty_attendance)
        b4.place(x=400,y=580,width=220,height=40)  
        
        #Attendance button
        img6=Image.open(r"C:\Face_Recognization\FRS_images\attendance_report.jpg")
        img6=img6.resize((160,190),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b5=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.Attendance_data)
        b5.place(x=700,y=100,width=220,height=220)
        
        b6=Button(bg_img,text="Student Attedance Report",cursor="hand2",bg="white",command=self.Attendance_data)
        b6.place(x=700,y=300,width=220,height=40)
        
        #Developer Button
       
       
        img11=Image.open(r"FRS_images\faculty_male.jpg")
        img11=img11.resize((160,190),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b13=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.faculty_attendance_data)
        b13.place(x=1000,y=100,width=220,height=220)
        
        b14=Button(bg_img,text="My Attendance report",cursor="hand2",bg="white",command=self.faculty_attendance_data)
        b14.place(x=1000,y=300,width=220,height=40)
        
       
        
        #Train face button
        
        img8=Image.open(r"C:\Face_Recognization\FRS_images\train_dataset.jpg")
        img8=img8.resize((200,190),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b9=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b9.place(x=100,y=380,width=220,height=220)
        
        b10=Button(bg_img,text="Train System",cursor="hand2",bg="white",command=self.train_data)
        b10.place(x=100,y=580,width=220,height=40)
        
        #help desk button

        img7=Image.open(r"FRS_images\help_desk.jpg")
        img7=img7.resize((160,190),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b7=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.helpdesk_data)
        b7.place(x=700,y=380,width=220,height=220)
        
        b8=Button(bg_img,text="Help Desk",cursor="hand2",bg="white",command=self.helpdesk_data)
        b8.place(x=700,y=580,width=220,height=40)
        
        
        
        #EXIT
       
        img10=Image.open(r"FRS_images\exit.png")
        img10=img10.resize((160,190),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b11=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.exit)
        b11.place(x=1000,y=380,width=220,height=220)
        
        b12=Button(bg_img,text="EXIT",cursor="hand2",bg="white",command=self.exit)
        b12.place(x=1000,y=580,width=220,height=40)
        
        
         
        
    
       
        
    #_______________________buttons functions______________#
    #def open_img(self):
        #os.startfile("data") 
    def student_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Student(self.new_window)  
    def faculty_details(self):
        
        self.new_window=Toplevel(self.root)
        self.app=Employee_faculty(self.new_window) 
    def faculty_attendance_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Attendance_FacultyPortal(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train_faculty(self.new_window)  
    def faculty_attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_faculty(self.new_window)  
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
        
        
###################### Employee_faculty #####################################################3


class Employee_faculty:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x790+0+0")
        self.root.title('Faculty Details')
        self.root.configure(bg='white')
        self.root.wm_iconbitmap("icon-1.ico")
        
        #variable
        self.var_id=StringVar()
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designition=StringVar()
        self.var_email=StringVar()
        self.var_cityname=StringVar()
        self.var_mstatus=StringVar()
        self.var_dob=StringVar()
        self.var_idproofcombo=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_salary=StringVar()
        
        # title
        
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=0,width=1420,height=160)
        lbl_title=Label(img_frame,text="Faculty Information Portal",font=('times new roman',15,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=230,height=50)
        quit=Button(self.root, text="<<Back", command=self.root.destroy,bg="Red")
        quit.place(x=1200,y=10,width=70,height=35)
         
        
        #images
        
        img_left=Image.open(r"C:\Face_Recognization\FRS_images\employeebg.jpg")
        img_left=img_left.resize((800,150),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        frame_label=Label(img_frame,image=self.photoimg_left)
        frame_label.place(x=240,y=0,width=800,height=150)
        
        # Main frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=0,y=150,width=1300,height=495)
        # upper Frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text="Faculty Details",font=('times new roman',15,'bold'),fg='darkblue',bg='white')
        upper_frame.place(x=10,y=5,width=1250,height=220)
        
        #Labels and Entry field
        
        #Department
        lbl_dep=Label(upper_frame,text="Department",font=('arial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        
        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',12,'bold'),width=17,state='readonly')
        combo_dep['value']=('select Department','HR',"CSE","MECH","Civil","EEE","ECE","ECM")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        #Name
        lbl_name=Label(upper_frame,text="Name",font=('arial',11,'bold'),bg='white')
        lbl_name.grid(row=0,column=2,padx=2,pady=7)
        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)
        
        #Designition
        lbl_designition=Label(upper_frame,font=("arial",12,"bold"),text="Designition:",bg="white")
        lbl_designition.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        txt_designition=ttk.Entry(upper_frame,textvariable=self.var_designition,width=22,font=("arial",11,"bold"))
        txt_designition.grid(row=1,column=1,sticky=W,padx=2,pady=7)
        
        #Email
        lbl_email=Label(upper_frame,text="Email",font=('arial',12,'bold'),bg="white")
        lbl_email.grid(row=1,column=2,padx=2,pady=7)
        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=("arial",11,"bold"))
        txt_email.grid(row=1,column=3,padx=2,pady=7)
        
        #cityname
        lbl_address=Label(upper_frame,font=('arial',12,'bold'),text="CityName:",bg="white")
        lbl_address.grid(row=2,column=0,padx=2,pady=7)
        txt_address=ttk.Entry(upper_frame,textvariable=self.var_cityname,width=22,font=("arial",11,"bold"))
        txt_address.grid(row=2,column=1,padx=2,pady=7)
        
        #married
        lbl_marriage_status=Label(upper_frame,text="Marital Status",font=('arial',11,'bold'),bg='white')
        lbl_marriage_status.grid(row=2,column=2,padx=2,sticky=W)
        
        combo_marriage_status=ttk.Combobox(upper_frame,textvariable=self.var_mstatus,font=('arial',12,'bold'),width=17,state='readonly')
        combo_marriage_status['value']=("No Selection","Married","UnMarried")
        combo_marriage_status.current(0)
        combo_marriage_status.grid(row=2,column=3,padx=2,pady=10,sticky=W)
        
        #DOB
        lbl_dob=Label(upper_frame,font=('arial',12,'bold'),text="Date of Birth:",bg="white")
        lbl_dob.grid(row=3,column=0,padx=2,pady=7)
        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)
        
        #ID
        lbl_doj=Label(upper_frame,font=('arial',12,'bold'),text="Employee ID:",bg="white")
        lbl_doj.grid(row=3,column=2,padx=2,pady=7)
        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_id,width=22,font=("arial",11,"bold"))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)
        
        #Id proof
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcombo,state="readonly",font=("arial",12,"bold"),width=17)
        com_txt_proof['value']=("Select ID proof","ADHAR CARD","DRIVING LICENCE","VOTER ID","PAN CARD")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=0,column=4,sticky=W,padx=2,pady=7)
        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=("arial",11,"bold"))
        txt_proof.grid(row=0,column=5,padx=7,pady=7)
        #gender
        lbl_gender=Label(upper_frame,text="Gender:",font=('arial',11,'bold'),bg='white')
        lbl_gender.grid(row=1,column=4,padx=7,sticky=W)
        
        combo_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',12,'bold'),width=17,state='readonly')
        combo_txt_gender['value']=("No Selection","Male","female")
        combo_txt_gender.current(0)
        combo_txt_gender.grid(row=1,column=5,padx=7,pady=10,sticky=W)
        
        #phone
        lbl_phone=Label(upper_frame,font=("arial",12,"bold"),text="Phone No:",bg="White")
        lbl_phone.grid(row=2,column=4,sticky=W,padx=2,pady=7)
        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_contact,width=22,font=("arial",11,"bold"))
        txt_phone.grid(row=2,column=5,padx=2,pady=7)
        #Salary
        lbl_ctc=Label(upper_frame,font=("arial",12,"bold"),text="Salary(CTC):",bg="White")
        lbl_ctc.grid(row=3,column=4,sticky=W,padx=2,pady=7)
        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=("arial",11,"bold"))
        txt_ctc.grid(row=3,column=5,padx=2,pady=7)
        
        #Button frame
        #button_frame=LabelFrame(upper_frame,bd=2,relief=RIDGE,bg='white')
        #button_frame.place(x=1050,y=5,width=180,height=180)
        
       
        btn_reset=Button(upper_frame,text="Reset",command=self.reset_data,font=("arial",15,"bold"),width=20,bg='blue',fg='white')
        btn_reset.grid(row=1,column=7,padx=1,pady=5)
        
        # Button Frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=990,y=100,width=250,height=85)
        
        btn_Photo_sample=Button(button_frame,text="Take photo sample",command=self.generate_dataset,font=("arial",13,"bold"),width=20,bg='blue',fg='white')
        btn_Photo_sample.grid(row=2,column=6,padx=1,pady=5)
        
        btn_update_sample=Button(button_frame,text="Update photo sample",command=self.generate_dataset,font=("arial",13,"bold"),width=20,bg='blue',fg='white')
        btn_update_sample.grid(row=3,column=6,padx=1,pady=5)
        
        #down frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text="Faculty Details Table",font=('times new roman',15,'bold'),fg='darkblue',bg='white')
        down_frame.place(x=10,y=230,width=1250,height=245)
        
        #search frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white')
        search_frame.place(x=10,y=0,width=1220,height=40)
        
        search_by=Label(search_frame,text="Search By:",font=('times new roman',15,'bold'),fg='darkblue',bg='white')
        search_by.grid(row=0,column=0,sticky=W,padx=5)
        
        #search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable= self.var_com_search,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_search['value']=("Select Option","idproof","id")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)
        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=7,pady=7)
        
        btn_search=Button(search_frame,text="Search",command=self.search_data,font=("arial",13,"bold"),width=10,bg='Red',fg='white')
        btn_search.grid(row=0,column=3,padx=1,pady=5)
        
       
        ########## faculty table #####################
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=10,y=40,width=1220,height=175)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.faculty_table=ttk.Treeview(table_frame,column=("id","dep","name","desig","email","cityname","mstatus","dob","idproofcombo","idproof","gender","phone","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.faculty_table.xview)
        scroll_y.config(command=self.faculty_table.yview)
        
        self.faculty_table.heading('id',text='Employee ID')
        self.faculty_table.heading('dep',text='Department')
        self.faculty_table.heading('name',text='Name')
        self.faculty_table.heading('desig',text='Designation')
        self.faculty_table.heading('email',text='Email')
        self.faculty_table.heading('cityname',text='CityName')
        self.faculty_table.heading('mstatus',text='Marital Status')
        self.faculty_table.heading('dob',text='DOB')
        self.faculty_table.heading('idproofcombo',text='ID Type')
        self.faculty_table.heading('idproof',text='ID Proof')
        self.faculty_table.heading('gender',text='Gender')
        self.faculty_table.heading('phone',text='Contact')
        self.faculty_table.heading('salary',text='Salary(CTC)')
        
        self.faculty_table['show']='headings'
        
        self.faculty_table.column('id',width=130)
        self.faculty_table.column('dep',width=130)
        self.faculty_table.column('name',width=130)
        self.faculty_table.column('desig',width=130)
        self.faculty_table.column('email',width=130)
        self.faculty_table.column('cityname',width=130)
        self.faculty_table.column('mstatus',width=130)
        self.faculty_table.column('dob',width=130)
        self.faculty_table.column('idproofcombo',width=130)
        self.faculty_table.column('idproof',width=130)
        self.faculty_table.column('gender',width=130)
        self.faculty_table.column('phone',width=130)
        self.faculty_table.column('salary',width=130)
        
        self.faculty_table.pack(fill=BOTH,expand=1)
        self.faculty_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.fetch_data()
        
  
                
    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Janu@5989",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from faculty")
        data=my_cursor.fetchall()
        
        
        if len(data)!=0:
            self.faculty_table.delete(*self.faculty_table.get_children())
            for i in data:
                self.faculty_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    #get coursor
    def get_cursor(self,event=""):
        cursor_row=self.faculty_table.focus()
        content=self.faculty_table.item(cursor_row)
        data=content['values']
        
        self.var_id.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_name.set(data[2]),
        self.var_designition.set(data[3]),
        self.var_email.set(data[4]),
        self.var_cityname.set(data[5]),
        self.var_mstatus.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_idproofcombo.set(data[8]),
        self.var_idproof.set(data[9]),
        self.var_gender.set(data[10]),
        self.var_contact.set(data[11]),
        self.var_salary.set(data[12])
        
   
   
    #Reset
    def reset_data(self):
        self.var_id.set(""),
        self.var_dep.set("No selection"),
        self.var_name.set(""),
        self.var_designition.set(""),
        self.var_email.set(""),
        self.var_cityname.set(""),
        self.var_mstatus.set("No Selection"),
        self.var_dob.set(""),
        self.var_idproofcombo.set("Select ID proof"),
        self.var_idproof.set(""),
        self.var_gender.set("No Selection"),
        self.var_contact.set(""),
        self.var_salary.set("")
    #search
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Janu@5989",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from faculty where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                
                if len(data)!=0:
                    self.faculty_table.delete(*self.faculty_table.get_children())
                    for i in data:
                        self.faculty_table.insert("",END,values=i)
                        
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   
                
   #generating data set or take photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Janu@5989",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from faculty")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update faculty set dep=%s,name=%s,designition=%s,email=%s,cityname=%s,mstatus=%s,dob=%s,idproofcombo=%s,gender=%s,phone=%s,salary=%s where id=%s and idproof=%s",(
                                                                                                                                                                                                                  
                                                                                                        
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_designition.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_cityname.get(),
                                                                                                        self.var_mstatus.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_idproofcombo.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_contact.get(),
                                                                                                        self.var_salary.get(),
                                                                                                        self.var_id.get(),
                                                                                                        self.var_idproof.get() 
                                                                                                                                           
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
                        file_name_path="data_faculty/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)
                        
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  
                
                
############# Attendance in faculty portal ####################################

mydata=[]
class Attendance_FacultyPortal:##for window
    def __init__(self,root):
        self.root=root
        self.root.geometry("1430x790+0+0")#for window size
        self.root.title("Faculty Attendance Report")
        self.root.wm_iconbitmap("icon-1.ico")
       
        
        #variables########
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        #bg image
        img3=Image.open(r"C:\Face_Recognization\FRS_images\bg-1.jpg")
        img3=img3.resize((1520,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1520,height=790)
        
        
        title_label=Label(bg_img,text="Faculty Attendance Report",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1410,height=45)
        quit=Button(title_label, text="<<Back", command=self.root.destroy,bg="Red")
        quit.place(x=1150,y=10,width=70,height=35)
        
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1480,height=600) 
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Faculty Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=625,height=550)
        img_left=Image.open(r"FRS_images\faculty.jpg")
        img_left=img_left.resize((700,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        frame_label=Label(Left_frame,image=self.photoimg_left)
        frame_label.place(x=5,y=0,width=580,height=120)
        
        Left_inside_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE)
        Left_inside_frame.place(x=0,y=135,width=615,height=385)
        #attendance id
        attendanceId_label=Label(Left_inside_frame,text="AttendanceId:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceId_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_atten_id,width=22,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,pady=5,sticky=W)
        
        
        #Employee name
        name_label=Label(Left_inside_frame,text="Employee name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0)
        
        name_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_atten_name,width=22,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,pady=8,sticky=W)
        #Department
        depLabel=Label(Left_inside_frame,text="Department:",bg="white",font="comicsansns 11 bold")
        depLabel.grid(row=0,column=2)
        atten_dep=ttk.Entry(Left_inside_frame,textvariable=self.var_atten_dep,width=22,font="comicsansns 11 bold")
        atten_dep.grid(row=0,column=3,pady=8)
        
        
        
        
        
        #time
        timeLabel=Label(Left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)
        atten_time=ttk.Entry(Left_inside_frame,textvariable=self.var_atten_time,width=22,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)
        #date
        dateLabel=Label(Left_inside_frame,text="Date:",font="comicsansns 11 bold")
        dateLabel.grid(row=1,column=2,padx=20)
        atten_date=ttk.Entry(Left_inside_frame,textvariable=self.var_atten_date,width=22,font="comicsansns 11 bold")
        atten_date.grid(row=1,column=3,pady=8)
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
        
        
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),bg="yellow",fg="black",width=35)
        reset_btn.grid(row=0,column=3)
        
        showAll_btn=Button(btn_frame,text="Show all",command=self.fetch_data,font=("times new roman",12,"bold"),bg="yellow",fg="black",width=35)
        showAll_btn.grid(row=0,column=4)
        
        
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
        
        Search_label_id=Label(Search_frame,text="Id of the Employee:",bg="powder blue",font=("times new roman",12,"bold"))
        Search_label_id.grid(row=1,column=0,sticky=W)
        
        self.var_search_id=StringVar()
        Search_entry=ttk.Entry(Search_frame,textvariable=self.var_search_id,width=15,font=("times new roman",12,"bold"))
        Search_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        Search_label_date=Label(Search_frame,text="dd/mm/yy:",bg="powder blue",font=("times new roman",12,"bold"))
        Search_label_date.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        self.var_search_date=StringVar()
        Search_entry=ttk.Entry(Search_frame,textvariable=self.var_search_date,width=15,font=("times new roman",10,"bold"))
        Search_entry.grid(row=1,column=3,sticky=W)
        
        
        
        
        
        #+++++++++++++++scroll bar+++++++++++++++
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Deaprtment")
        self.AttendanceReportTable.heading("time",text="time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=150)
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
   
    # cursor 
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])     
        self.var_atten_name.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_attendance.set(rows[5])
        
    #Reset
        
    def reset_data(self):
        self.var_atten_id.set("")   
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")
        ######### Adding data to database######################333
        
    ###############fetch data#####################
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Janu@5989",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from facultyattendance")
        data=my_cursor.fetchall()
        
        
        if len(data)!=0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in data:
                self.AttendanceReportTable.insert("",END,values=i)
            conn.commit()
        conn.close() 
                
    #search
    def search_data(self):
        #if self.var_com_search.get()=="" or self.var_search.get()=="":
            #messagebox.showerror("Error","Please select option")
        #else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Janu@5989",database="face_recognition")
                my_cursor=conn.cursor()
                
                if self.var_com_search.get()=="" or self.var_search.get()=="" and self.var_search_id.get()!="" and self.var_search_date.get()!="" :
                    my_cursor.execute("select * from facultyattendance where id LIKE '%"+str(self.var_search_id.get())+"%' and date LIKE '%"+str(self.var_search_date.get())+"%'")
                elif self.var_com_search.get()!="" or self.var_search.get()!="":
                    my_cursor.execute("select * from facultyattendance where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                else:
                    messagebox.showerror("Error","Enter valid data",parent=self.root)
                    
                data=my_cursor.fetchall()
                if len(data)==0:
                    messagebox.showerror("Error","Data Not found",parent=self.root)
                
                if len(data)!=0:
                    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                    for i in data:
                        self.AttendanceReportTable.insert("",END,values=i)
                        
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
                
             
   
        

            
               
            
                
            
        
        
        
        
        
    
        
  


           
        
                                                                                                
        
        
        
        
        
              
        
        
        
           
        
        
        
        
       
        
        
        
        
    
        
        

        
   
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System_faculty(root)
    root.mainloop()