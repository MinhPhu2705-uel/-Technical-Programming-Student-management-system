
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from pymongo import *
import datetime
from tkinter import ttk
import tkinter.messagebox as mb
from tkinter import *
from PIL import Image
from PIL import ImageTk
from Exam import ExamWindow
from Student import StudentWindow
from Library import LibraryWindow
from Staff import StaffWindow

 
class Menu:
        def __init__(self,window):
                self.master = window
                self.master.title("Menu")
                self.master.geometry('700x600')
                self.master.configure(background="white")
                self.master.resizable(False,False)
                
                self.img_student = Image.open('Image/Student.png')
                self.img_student.thumbnail((190,190))
                self.new_img_student = ImageTk.PhotoImage(self.img_student)

                self.img_exam = Image.open('Image/Exam.png')
                self.img_exam.thumbnail((190,190))
                self.new_img_exam = ImageTk.PhotoImage(self.img_exam)


                self.img_staff = Image.open('Image/Staff.png')
                self.img_staff.thumbnail((190,190))
                self.new_img_staff = ImageTk.PhotoImage(self.img_staff)


                self.img_lib = Image.open('Image/Library.png')
                self.img_lib.thumbnail((190,190))
                self.new_img_lib = ImageTk.PhotoImage(self.img_lib)

                



                self.frame_header=Frame(window, bg='#fff')
                self.frame_header.pack(fill=X)
                self.frame_menu=Frame(window, bg='#fff',background="royalblue")
                self.frame_menu.pack(pady=10)

                self.heading=Label(self.frame_header, text='Student Management System', fg="black", bg='white', font=('Microsoft Yahei UI', 30, 'bold'))
                self.heading.pack(pady=20)
                self.button_student=Button(self.frame_menu,image=self.new_img_student,fg="#57a1f8", bg='white',bd = 0, height=230,width=230, background= "mintcream",command=self.student)
                self.button_student.grid(row=0,column=0)

                self.button_student=Button(self.frame_menu,image=self.new_img_staff,fg="#57a1f8", bg='white',bd = 0, height=230,width=230,command=self.staff)
                self.button_student.grid(row=0, column=1)

                self.button_student=Button(self.frame_menu,image=self.new_img_exam,fg="#57a1f8", bg='white',bd = 0, height=230,width=230,command=self.exam)
                self.button_student.grid(row=1, column=0)

                self.button_student=Button(self.frame_menu,image=self.new_img_lib,fg="#57a1f8", bg='white',bd = 0 ,height=230,width=230,command=self.library)
                self.button_student.grid(row=1, column=1)

        


        def student(self):
                std = StudentWindow()

        def exam(self):
                exm = ExamWindow()

        def library(self):
                lib = LibraryWindow()

        def staff(self):
                stf = StaffWindow()








window = Tk()
std = Menu(window)
window.mainloop()