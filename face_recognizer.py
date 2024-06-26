from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_recognization:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Recognize Face")
        # Set the background color of the main window
        self.root.configure(bg="lightblue")
        # Add a title label
        title_label = Label(self.root, text="Recognize Face", font=("Helvetica", 16), bg="lightblue")
        title_label.pack(pady=20)  # Adjust pady as needed

        b1_1=Button(text="Recognize Face",cursor="hand2", command=self.face_recog)
        b1_1.place(x=650,y=380,width=220,height=60)


    #<======Atttendance=======>
    def mark_attendance(self,i,r,n,d):  #n and i are student id and name retirved from databse whihch is mentioned below(data to be displayed on the box)
        with open(r"C:\Jeevesh\me\face_attendence\Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


    #<======Face Recognition=======>
    def face_recog(self):
        # def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
        #     gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #     features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

        #     for (x, y, w, h) in features:
        #         cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        #         roi_gray = gray_image[y:y+h, x:x+w]
        #         id_, predict = clf.predict(roi_gray)
        #         confidence = int((100 * (1 - predict / 300)))

        #         if confidence > 75:
        #             conn = mysql.connector.connect(host="localhost", username="root", password="J2304@PJN#", database="face_recognizer")
        #             my_cursor = conn.cursor()

        #             my_cursor.execute("SELECT student_name FROM student WHERE student_id=" + str(id_))
        #             n = my_cursor.fetchone()
        #             n = "+".join(n)

        #             # Selecting student ID for attendance update
        #             i = str(id_)  # Convert ID to string
        #             r = i  # Using ID as roll number if roll number is not available
        #             d = "Dep"  # Department placeholder
        #             cv2.putText(img, f"ID: {i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
        #             cv2.putText(img, f"Name: {n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
        #             self.mark_attendance(i, r, n, d)
        #         else:
        #             cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
        #             cv2.putText(img, "Unknown Face", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

        #     return img

        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost", username="root",password="J2304@PJN#",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select student_name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                #selecting student id for attendance update
                my_cursor.execute("select student_id from student where student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select roll_no from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r=str(r[0])  # Convert roll number to string before joining
                r="+".join(r)

                my_cursor.execute("select Dep from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                if confidence>75:
                    cv2.putText(img, f"ID:{i}", (x,y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Name:{n}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown Face", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img

        faceCascade=cv2.CascadeClassifier(r"C:\Jeevesh\me\face_attendence\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()      
        clf.read(r"C:\Jeevesh\me\face_attendence\classifier.xml")  

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



                    
if __name__ == "__main__":
    root=Tk()
    obj=Face_recognization(root)
    root.mainloop()