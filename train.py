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



#<======== Different UI =========>#
# import tkinter as tk
# from tkinter import Button, Label, messagebox, ttk, filedialog
# from PIL import Image, ImageTk
# import os
# import numpy as np
# import cv2

# class Train:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Train Data Set")
#         self.root.configure(bg="white")

#         # Initialize the directory path variable
#         self.data_dir = None

#         # Set window size to fit the normal screen size of a laptop
#         screen_width = root.winfo_screenwidth()
#         screen_height = root.winfo_screenheight()
#         window_width = int(screen_width * 0.6)
#         window_height = int(screen_height * 0.6)
#         window_x = (screen_width - window_width) // 2
#         window_y = (screen_height - window_height) // 2
#         self.root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#         self.title_label = Label(self.root, text="Train Data Set", font=("Helvetica", 20, "bold"), bg="white")
#         self.title_label.pack(pady=10)

#         self.select_dir_label = Label(self.root, text="Selected Directory: None", font=("Helvetica", 12), bg="white")
#         self.select_dir_label.pack(pady=5)

#         self.select_button = Button(self.root, text="Browse", command=self.browse_directory, cursor="hand2", bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
#         self.select_button.pack(pady=5)

#         self.progress_label = Label(self.root, text="Progress:", font=("Helvetica", 12), bg="white")
#         self.progress_label.pack(pady=5)

#         self.progress_bar = ttk.Progressbar(self.root, orient='horizontal', length=300, mode='determinate')
#         self.progress_bar.pack(pady=5)

#         self.train_button = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2", bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
#         self.train_button.pack(pady=10)

#         # Center the window
#         self.root.eval('tk::PlaceWindow . center')

#     def browse_directory(self):
#         self.data_dir = filedialog.askdirectory()
#         if self.data_dir:
#             self.select_dir_label.config(text=f"Selected Directory: {self.data_dir}")
#         else:
#             messagebox.showerror("Error", "Please select a directory")

#     def train_classifier(self):
#         if not self.data_dir:
#             messagebox.showerror("Error", "Please select a directory")
#             return

#         path = [os.path.join(self.data_dir, file) for file in os.listdir(self.data_dir)]
#         total_images = len(path)
#         progress_step = 100 / total_images

#         faces = []
#         ids = []

#         for index, image in enumerate(path):
#             # Check if the file is an image
#             if image.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
#                 img = Image.open(image).convert('L')
#                 image_np = np.array(img, 'uint8')
#                 id = int(os.path.split(image)[1].split('.')[1])

#                 faces.append(image_np)
#                 ids.append(id)

#                 # Update progress bar
#                 self.progress_bar['value'] = (index + 1) * progress_step
#                 self.root.update_idletasks()

#         ids = np.array(ids)

#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.train(faces, ids)
#         clf.write(os.path.join(self.data_dir, "classifier.xml"))

#         messagebox.showinfo("Result", "Training datasets completed")

# if __name__ == "__main__":
#     root = tk.Tk()
#     obj = Train(root)
#     root.mainloop()
