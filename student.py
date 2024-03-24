from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # Set the background color of the main window
        self.root.configure(bg="lightblue")
        # Add a title label
        title_label = Label(self.root, text="Student", font=("Helvetica", 16), bg="lightblue")
        title_label.pack(pady=20)  # Adjust pady as needed

        #<======variables======>#
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()

        main_frame=Frame(bd=2)
        main_frame.place(x=15, y=60, width=1500, height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details")
        Left_frame.place(x=15, y=10, width=730, height=580)

        img_left = Image.open(r"C:\Jeevesh\me\face_attendence\images\student.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current course")
        current_course_frame.place(x=5, y=135, width=720, height=115)

        #department
        dep_label=Label(current_course_frame,text="Department")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,width=17,state="read only")
        dep_combo['values']=("Select Department","Computer","IT","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #course
        course_label=Label(current_course_frame,text="Course")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,width=17,state="read only")
        course_combo['values']=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,width=17,state="read only")
        year_combo['values']=("Select Year","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=17,state="read only")
        semester_combo['values']=("Select semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student info
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information")
        class_student_frame.place(x=5, y=250, width=720, height=300)

        #student id
        student_id_label=Label(class_student_frame,text="Student ID")
        student_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20)
        student_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #student name
        student_name_label=Label(class_student_frame,text="Student Name")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20)
        student_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #student division
        student_division_label=Label(class_student_frame,text="Class Division")
        student_division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        # student_division_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20)
        # student_division_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,width=17,state="read only")
        div_combo['values']=("A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #roll no
        roll_no_label=Label(class_student_frame,text="Roll No")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20)
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,width=17,state="read only")
        gender_combo['values']=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #Email id
        email_label=Label(class_student_frame,text="Email")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20)
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        #phone no address can be added

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame, variable=self.var_radio1,text="Take photo sample", value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame, variable=self.var_radio1,text="No photo sample", value="No")
        radiobtn2.grid(row=6, column=1)

        #button frame
        btn_frame=Frame(class_student_frame, bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=715,height=35)
        
        save_btn=Button(btn_frame, text="Save",command=self.add_data,width=17)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame, text="Update",command=self.update_data,width=17)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame, text="Delete",command=self.delete_data,width=17)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame, text="Reset",command=self.reset_data,width=17)
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame, bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=235,width=715,height=35)
        
        take_photo_sample_btn=Button(btn_frame1,command=self.generate_dataset, text="Take Photo",width=35)
        take_photo_sample_btn.grid(row=0,column=0)

        update_photo_sample_btn=Button(btn_frame1, text="Update Photo",width=35)
        update_photo_sample_btn.grid(row=0,column=1)



        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details")
        Right_frame.place(x=750, y=10, width=720, height=580)

        img_right = Image.open(r"C:\Jeevesh\me\face_attendence\images\student.jpg")
        img_right = img_right.resize((720, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame, image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #<------Search System------>#
        Search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search system")
        Search_frame.place(x=5, y=135, width=710, height=70)

        search_label=Label(Search_frame,text="Search By")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,width=17,state="read only")
        search_combo['values']=("Select","Roll_No")
        #can add more values for searching
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10)

        Search_entry=ttk.Entry(Search_frame,width=20)
        Search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn=Button(Search_frame, text="Search",width=12)
        search_btn.grid(row=0,column=3, padx=4)

        showAll_btn=Button(Search_frame, text="Show All",width=12)
        showAll_btn.grid(row=0,column=4,padx=4)

        #<------Table frame------>#
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","email","photo"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student_ID")
        self.student_table.heading("name",text="Student_name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll_No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #<======Function declaration======>
    def add_data(self):
        #validation
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root",password="J2304@PJN#",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_id.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_email.get(),
                            self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student deatils has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    #<=======Fetch Data=======>
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root",password="J2304@PJN#",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #<=======Get cursor=======>
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_email.set(data[9]),
        self.var_radio1.set(data[10])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update", "Do you want to update Student details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost", username="root",password="J2304@PJN#",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,semester=%s,`div`=%s,roll_no=%s,gender=%s,email=%s,PhotoSample=%s where student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error", "Student ID required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page", "Do you want to delete the student detail", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root",password="J2304@PJN#",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfullly deteled", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("Select Department")
        self.var_gender.set("Select Gender")
        self.var_email.set("")

    #<======Generate data set or take photo sample======>
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="J2304@PJN#",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,semester=%s,student_name=%s,`div`=%s,roll_no=%s,gender=%s,email=%s,PhotoSample=%s where student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get(),
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #<=====Load predefined data on face from opencv======>
                face_classifier=cv2.CascadeClassifier(r"C:\Jeevesh\me\face_attendence\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #1.3 is caling factor
                    #minimum neighbour is 5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                id = myresult[-1][4] if myresult else 0
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path=r"C:\Jeevesh\me\face_attendence\data\user."+str(myresult[-1][4])+"."+str(img_id)+".jpg"
                        # print("Saving image to:", file_name_path)
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50, 50), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed.")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)














if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()