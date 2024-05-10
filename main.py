from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognizer import Face_recognization


class Face_Recognition_System:
    
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # Set the background color of the main window
        self.root.configure(bg="lightblue")
        # Add a title label
        title_label = Label(self.root, text="Face Recognition System Software", font=("Helvetica", 16), bg="lightblue")
        title_label.pack(pady=20)  # Adjust pady as needed

        # # Add a styled button
        # styled_button = Button(self.root, text="Click Me", command=self.button_click, bg="green", fg="white", font=("Helvetica", 12))
        # styled_button.pack(pady=10, padx=20)  # Adjust pady and padx as needed

        #student details button
        img1 = Image.open(r"C:\Jeevesh\me\face_attendence\images\student.jpg")
        img1 = img1.resize((220, 220), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1=Button(image=self.photoimg1,command=self.student_details,  cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(text="Student Details", command=self.student_details, cursor="hand2", )
        b1_1.place(x=200,y=300,width=220,height=40)

        #detect face
        img2 = Image.open(r"C:\Jeevesh\me\face_attendence\images\cam.jpg")
        img2 = img2.resize((220, 220), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2=Button(image=self.photoimg2, cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)

        b2_2=Button(text="Detect Face", cursor="hand2",command=self.face_data)
        b2_2.place(x=500,y=300,width=220,height=40)

        #Attendance
        img3 = Image.open(r"C:\Jeevesh\me\face_attendence\images\attendance.jpg")
        img3 = img3.resize((220, 220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b3=Button(image=self.photoimg3, cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)

        b3_3=Button(text="Attendence", cursor="hand2", )
        b3_3.place(x=800,y=300,width=220,height=40)

        #Train new face
        img4 = Image.open(r"C:\Jeevesh\me\face_attendence\images\train.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b4=Button(image=self.photoimg4, cursor="hand2", command=self.train_data)
        b4.place(x=1100,y=100,width=220,height=220)

        b4_4=Button(text="Train New Face", cursor="hand2", command=self.train_data)
        b4_4.place(x=1100,y=300,width=220,height=40)

        #photo
        img5 = Image.open(r"C:\Jeevesh\me\face_attendence\images\photo.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b5=Button(image=self.photoimg4, cursor="hand2",command=self.open_img)
        b5.place(x=200,y=400,width=220,height=220)

        b5_5=Button(text="Photos", cursor="hand2",command=self.open_img)
        b5_5.place(x=200,y=600,width=220,height=40)


    def open_img(self):
        os.startfile(r"C:\Jeevesh\me\face_attendence\data")


    #=======function buttons===========#
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.new_window.geometry("800x600")  # Set the geometry of the new window
        self.new_window.title("Student Details")  # Set the title of the new window
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        # self.new_window.geometry("800x600")  # Set the geometry of the new window
        # self.new_window.title("Student Details")  # Set the title of the new window
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        # self.new_window.geometry("800x600")  # Set the geometry of the new window
        # self.new_window.title("Student Details")  # Set the title of the new window
        self.app=Face_recognization(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

    