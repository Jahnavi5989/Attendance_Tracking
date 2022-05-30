from tkinter import*
from tkinter import ttk
from pil import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
import os
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import numpy as np
import sqlite3


class Face_Recognition_faculty:##for window
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x790+0+0")#for window size
        self.root.title("Faculty Face Detector")
        self.root.wm_iconbitmap("icon-1.ico")
        #title_label=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="Dark Blue")
        #title_label.place(x=0,y=0,width=1530,height=45)
        #quit=Button(title_label, text="Back", command=self.root.destroy,bg="Red")
        #quit.place(x=1150,y=10,width=70,height=35)
        
        
        img3=Image.open(r"FRS_images\newbg_cartoon.jpeg")
        img3=img3.resize((1520,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1520,height=790)
        
        b2=Button(bg_img,text="Scan face",cursor="hand2",command=self.face_recog,font=("times new roman",12,"bold"),bg="Dark Blue",fg="white")
        b2.place(x=200,y=530,width=420,height=50)
        
        quit=Button(bg_img, text="<<Back", command=self.root.destroy,bg="Red")
        quit.place(x=1150,y=10,width=70,height=35)
        
    # ==================marking attendance========================
    def mark_attendance(self,i,n,d):
        with open(r"Attendance\Attendance_faculty.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))    
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{dtString},{d1},Present")
                
                
                
            
        
        
    #___________face recognition_______________________
    def face_recog(self):
        
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                
                conn=sqlite3.connect(r'database\face_recognition.db')
                my_cursor=conn.cursor()
                
                my_cursor.execute("select name from faculty where id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select dep from faculty where id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                my_cursor.execute("select id from faculty where id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                
                if confidence>78:
                    cv2.putText(img,f"Employee ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255))
                    #cv2.putText(img,f"Designition:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255))
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255))
                    cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255))
                    
                    self.mark_attendance(i, n, d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3) 
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3)
                
                
                coord=[x,y,w,h]  
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier(r"xmlfiles\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"xmlfiles\classifier_fac.xml")
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img, clf, faceCascade)
            cv2.imshow("Taking Attendance",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()    
        
                
                       
                     
                    
                    
                
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_faculty(root)
    root.mainloop()          