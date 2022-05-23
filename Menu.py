
from tkinter import *
from PIL import ImageTk
from pymongo import *
from tkinter import *
from PIL import Image
from PIL import ImageTk
from Exam import ExamWindow
from Student import StudentWindow
from Library import LibraryWindow
from Staff import StaffWindow
 
class Menu_Window:
        def __init__(self,window):
                self.master = window
                self.master.title("Menu")
                # self.master.geometry('700x600')
                self.master.configure(background="white")
                self.master.resizable(False,False)

                self.window_width = 700
                self.window_height = 650
                self.screen_width = window.winfo_screenwidth()
                self.screen_height = window.winfo_screenheight()
                # print("Width: ", screen_width, "Height: ", screen_height)
                self.x = ( self.screen_width / 2) - ( self.window_width / 2)
                self.y = ( self.screen_height / 2) - ( self.window_height / 2)-30
                self.master.geometry(f"{ self.window_width}x{ self.window_height}+{int( self.x)}+{int( self.y)}")
                                
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

                
                self.img_exit = Image.open('Image/Exit.png')
                self.img_exit.thumbnail((70,70))
                self.new_img_exit = ImageTk.PhotoImage(self.img_exit)

                # self.img_re = Image.open('Image/return_icon.png')
                # self.img_re.thumbnail((70,70))
                # self.new_img_re = ImageTk.PhotoImage(self.img_re)



                

                self.frame_header=Frame(window, bg='#fff')
                self.frame_header.pack(fill=X)
                self.frame_menu=Frame(window, bg='#fff')
                self.frame_menu.pack(pady=10)
                self.frame_bottom=Frame(window, bg='#fff')
                self.frame_bottom.pack(fill=X)


                self.heading=Label(self.frame_header, text='University Management System', fg="black", bg='white', font=('Microsoft Yahei UI', 30, 'bold'))
                self.heading.pack(pady=10)
                self.button_student=Button(self.frame_menu,image=self.new_img_student,fg="#57a1f8", bg='white',bd = 0, height=230,width=230, background= "mintcream",command=self.student)
                self.button_student.grid(row=0,column=0)

                self.button_staff=Button(self.frame_menu,image=self.new_img_staff,fg="#57a1f8", bg='white',bd = 0, height=230,width=230,command=self.staff)
                self.button_staff.grid(row=0, column=1)

                self.button_exam=Button(self.frame_menu,image=self.new_img_exam,fg="#57a1f8", bg='white',bd = 0, height=230,width=230,command=self.exam)
                self.button_exam.grid(row=1, column=0)

                self.button_lib=Button(self.frame_menu,image=self.new_img_lib,fg="#57a1f8", bg='white',bd = 0 ,height=230,width=230,command=self.library)
                self.button_lib.grid(row=1, column=1)



                self.button_exit=Button(self.frame_bottom,image=self.new_img_exit, bg='white',bd = 0,command=self.log_out)
                self.button_exit.pack(side=RIGHT, padx=20)

                # self.button_return=Button(self.frame_bottom,image=self.new_img_re,fg="#57a1f8", bg='white',bd = 0)
                # self.button_return.pack(side=LEFT, padx=20)

        def log_out(self):
                self.master.destroy()

        # def return_back(self):
        #         self.master.destroy()
        #         win = Tk()
        #         std = Signin(win)
                



                




        


        def student(self):
                self.master.iconify()
                std = StudentWindow()

        def exam(self):
                self.master.iconify()
                exm = ExamWindow()

        def library(self):
                self.master.iconify()
                lib = LibraryWindow()

        def staff(self):
                self.master.iconify()
                stf = StaffWindow()
# window = Tk()
# std = Login(window)
# mainloop()







