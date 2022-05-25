from tkinter import*
from tkinter import ttk
from pil import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import cv2


class Employee:
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
        
        btn_add=Button(upper_frame,text="Save",command=self.add_data,font=("arial",15,"bold"),width=10,bg='blue',fg='white')
        btn_add.grid(row=0,column=6,padx=1,pady=5)
        
        btn_delete=Button(upper_frame,text="Delete",command=self.delete_data,font=("arial",15,"bold"),width=9,bg='blue',fg='white')
        btn_delete.grid(row=0,column=7,padx=1,pady=5)
        
        btn_update=Button(upper_frame,text="Update",command=self.update_data,font=("arial",15,"bold"),width=10,bg='blue',fg='white')
        btn_update.grid(row=1,column=6,padx=1,pady=5)
        
        btn_reset=Button(upper_frame,text="Reset",command=self.reset_data,font=("arial",15,"bold"),width=9,bg='blue',fg='white')
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
        
        btn_show_all=Button(search_frame,text="Show all",command=self.fetch_data,font=("arial",13,"bold"),width=9,bg='red',fg='white')
        btn_show_all.grid(row=0,column=4,padx=1,pady=5)
        
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
        
        ########## Function declarations ##############
    def add_data(self):
        if self.var_id.get()=="" or self.var_dep.get()=="": #or self.var_name.get()=="" or self.var_designition.get()=="" or self.var_email.get()=="" or self.var_city.get()=="" or self.var_mstatus.get()=="" or self.var_dob.get()=="" or self.var_idproofcombo.get()=="" or self.var_idproof.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_salary.get()=="":
            messagebox.showerror("Error","Please fill all the required fields")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Janu@5989",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute('insert into faculty values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                        self.var_id.get(),
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_designition.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_cityname.get(),
                                                                                                        self.var_mstatus.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_idproofcombo.get(),
                                                                                                        self.var_idproof.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_contact.get(),
                                                                                                        self.var_salary.get() 
                                                                                                                                                                    
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Faculty details added succesfully',parent=self.root)
            except Exception as ex:
                messagebox.showerror('Error',f"Due To : {str(ex)}",parent=self.root)
                
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
        
            #++++++++++++++++++++++++++++++UPADTE FUNCTION+++++++++++++++++++++++++++#
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Upadte","Do you want to update this faculty details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Janu@5989",database="face_recognition")
                    my_cursor=conn.cursor()
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
                else:
                    if not Update:
                        return  
                messagebox.showinfo("Success","faculty details successfully update completed",parent=self.root)      
                conn.commit()
                self.fetch_data()
                conn.close
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    #delete data
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Faculty Employee Id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this faculty details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Janu@5989",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from faculty where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Delete","Successfully deleted faculty details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  
                
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
            messagebox.showerror("Error","Please select option",parent=self.root)
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
                
                

        
        

           
        
                                                                                                
        
        
        
        
        
              
        
        
        
           
        
        
        
        
       
        
        
        
        
    
        
        
if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
        
        
