from tkinter import*
from tkinter import ttk
from pil import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import webbrowser
import os


class Help:##for window
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")#for window size
        self.root.title("Help Desk")
        quit=Button(self.root, text="Back", command=self.root.destroy,bg="Red")
        quit.place(x=1300,y=10,width=100,height=35)
        #bg image
        img3=Image.open(r"FRS_images\help_desk_bg.jpg")
        img3=img3.resize((1300,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1250,height=690)
        
        quit=Button(bg_img, text="<<Back", command=self.root.destroy,bg="Red")
        quit.place(x=1150,y=50,width=70,height=35)
        
        email_label=Label(bg_img,text="Send us an Email @ Attendancesystem@gamil.com",font=("times new roman",20,"bold"),bg="white",fg="black")
        email_label.place(x=60,y=10,width=1010,height=100)
        
        label=Label(bg_img,text="Connect to us",font=("times new roman",15,"bold"),bg="white",fg="black")
        label.place(x=60,y=75,width=1010,height=100)
        
        def open_insta():
            webbrowser.open_new("https://www.instagram.com/accounts/login/")       
        
        btn_insta=Button(bg_img,text="Instagram",font=("Helvetica",34),command=open_insta,bg='powder blue',fg='white')
        btn_insta.place(x=500,y=145,width=230,height=50) 
        
        def open_facebook():
            webbrowser.open_new("https://about.facebook.com/")   
            
        btn_face=Button(bg_img,text="Facebook",font=("Helvetica",34),command=open_facebook,bg='powder blue',fg='white')
        btn_face.place(x=500,y=225,width=230,height=50) 
        
        def open_twitter():
            webbrowser.open_new("https://twitter.com/i/flow/login")   
            
        btn_face=Button(bg_img,text="Twitter",font=("Helvetica",34),command=open_twitter,bg='powder blue',fg='white')
        btn_face.place(x=500,y=300,width=230,height=50)     
        
        
        
       
    
        
        
    
    
        
       
        
        
       
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()        