from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from PIL import ImageTk
from pymongo import *
import datetime
from tkinter import ttk
import mysql.connector as mc
import tkinter.messagebox as mb
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkcalendar import Calendar
# DB Connection
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["example"]
col = db["products"]


class Infouni:
    def __init__(self, cf):
        self.universityInfo = Frame(cf, pady=10, padx=10)
        self.universityInfo.grid(row=0, column=0, sticky='senw')
        self.img = Image.open('Image/university.png')
        self.img.thumbnail((200, 200))
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imgUniversity = Label(self.universityInfo, image=self.new_img, padx=10, pady=10)
        self.imgUniversity.pack()
        self.buttonUniversity = Button(self.universityInfo, command=self.openinfowindow, font=('tahoma', 10, 'bold'),
                                       text='About University', bg='#1b9ea4', fg='white', padx=10, pady=10)
        self.buttonUniversity.pack()

    def openinfowindow(self):
        pass
        # info = InfoWindow()


class Staff:
    def __init__(self, cf):
        self.staffFrame = Frame(cf, pady=10, padx=10)
        self.staffFrame.grid(row=0, column=2, sticky='senw')
        self.img3 = Image.open('Image/staff.png')
        self.img3.thumbnail((200, 200))
        self.new_img3 = ImageTk.PhotoImage(self.img3)
        self.imgStaff = Label(self.staffFrame, image=self.new_img3, padx=10, pady=10)
        self.imgStaff.pack()
        self.buttonStaff = Button(self.staffFrame, command=self.openstaffwindow, font=('tahoma', 10, 'bold'),
                                  text='Staff Management', bg='#1b9ea4', fg='white', padx=10, pady=10)
        self.buttonStaff.pack()

    def openstaffwindow(self):
        pass
        # stdw = StaffWindow()

class Student:
    def __init__(self,cf):
        self.studentFrame = Frame(cf, pady=10, padx=10)
        self.studentFrame.grid(row=0, column=1, sticky='senw')
        self.img2 = Image.open('Image/studenticon.png')
        self.img2.thumbnail((200, 200))
        self.new_img2 = ImageTk.PhotoImage(self.img2)
        self.imgStudent = Label(self.studentFrame, image=self.new_img2, padx=10, pady=10)
        self.imgStudent.pack()
        self.buttonStudent = Button(self.studentFrame, command=self.openstudentwindow, font=('tahoma', 10, 'bold'),text='Student Management', bg='#1b9ea4', fg='white', padx=10, pady=10)
        self.buttonStudent.pack()


    def openstudentwindow(self):
        pass
       # stdw=StudentWindow()


class Library:
    def __init__(self,bf):
        self.libraryFrame = Frame(bf, pady=10, padx=50)
        self.libraryFrame.grid(row=1, column=0, sticky='senw')
        self.img4 = Image.open('Image/open-book.png')
        self.img4.thumbnail((200, 200))
        self.new_img4 = ImageTk.PhotoImage(self.img4)
        self.imgLibrary = Label(self.libraryFrame, image=self.new_img4, padx=10, pady=10)
        self.imgLibrary.pack()

        self.buttonLibrary = Button(self.libraryFrame, command=self.openlibrarywindow, font=('tahoma', 10, 'bold'),
                                    text='Library Management', bg='#1b9ea4', fg='white', padx=10, pady=10)
        self.buttonLibrary.pack()
    def openlibrarywindow(self):
        pass
        # lib = LibraryWindow()

# class Exam:
#     def __init__(self,bf):
#         self.examFrame = Frame(bf, pady=10, padx=50)
#         self.examFrame.grid(row=1, column=1, sticky='senw')
#         self.img5 = Image.open('Image/exam.png')
#         self.img5.thumbnail((200, 200))
#         self.new_img5 = ImageTk.PhotoImage(self.img5)
#         self.imgExam = Label(self.examFrame, image=self.new_img5, padx=10, pady=10)
#         self.imgExam.pack()
#         self.buttonExam = Button(self.examFrame, command=self.openExamWindow, font=('tahoma', 10, 'bold'),
#                                  text='Exam Management', bg='#1b9ea4', fg='white', padx=10, pady=10)
#         self.buttonExam.pack()
#
#     def openExamWindow(self):
#         pass
#         # lib = ExamWindow()

class University:
    def __init__(self, window):
        self.master = window
        self.master.title("University Management System")
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width, h=self.height))
        self.master.state('zoomed')
        ################# Frame Top Start Here ########################
        self.frametop = Frame(self.master, bg='#1b9ea4', height=150)
        self.frametop.pack(fill=X)
        self.sms = Label(self.frametop, text='University Management System', bg='#1b9ea4', fg='white',
                         font=('tahoma', 50), pady=50)
        self.sms.pack()
        self.buttonLogout = Button(self.frametop, text='logout', command=self.logout)
        self.buttonLogout.pack()
        ################# Frame Top End Here ##########################

        ################# Frame Center Start Here ########################

        self.centerFrame = Frame(self.master)
        self.centerFrame.pack(fill=X)
        ######Frame University info #####
        inf = Infouni(self.centerFrame)
        ##### Frame Student Frame ####
        std = Student(self.centerFrame)
        #####Frame Staff info ######
        stf = Staff(self.centerFrame)

        ################# Frame Center End Here ########################

        ################# Bottom Frame Start Here ########################
        self.bottomFrame = Frame(self.master, height=200)
        self.bottomFrame.pack(fill=X)
        ####### Library Frame ######
        lib = Library(self.bottomFrame)
        ######### Exam Frame ########
        # exa = Exam(self.bottomFrame)
        ################# Bottom Frame End Here ########################
        self.centerFrame.grid_columnconfigure(0, weight=1)
        self.centerFrame.grid_columnconfigure(1, weight=1)
        self.centerFrame.grid_columnconfigure(2, weight=1)

        self.bottomFrame.grid_columnconfigure(0, weight=1)
        self.bottomFrame.grid_columnconfigure(1, weight=1)

    def logout(self):
        self.master.destroy()

if (__name__ == '__main__'):
    window = Tk()
    window.iconbitmap('swim_ring_icon_183313.ico')
    std = University(window)
    mainloop()