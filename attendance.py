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
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Recognize Face")
        # Set the background color of the main window
        self.root.configure(bg="lightblue")
        # Add a title label
        title_label = Label(self.root, text="Attendace", font=("Helvetica", 16), bg="lightblue")
        title_label.pack(pady=20)  # Adjust pady as needed

        #variable

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        main_frame=Frame(bd=2)
        main_frame.place(x=15, y=60, width=1500, height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details")
        Left_frame.place(x=15, y=10, width=730, height=580)

        img_left = Image.open(r"C:\Jeevesh\me\face_attendence\images\student.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE)
        left_inside_frame.place(x=0, y=135, width=720, height=370)

        #labels and entries
        #attendance id
        attendance_id_label=Label(left_inside_frame,text="Attendance ID :")
        attendance_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendance_id_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id)
        attendance_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #roll no
        roll_no_label=Label(left_inside_frame,text="Roll No :")
        roll_no_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll)
        roll_no_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #Name
        name_label=Label(left_inside_frame,text="Name :")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name)
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        #department
        dep_label=Label(left_inside_frame,text="Department :")
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep)
        dep_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #Time
        time_label=Label(left_inside_frame,text="Time :")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time)
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #date
        date_label=Label(left_inside_frame,text="Date :")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date)
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #attendance status
        attendance_label=Label(left_inside_frame,text="Attendance Status :")
        attendance_label.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,state="readonly")
        self.atten_status["values"]=("Status","Present","Avsent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current

        #buttons
        btn_frame=Frame(left_inside_frame, bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=715,height=35)
        
        impoer_csv_btn=Button(btn_frame, text="Import CSV",command=self.importCsv,width=17)
        impoer_csv_btn.grid(row=0,column=0)

        export_csv_btn=Button(btn_frame, text="Export CSV",command=self.exportCsv,width=17)
        export_csv_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame, text="Update",width=17)
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame, text="Reset",width=17,command=self.reset_data)
        reset_btn.grid(row=0,column=3)



        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details")
        Right_frame.place(x=750, y=10, width=720, height=580)

        table_frame=Label(Right_frame, bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=700,height=455)

        #scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Student Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")

        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #<======Fetch data=========>
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())    
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv file
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    #export csv file
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data", "No Data foubd to export", parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                    messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"successfully")
        
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

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
        self.var_atten_attendance.set("")



    



        


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()