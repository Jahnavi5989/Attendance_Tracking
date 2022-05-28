from tkinter import*
from tkinter import ttk
from pil import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
import os
import mysql.connector
import cv2
import numpy as np


class Train:##for window
    def __init__(self,root):
        self.root=root
        self.root.attributes('-fullscreen', True)#for window size
        self.root.title("Train DataSet")
        self.root.wm_iconbitmap("icon-1.ico")
        #title_label=Label(self.root,text="Train DataSet",font=("times new roman",35,"bold"),bg="blue",fg="powderblue")
        #title_label.pack(pady=10)
        
        ############ back ground pic
        img3=Image.open(r"FRS_images\train_dataset1.jpg")
        img3=img3.resize((1300,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1250,height=690)
        
        quit=Button(bg_img, text="<<Back", command=self.root.destroy,bg="Red")
        quit.place(x=1150,y=50,width=70,height=35)
        
        
        
        img4=Image.open(r"FRS_images\traindata_inside.jpg")
        img4=img4.resize((520,390),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.train_classifier)
        b1.place(x=200,y=100,width=420,height=420)
        
        b2=Button(bg_img,text="Train Student System",cursor="hand2",command=self.train_classifier,font=("times new roman",12,"bold"),bg="Light green",fg="white")
        b2.place(x=200,y=500,width=420,height=50)
    def train_classifier(self):
        try:
            
            data_dir=("data")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
            faces=[]
            ids=[]
        
            for image in path:
                img=Image.open(image).convert('L')##gray scale image
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])
            
            
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)
        
         #+++++training the calssifier and save
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write(r"xmlfiles\classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training datasets completed!!")   
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                 
            
        
        
if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()           
        