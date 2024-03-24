from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data Set")
        # Set the background color of the main window
        self.root.configure(bg="lightblue")
        # Add a title label
        title_label = Label(self.root, text="Train Data Set", font=("Helvetica", 16), bg="lightblue")
        title_label.pack(pady=20)  # Adjust pady as needed

        b1_1=Button(text="Train Data", command=self.train_classifier,cursor="hand2", )
        b1_1.place(x=650,y=380,width=220,height=60)

    def train_classifier(self):
        data_dir=(r"C:\Jeevesh\me\face_attendence\data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1] )

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        #<=====Train the classifier and save=====>
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write(r"C:\Jeevesh\me\face_attendence\classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed")






if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()