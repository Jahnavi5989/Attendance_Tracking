from tkinter import*
from tkinter import ttk
from pil import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
import os
import mysql.connector
import cv2
import csv
from tkinter import filedialog
import sqlite3

mydata=[]
class Attendance:##for window
    def __init__(self,root):
        self.root=root
        self.root.attributes('-fullscreen', True)#for window size
        self.root.title("Student Attendance Report")
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
        img3=Image.open(r"FRS_images\bg-1.jpg")
        img3=img3.resize((1520,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1520,height=790)
        
        
        title_label=Label(bg_img,text="Student Attendance Report",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1410,height=45)
        quit=Button(title_label, text="<<Back", command=self.root.destroy,bg="Red")
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
        
        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        import_btn.grid(row=0,column=0)
        
        Export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        Export_btn.grid(row=0,column=1)
        
        save_btn=Button(btn_frame,text="Save to Database",command=self.add_data,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        save_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        reset_btn.grid(row=0,column=3)
        
        showAll_btn=Button(btn_frame,text="Show all",command=self.fetch_data,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        showAll_btn.grid(row=0,column=4)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",12,"bold"),bg="yellow",fg="black",width=10)
        update_btn.grid(row=0,column=5)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",12,"bold"),bg="yellow",fg="black",width=8)
        delete_btn.grid(row=0,column=6)
        
        
        
        
        
        
        
        
        
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
            
    #import csv        
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata) 
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                export_write=csv.writer(myfile,delimiter=",")             
                for i in mydata:
                    export_write.writerow(i)
                    messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   
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
        ######### Adding data to database######################333
        
    def add_data(self):
        conn=sqlite3.connect(r'database\face_recognition.db')
        my_cursor=conn.cursor()
        
        try:
            my_cursor.execute("insert into attendance values(?,?,?,?,?,?,?)",(
                                                                                             self.var_atten_id.get(),
                                                                                             self.var_atten_roll.get(),       
                                                                                             self.var_atten_name.get(),
                                                                                             self.var_atten_dep.get(),
                                                                                             self.var_atten_time.get(),
                                                                                             self.var_atten_date.get(),
                                                                                             self.var_atten_attendance.get()
                                                                                                             
                                    
                                                                                                          ))
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("success","Saved Attendance status successfully to the database",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 
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
    def update_data(self):
        if self.var_atten_dep.get()=="Select Department" or self.var_atten_name.get()=="" or self.var_atten_attendance.get()=="Status" or self.var_atten_roll.get()=="" or self.var_atten_dep.get()=="" or self.var_atten_time.get()=="" or self.var_atten_date.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=sqlite3.connect(r'database\face_recognition.db')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update attendance set roll=?,name=?,department=?,time=?,attendance=? where id=? and date=?",(
                                                                                             self.var_atten_roll.get(),       
                                                                                             self.var_atten_name.get(),
                                                                                             self.var_atten_dep.get(),
                                                                                             self.var_atten_time.get(),
                                                                                             self.var_atten_attendance.get(),
                                                                                             self.var_atten_id.get(),
                                                                                             self.var_atten_date.get()                                                                                                                                                                                          
                                                                                                             
                                                                                                                                           
                    ))
                else:
                    if not Update:
                        return  
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)      
                conn.commit()
                self.fetch_data()
                conn.close
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
                
     #delete data
    def delete_data(self):
        if self.var_atten_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this student details",parent=self.root)
                if delete>0:
                    conn=sqlite3.connect(r'database\face_recognition.db')
                    my_cursor=conn.cursor()
                    sql="delete from attendance where id=?"
                    val=(self.var_atten_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
                
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
                    messagebox.showerror("Error","No data found")
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
    obj=Attendance(root)
    root.mainloop()       