from tkinter import ttk
import random
from numpy import datetime64, datetime_data
from pymongo import*
from tkinter import messagebox
from tkinter import *
from PIL import Image
from PIL import ImageTk
import re


mongo_client = MongoClient('mongodb+srv://Luppy_1005:anhyeuem123456@cuncon.cnyl1.mongodb.net/test')
db = mongo_client["University"]
cols = db["Student"]



class StudentWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('Student Management System')
        self.master.iconbitmap('Img/iconn.ico')
        self.master.geometry("1200x550+30+15")
        self.master.resizable(False,False)
        #########################################################
        self.frameleft = Frame(self.master, width=400,bg='#305065')
        self.frameleft.pack(side=LEFT, fill=BOTH)
        #########################################################
        self.firstName=Label(self.frameleft,text='First name:',fg='black',font=('tahoma',12,'bold'),bg='#305065')
        self.firstName.place(x=10,y=50,width=100,height=40)
        self.lastName = Label(self.frameleft, text='Last name:',fg='black',font=('tahoma',12,'bold'),bg='#305065')
        self.lastName.place(x=10,y=120,width=100,height=40)
        self.DOB = Label(self.frameleft, text='Date of Birth:',fg='black',font=('tahoma',11,'bold'),bg='#305065')
        self.DOB.place(x=10,y=190,width=100,height=40)
        self.Email = Label(self.frameleft, text='Email:',fg='black',font=('tahoma',12,'bold'),bg='#305065')
        self.Email.place(x=10,y=260,width=100,height=40)
        self.id = IntVar()
        self.name=StringVar()
        self.last = StringVar()
        self.email = StringVar()
        self.dob = StringVar()

        self.firstNameEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.name)
        self.firstNameEntry.place(x=120,y=50,width=200,height=40)
        self.lastNameEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.last)
        self.lastNameEntry.place(x=120,y=120,width=200,height=40)
        self.DOBentry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.dob)
        self.DOBentry.place(x=120,y=190,width=200,height=40)
        self.EmailEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.email)
        self.EmailEntry.place(x=120,y=260,width=200,height=40)



        self.buttonAdd=Button(self.frameleft,text="ADD", command=self.add ,font=('tahoma',10,'bold'), bg='#006699')
        self.buttonAdd.place(x=20,y=400,width=60,height=50)
        self.buttonUpdate = Button(self.frameleft,command=self.update, text="UPDATE",font=('tahoma',10,'bold'), bg='#006699')
        self.buttonUpdate.place(x=100, y=400,width=60,height=50)
        self.buttonDelete = Button(self.frameleft,command=self.delete, text="DELETE",font=('tahoma',10,'bold'), bg='#006699')
        self.buttonDelete.place(x=180, y=400,width=60,height=50)
        self.buttonRead = Button(self.frameleft, command=self.load_data, text="SHOW", font=('tahoma', 10, 'bold'), bg='#006699')
        self.buttonRead.place(x=260, y=400, width=60, height=50)
        self.buttonReset = Button(self.frameleft,command=self.reset, text="RESET", font=('tahoma', 10, 'bold'), bg='#006699')
        self.buttonReset.place(x=340, y=400, width=60, height=50)






    ############################# right frame start here ######################"""
        self.frameright = Frame(self.master, width=800,bg='#305065')
        self.frameright.pack(side=LEFT, fill=Y)
    ############################# right frame end here ######################"""

        self.framerighttop=Frame(self.frameright,height=50,pady=5,padx=5,bg='#305065')


        self.searchstudent = Entry(self.framerighttop, fg='#4F4F4F', font=('tahoma', 12, 'bold'),width=110)
        self.searchstudent.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        self.buttonsearch = Button(self.framerighttop,command=self.search, text='Search', fg='black', font=('tahoma', 12, 'bold'),width=50, bg='#006699')
        self.buttonsearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        self.framerighttop.pack(fill=X)

        ################################# Frame Tree View ######################################"

        self.frameView=Frame(self.frameright,bg='blue')
        self.frameView.pack(fill=X, padx = 70)
        self.scrollbar=Scrollbar(self.frameView,orient=VERTICAL)
        self.table=ttk.Treeview(self.frameView,columns=("ID","Firstname","Lastname","DOB","Email"),show='headings',yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID",text="ID")
        self.table.heading("Firstname", text="Firstname")
        self.table.heading("Lastname", text="Lastname")
        self.table.heading("DOB", text="Date of birth")
        self.table.heading("Email", text="Email")

        self.table.column("ID", anchor=W,width=30)
        self.table.column("Firstname", anchor=W,width=100)
        self.table.column("Lastname",anchor=W,width=150)
        self.table.column("DOB",anchor=W,width=170)
        self.table.column("Email",anchor=W,width=170)
        self.load_data()
        self.table.bind("<ButtonRelease>",self.show)
############ Bottom Frame######################################

        self.img_std = Image.open('Image/student_screen.png')
        self.img_std.thumbnail((350,350))
        self.new_img_std = ImageTk.PhotoImage(self.img_std)


        self.frameBot=Frame(self.frameright,bg='blue',width=50,height=50)
        self.frameBot.pack(pady=10)

        self.std_label = Label(self.frameBot,image=self.new_img_std,bg='#305065')
        self.std_label.pack()



########### Tạo hàm ##########################################################


    def clear_tree_view(self):
        for i in self.table.get_children():
            self.table.delete(i)

    def load_data(self):
        self.clear_tree_view()
        cur = cols.find({})
        for d in cur:
            p_Id = int(d['ID'])
            p_Fname = str(d['Firstname']).encode("UTF-8").decode("UTF-8")
            p_Lname = str(d['Lastname']).encode("UTF-8").decode("UTF-8")
            p_dob = str(d['DOB'])
            p_email = str(d['Email']).encode("UTF-8").decode("UTF-8")
            self.table.insert('', 'end', values=(p_Id,p_Fname, p_Lname, p_dob, p_email))

    def load_data_name(self, name):
        self.clear_tree_view()
        cur = cols.find({})
        for d in cur:
            p_Id = int(d['ID'])
            p_Fname = str(d['Firstname']).encode("UTF-8").decode("UTF-8")
            if(name != p_Fname): continue
            p_Lprice = str(d['Lastname']).encode("UTF-8").decode("UTF-8")
            p_dob = str(d['DOB'])
            p_email = str(d['Email']).encode("UTF-8").decode("UTF-8")
            self.table.insert('', 'end', values=(p_Id,p_Fname, p_Lprice, p_dob, p_email))

        
    def add(self):
        max_id = 1
        cur = cols.find({})

        emailPattern = '\w+@gmail.com'

        intPattern = '[0-9_*]+'

        birthdayPattern = '(?:0[1-9]|[12][0-9]|3[01])[-/.](?:0[1-9]|1[012])[-/.](?:19\d{2,}|20[01][0-9]|2022)'

        if(not(re.fullmatch(emailPattern, self.email.get()))):
            messagebox.showwarning("Warning", "Invalid Email ! Should be ____@gmail.com !")
            return

        if(not(re.fullmatch(birthdayPattern, self.dob.get()))):
            messagebox.showwarning("Warning", "Invalid Birthday !")
            return

        if(re.findall(intPattern, self.name.get()) or re.findall(intPattern, self.last.get()) or self.name.get() == "" or  self.last.get() == ""):
            messagebox.showwarning("Warning", "Invalid Name ! Should be a string !")
            return


        for d in cur:
            max_id = int(d['ID']) + 1
            p_email = (d['Email'])
            if(p_email == self.email.get()):
                messagebox.showwarning("Warning", "Available email !")
                return
        data = {"ID": max_id,"Firstname": self.name.get(), "Lastname": self.last.get(), "DOB": self.dob.get(), "Email": self.email.get()}
        doc = cols.insert_one(data)
        if doc.inserted_id:
            messagebox.showinfo("Insert", "Success!")
            self.load_data()

    def show(self, ev):
        self.iid=self.table.focus()
        alldata=self.table.item(self.iid)
        val=alldata['values']
        self.id.set(val[0])
        self.name.set(val[1])
        self.last.set(val[2])
        self.dob.set(val[3])
        self.email.set(val[4])
        

    def reset(self):
        self.load_data()
        self.name.set("")
        self.last.set("")
        self.dob.set("")
        self.email.set("")

    def delete(self):
        if messagebox.askokcancel("Confirm", "Delete?"):
            cols.delete_one({"ID": self.id.get()})
            self.reset()

    def update(self):
        new_data = {"Firstname": self.name.get(),"Lastname": self.last.get(),"DOB": self.dob.get(), "Email": self.email.get()}
        cols.update_one({"ID": self.id.get()}, {"$set":new_data})
        self.load_data()

    def search(self):
        search_name = self.searchstudent.get()
        self.load_data_name(search_name)

# std = StudentWindow()
# mainloop()


