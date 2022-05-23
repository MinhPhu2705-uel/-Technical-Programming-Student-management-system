from ast import Str
from datetime import date, datetime

from sqlite3 import Date
from time import strftime, strptime
from tkinter import ttk
from tkinter import*
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from numpy import datetime64, datetime_as_string
from pymongo import*
from tkcalendar import*
import re

mongo_client = MongoClient('mongodb+srv://Luppy_1005:anhyeuem123456@cuncon.cnyl1.mongodb.net/test')
db = mongo_client["University"]
cols = db["Exam"]

class ExamWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.iconbitmap('Img/iconn.ico')
        self.master.title('Exam Management System')
        self.master.geometry("1200x600+30+15")

        # self.window_width = 1200
        # self.window_height = 600
        # self.screen_width = window.winfo_screenwidth()
        # self.screen_height = window.winfo_screenheight()
        # # print("Width: ", screen_width, "Height: ", screen_height)
        # self.x = (self.screen_width / 2) - (self.window_width / 2)
        # self.y = (self.screen_height / 2) - (self.window_height / 2)
        # self.master.geometry(f"{self.window_width}x{self.window_height}+{int(self.x)}+{int(self.y)}")





        #########################################################
        self.frameleft = Frame(self.master, width=400,bg='#f4a460')
        self.frameleft.pack(side=LEFT, fill=BOTH)
        #########################################################
        self.nameLabel = Label(self.frameleft, text='Name of Group:', fg='black', font=('tahoma', 11, 'bold'),bg='#f4a460')
        self.nameLabel.place(x=15, y=20, width=120, height=40)
        self.phoneLabel = Label(self.frameleft, text='ClassRoom:', fg='black', font=('tahoma', 12, 'bold'),bg='#f4a460')
        self.phoneLabel.place(x=10, y=80, width=120, height=40)
        self.NameBookLabel = Label(self.frameleft, text='Professor:', fg='black', font=('tahoma', 12, 'bold'),bg='#f4a460')
        self.NameBookLabel.place(x=10, y=140, width=120, height=40)
        self.datedLabel = Label(self.frameleft, text='Date:', fg='black', font=('tahoma', 12, 'bold'),bg='#f4a460')
        self.datedLabel.place(x=15, y=200, width=120, height=40)
        self.daterLabel = Label(self.frameleft, text='Time:', fg='black', font=('tahoma', 12, 'bold'),bg='#f4a460')
        self.daterLabel.place(x=15, y=430, width=120, height=40)
        self.id = IntVar()
        self.group = StringVar()
        self.classes = StringVar()
        self.professor = StringVar()
        self.dexam = StringVar()
        self.timeExam=StringVar()

        self.GroupName = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.group)
        self.GroupName.place(x=170, y=20, width=200, height=40)
        self.classRoom = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.classes)
        self.classRoom.place(x=170, y=80, width=200, height=40)
        self.Professor = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.professor)
        self.Professor.place(x=170, y=140, width=200, height=40)
        self.DateExam = Calendar(self.frameleft, year=datetime.today().year)
        dexam = self.DateExam
        self.DateExam.place(x=170, y=200, width=200, height=200)
        self.TimeEntry = ttk.Combobox(self.frameleft, values=["", "8:00", "9:00", "10:00","11:00","12:00","14:00","15:00","16:00","17:00"],
                                     state='readonly', textvariable=self.timeExam)
        self.TimeEntry.place(x=170, y=440, width=200)

        self.buttonAdd = Button(self.frameleft, text="ADD", command=self.add, font=('tahoma', 10, 'bold'), bg = '#FF9933')
        self.buttonAdd.place(x=20, y=500, width=60, height=60)
        self.buttonUpdate = Button(self.frameleft, command=self.update, text="UPDATE", font=('tahoma', 10, 'bold'), bg = '#FF9933')
        self.buttonUpdate.place(x=100, y=500, width=60, height=60)
        self.buttonDelete = Button(self.frameleft, command=self.delete, text="DELETE", font=('tahoma', 10, 'bold'),bg = '#FF9933')
        self.buttonDelete.place(x=180, y=500, width=60, height=60)
        self.buttonRead = Button(self.frameleft, command=self.load_data, text="SHOW", font=('tahoma', 10, 'bold'), bg = '#FF9933')
        self.buttonRead.place(x=260, y=500, width=60, height=60)
        self.buttonReset = Button(self.frameleft, command=self.reset, text="RESET", font=('tahoma', 10, 'bold'), bg = '#FF9933')
        self.buttonReset.place(x=340, y=500, width=60, height=60)

        ############################# right frame start here ######################"""
        self.frameright = Frame(self.master, width=800,bg='#f4a460')
        self.frameright.pack(side=LEFT, fill=Y)
        ############################# right frame end here ######################"""

        self.framerighttop = Frame(self.frameright, height=50, pady=5, padx=5,bg='#f4a460')

        self.searchstudent = Entry(self.framerighttop, fg='#4F4F4F', font=('tahoma', 12, 'bold'), width=110)
        self.searchstudent.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        self.buttonsearch = Button(self.framerighttop, command=self.search, text='Search', fg='black',
                                   font=('tahoma', 12, 'bold'), width=50,bg = '#FF9933')
        self.buttonsearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        self.framerighttop.pack(fill=X)

        ################################# Frame Tree View ######################################"

        self.frameView = Frame(self.frameright, bg='red')
        self.frameView.pack()
        self.scrollbar = Scrollbar(self.frameView, orient=VERTICAL)
        self.table = ttk.Treeview(self.frameView,
                                  columns=("ID","GroupeName","ClassRoom","Professor","Date Exam","Time"),
                                  show='headings', yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill= Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID", text="ID")
        self.table.heading("GroupeName", text="Group Name")
        self.table.heading("ClassRoom", text="Class Room")
        self.table.heading("Professor", text="Professor")
        self.table.heading("Date Exam", text="Date Exam")
        self.table.heading("Time", text="Time")

        self.table.column("ID", anchor=W, width=15)
        self.table.column("GroupeName", anchor=W,width=150)
        self.table.column("ClassRoom", anchor=W,width=100)
        self.table.column("Professor", anchor=W,width=150)
        self.table.column("Date Exam", anchor=W,width=150)
        self.table.column("Time", anchor=W,width=100)
        self.load_data()
        self.table.bind("<ButtonRelease-1>", self.show)

    def clear_tree_view(self):
        for i in self.table.get_children():
            self.table.delete(i)

    def load_data(self):
        self.clear_tree_view()
        cur = cols.find({})
        for d in cur:
            p_id = (d['ID'])
            p_date_exam = (d['Date_Exam'])
            p_classroom = str(d['Classromm']).encode("UTF-8").decode("UTF-8")
            p_time = str(d['Time']).encode("UTF-8").decode("UTF-8")
            p_professor = str(d['Professor']).encode("UTF-8").decode("UTF-8")
            p_grname = str(d['Gr_name']).encode("UTF-8").decode("UTF-8")
            self.table.insert('', 'end', values=(p_id,p_grname, p_classroom, p_professor, p_date_exam,p_time))

################### Bottom Frame ####################################
    
        self.img_ex = Image.open('Image/exam_screen.png')
        self.img_ex.thumbnail((300,300))
        self.new_img_ex = ImageTk.PhotoImage(self.img_ex)


        self.frameBot=Frame(self.frameright,bg='blue',width=50,height=50)
        self.frameBot.pack(pady=10)

        self.std_label = Label(self.frameBot,image=self.new_img_ex,bg='#f4a460')
        self.std_label.pack()



    def load_data_name(self, ID):
        self.clear_tree_view()
        cur = cols.find({})
        for d in cur:
            p_date_exam = str(d['Date_Exam']).encode("UTF-8").decode("UTF-8")
            if(ID != p_date_exam): continue
            p_Id = int(d['ID'])
            p_classroom = str(d['Classromm']).encode("UTF-8").decode("UTF-8")
            p_time = str(d['Time']).encode("UTF-8").decode("UTF-8")
            p_professor = str(d['Professor']).encode("UTF-8").decode("UTF-8")
            p_grname = str(d['Gr_name']).encode("UTF-8").decode("UTF-8")
            self.table.insert('', 'end', values=(p_Id,p_grname, p_classroom, p_professor, p_date_exam,p_time))
        
         
        
    def add(self):
        max_id = 0
        cur = cols.find({})
        self.dexam = self.DateExam.get_date()

        intPattern = '[0-9_*]+'
        roomPattern = '\w+.\d+'

        if(re.findall(intPattern, self.group.get()) or re.findall(intPattern, self.professor.get())):
            messagebox.showwarning("Warning", "Invalid Name ! Should be a string !")
            return

        if(not(re.fullmatch(roomPattern, self.classRoom.get()))):
            messagebox.showwarning("Warning", "Invalid Room's Name !")
            return

        if(self.dexam == ""):
            messagebox.showwarning("Warning", "Date exam is empty !")
            return

        for d in cur:
            max_id = (d['ID'])
            d_classRoom = (d['Classromm'])
            d_dateExam = (d['Date_Exam'])
            d_date = (d['Time'])
            if(self.classRoom.get() == d_classRoom and d_dateExam == self.dexam  and self.timeExam.get() == d_date):
                messagebox.showwarning("Warning", "Used room !")
                return
        cur_id = max_id + 1
        data = {"ID": cur_id,"Classromm": self.classes.get(), "Date_Exam": self.dexam, "Gr_name": self.group.get(), "Professor": self.Professor.get(),
        "Time": self.timeExam.get()}
        doc = cols.insert_one(data)
        if doc.inserted_id:
            messagebox.showinfo("Insert", "Success !")
            self.load_data()

    def show(self, ev):
        self.iid=self.table.focus()
        alldata=self.table.item(self.iid)
        val=alldata['values']
        self.id.set(val[0])
        self.group.set(val[1])
        self.classes.set(val[2])
        self.professor.set(val[3])
        self.dexam.set(val[4])
        self.timeExam.set(val[5])
        

    def reset(self):
        self.load_data()
        self.group.set("")
        self.classes.set("")
        self.professor.set("")
        self.dexam.set("")
        self.timeExam.set("")

    def delete(self):
        if messagebox.askokcancel("Confirm", "Delete?"):
            cols.delete_one({"ID": self.id.get()})
            self.reset()

    def update(self):
        new_data = {"Professor": self.professor.get()}
        cols.update_one({"ID": self.id.get()}, {"$set":new_data})
        self.load_data()

    def search(self):
        search_name = self.searchstudent.get()
        self.load_data_name(search_name)


# std = ExamWindow()                    
# mainloop()                                                                                                                                                                                                                                                                                                                                                              