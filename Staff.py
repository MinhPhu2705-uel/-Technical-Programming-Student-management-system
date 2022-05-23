import email
from tkinter import ttk
from tkinter import*
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from pymongo import*
import re

  
mongo_client = MongoClient('localhost:27017')
db = mongo_client["University"]
cols = db["Staff"]

class StaffWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('Staff Management System')
        self.master.geometry("1200x600+0+0")
        #########################################################
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=BOTH)
        #########################################################
        self.firstName = Label(self.frameleft, text='Firstname:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.firstName.place(x=10, y=20, width=100, height=40)
        self.lastName = Label(self.frameleft, text='Lastname:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.lastName.place(x=10, y=70, width=100, height=40)
        self.Email = Label(self.frameleft, text='Email:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.Email.place(x=10, y=120, width=100, height=40)
        self.Phone = Label(self.frameleft, text='Phone:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.Phone.place(x=10, y=170, width=100, height=40)
        self.Job = Label(self.frameleft, text='Job:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.Job.place(x=10, y=220, width=100, height=40)
        self.id = IntVar()
        self.name = StringVar()
        self.last = StringVar()
        self.email = StringVar()
        self.phone = StringVar()
        self.job = StringVar()
        self.firstNameEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.name)
        self.firstNameEntry.place(x=120, y=20, width=200, height=40)
        self.lastNameEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.last)
        self.lastNameEntry.place(x=120, y=70, width=200, height=40)
        self.EmailEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.email)
        self.EmailEntry.place(x=120, y=120, width=200, height=40)
        self.PhoneEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.phone)
        self.PhoneEntry.place(x=120, y=170, width=200, height=40)
        self.job.set("--Select Job--")
        self.JobEntry = ttk.Combobox(self.frameleft, values=["Employee", "Professor", "Technician"],
                                     state='readonly', textvariable=self.job)
        self.JobEntry.place(x=120, y=220, width=200, height=40)

        self.buttonAdd = Button(self.frameleft, text="ADD", command=self.add, font=('tahoma', 10, 'bold'))
        self.buttonAdd.place(x=20, y=400, width=60, height=60)
        self.buttonUpdate = Button(self.frameleft, command=self.update, text="UPDATE", font=('tahoma', 10, 'bold'))
        self.buttonUpdate.place(x=100, y=400, width=60, height=60)
        self.buttonDelete = Button(self.frameleft, command=self.delete, text="DELETE", font=('tahoma', 10, 'bold'))
        self.buttonDelete.place(x=180, y=400, width=60, height=60)
        self.buttonRead = Button(self.frameleft, command=self.load_data, text="SHOW", font=('tahoma', 10, 'bold'))
        self.buttonRead.place(x=260, y=400, width=60, height=60)
        self.buttonReset = Button(self.frameleft, command=self.reset, text="RESET", font=('tahoma', 10, 'bold'))
        self.buttonReset.place(x=340, y=400, width=60, height=60)

        ############################# right frame start here ######################"""
        self.frameright = Frame(self.master, width=800)
        self.frameright.pack(side=LEFT, fill=Y)
        ############################# right frame end here ######################"""

        self.framerighttop = Frame(self.frameright, height=50, pady=5, padx=5)

        self.searchstudent = Entry(self.framerighttop, fg='#4F4F4F', font=('tahoma', 12, 'bold'), width=110)
        self.searchstudent.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        self.buttonsearch = Button(self.framerighttop, command=self.search, text='Search', fg='#4F4F4F',
                                   font=('tahoma', 12, 'bold'), width=50)
        self.buttonsearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        self.framerighttop.pack(fill=X)

        ################################# Frame Tree View ######################################"

        self.frameView = Frame(self.frameright, bg='blue')
        self.frameView.pack(fill=Y)
        self.scrollbar = Scrollbar(self.frameView, orient=VERTICAL)
        self.table = ttk.Treeview(self.frameView,
                                  columns=("ID", "Firstname", "Lastname", "Email", "Phone", "Job"),
                                  show='headings', yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID", text="ID")
        self.table.heading("Firstname", text="Firstname")
        self.table.heading("Lastname", text="Lastname")
        self.table.heading("Email", text="Email")
        self.table.heading("Phone", text="Phone")
        self.table.heading("Job", text="Job")

        self.table.column("ID", anchor=W, width=30)
        self.table.column("Firstname", anchor=W, width=100)
        self.table.column("Lastname", anchor=W, width=100)
        self.table.column("Email", anchor=W, width=150)
        self.table.column("Phone", anchor=W,width=150)
        self.table.column("Job", anchor=W,width=150)
        self.load_data()
        self.table.bind("<ButtonRelease>", self.show)

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
            p_phone = int(d['Phone'])
            p_email = str(d['Email']).encode("UTF-8").decode("UTF-8")
            p_job = str(d['Job']).encode("UTF-8").decode("UTF-8")
            self.table.insert('', 'end', values=(p_Id, p_Fname, p_Lname, p_email, p_phone,p_job))

    def load_data_name(self, name):
        self.clear_tree_view()
        cur = cols.find({})
        for d in cur:
            p_Fname = str(d['Firstname']).encode("UTF-8").decode("UTF-8")
            if(name != p_Fname): continue
            p_Id = int(d['ID'])
            p_Lname = str(d['Lastname']).encode("UTF-8").decode("UTF-8")
            p_phone = int(d['Phone'])
            p_email = str(d['Email']).encode("UTF-8").decode("UTF-8")
            p_job = str(d['Job']).encode("UTF-8").decode("UTF-8")
            self.table.insert('', 'end', values=(p_Id, p_Fname, p_Lname, p_email, p_phone,p_job))

        
    def add(self):
        cur = cols.find({})
        max_id = 1
        
        emailPattern = '\w+@gmail.com'
        phonePattern = '^[0-9]{10,12}'
        intPattern = '[0-9_*]+'
        jobPattern ='(Employee|Professor|Technician)'

        if(not(re.fullmatch(emailPattern, self.email.get()))):
            messagebox.showwarning("Warning", "Invalid Email ! Should be ____@gmail.com !")
            return

        if(not(re.fullmatch(phonePattern, self.phone.get()))):
            messagebox.showwarning("Warning", "Invalid Phone ! Should be phone number !")
            return

        if(re.findall(intPattern, self.name.get()) or re.findall(intPattern, self.last.get()) or self.name.get() == "" or self.last.get() == ""):
            messagebox.showwarning("Warning", "Invalid Name ! Should be a string !")
            return
        
        if(not(re.fullmatch(jobPattern, self.job.get()))):
            messagebox.showwarning("Warning", "Empty job !")
            return

        for d in cur:
            max_id = int(d['ID']) + 1
            p_email = (d['Email'])
            if(p_email == self.email.get()):
                messagebox.showwarning("Warning", "Available email !")
                return
                
        data = {"ID": max_id,"Firstname": self.name.get(), "Lastname": self.last.get(), "Phone": self.phone.get(), "Email": self.email.get(),"Job": self.job.get()}
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
        self.email.set(val[3])
        self.phone.set(val[4])
        self.job.set(val[5])
        

    def reset(self):
        self.load_data()
        self.name.set("")
        self.last.set("")
        self.email.set("")
        self.phone.set("")
        self.job.set("--Select Job--")

    def delete(self):
        if messagebox.askokcancel("Confirm", "Delete?"):
            cols.delete_one({"ID": self.id.get()})
            self.reset()

    def update(self):
        emailPattern = '\w+@gmail.com'
        phonePattern = '^[0-9]{10,12}'
        intPattern = '[0-9_*]+'

        if(not(re.fullmatch(emailPattern, self.email.get()))):
            messagebox.showwarning("Warning", "Invalid Email ! Should be ____@gmail.com !")
            return

        if(not(re.match(phonePattern, self.phone.get()))):
            messagebox.showwarning("Warning", "Invalid Phone ! Should be phone number !")
            return

        if(re.findall(intPattern, self.name.get()) or re.findall(intPattern, self.last.get()) or self.name.get() == "" or self.last.get() == ""):
            messagebox.showwarning("Warning", "Invalid Name ! Should be a string !")
            return
        new_data = {"Firstname": self.name.get(), "Lastname": self.last.get(), "Email": self.email.get(), "Phone": self.phone.get(), "Job": self.job.get()}
        cols.update_one({"ID": self.id.get()}, {"$set":new_data})
        self.load_data()

    def search(self):
        search_name = self.searchstudent.get()
        self.load_data_name(search_name)
# s = StaffWindow()
# mainloop()