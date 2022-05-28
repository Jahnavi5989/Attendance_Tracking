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
from train import Train
from face_recognition_faculty import Face_Recognition_faculty
from attendance_faculty import Attendance_Faculty
from time import strftime
from datetime import datetime
import tkinter
import os
import pyttsx3
import sqlite3


class Face_Recognition_System_admin:##for window
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
        
        lblportal=Label(bg_img,text="Admin Portal",font=('times new roman',14,'bold'),background='Gray',foreground='Red')
        lblportal.place(x=1000,y=0,width=210,height=50)     
        
        #details button
        img4=Image.open(r"FRS_images\student_details.png")
        img4=img4.resize((140,190),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=220)
        
        b2=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",bg="white")
        b2.place(x=100,y=300,width=220,height=40)
        
        #Faculty details
        img9=Image.open(r"FRS_images\dataset.jpg")
        img9=img9.resize((160,190),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b11=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.faculty_details)
        b11.place(x=400,y=100,width=220,height=220)
        
        b12=Button(bg_img,text="Faculty Details",cursor="hand2",bg="white",command=self.faculty_details)
        b12.place(x=400,y=300,width=220,height=40)
        #Datasets of student
        img5=Image.open(r"FRS_images\attendance.png")
        img5=img5.resize((160,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b3=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.open_img_student)
        b3.place(x=400,y=380,width=220,height=220)  
        
        b4=Button(bg_img,text="Student dataset",cursor="hand2",bg="white",command=self.open_img_student)
        b4.place(x=400,y=580,width=220,height=40)  
        
        #Attendance button
        img6=Image.open(r"FRS_images\attendance_report.jpg")
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
        
        b14=Button(bg_img,text="Faculty Attendance report",cursor="hand2",bg="white",command=self.faculty_attendance_data)
        b14.place(x=1000,y=300,width=220,height=40)
        
       
        
        #Train student dataset
        
        img8=Image.open(r"FRS_images\train_dataset.jpg")
        img8=img8.resize((200,190),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b9=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b9.place(x=100,y=380,width=220,height=220)
        
        b10=Button(bg_img,text="Train Student System",cursor="hand2",bg="white",command=self.train_data)
        b10.place(x=100,y=580,width=220,height=40)
        
        #faculty data set

        img7=Image.open(r"FRS_images\help_desk.jpg")
        img7=img7.resize((160,190),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b7=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.open_img_faculty)
        b7.place(x=1000,y=380,width=220,height=220)
        
        b8=Button(bg_img,text="Faculty Dataset",cursor="hand2",bg="white",command=self.open_img_faculty)
        b8.place(x=1000,y=580,width=220,height=40)
        
        
        
        #Train faculty dataset
       
        img10=Image.open(r"FRS_images\train_dataset.jpg")
        img10=img10.resize((160,190),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b11=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.train_faculty_data)
        b11.place(x=700,y=380,width=220,height=220)
        
        b12=Button(bg_img,text="Train Faculty system",cursor="hand2",bg="white",command=self.train_faculty_data)
        b12.place(x=700,y=580,width=220,height=40)
        
        
        
        
         
        
    
       
        
    #_______________________buttons functions______________#
    def open_img_faculty(self):
        os.startfile("data_faculty") 
    def open_img_student(self):
        os.startfile("data")
    def student_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Student(self.new_window)  
    def faculty_details(self):
        
        self.new_window=Toplevel(self.root)
        self.app=Employee(self.new_window) 
    def faculty_attendance_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Attendance_Faculty(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)  
    def train_faculty_data(self):
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
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System_admin(root)
    root.mainloop()