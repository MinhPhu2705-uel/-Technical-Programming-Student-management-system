import re
from tkinter import ttk
from tkinter import*
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from pymongo import*
from tkcalendar import Calendar
from datetime import date, datetime
from pymongo import*

mongo_client = MongoClient('mongodb+srv://Luppy_1005:anhyeuem123456@cuncon.cnyl1.mongodb.net/test')
db = mongo_client["University"]
cols = db["Library"]

cols_student = db["Student"]

class LibraryWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.iconbitmap('Img/iconn.ico')
        self.master.title('Library Management System')
        self.master.geometry("1200x570+30+15")
        self.master.resizable(False,False)


        #########################################################
        self.frameleft = Frame(self.master, width=400,bg="#8fbc8f")
        self.frameleft.pack(side=LEFT, fill=BOTH)
        #########################################################
        self.nameLabel=Label(self.frameleft,text='Student Name:',fg='black',font=('tahoma',12,'bold'),bg="#8fbc8f")
        self.nameLabel.place(x=15,y=20,width=120,height=40)
        self.phoneLabel = Label(self.frameleft, text='Phone:', fg='black', font=('tahoma', 12, 'bold'),bg="#8fbc8f")
        self.phoneLabel.place(x=10, y=80, width=120, height=40)
        self.NameBookLabel = Label(self.frameleft, text='Book Name:', fg='black', font=('tahoma', 12, 'bold'),bg="#8fbc8f")
        self.NameBookLabel.place(x=10, y=140, width=120, height=40)
        self.datedLabel = Label(self.frameleft, text='Delivery Date:', fg='black', font=('tahoma', 12, 'bold'),bg="#8fbc8f")
        self.datedLabel.place(x=15, y=200, width=120, height=40)
        self.daterLabel = Label(self.frameleft, text='Return Date:', fg='black', font=('tahoma', 12, 'bold'),bg="#8fbc8f")
        self.daterLabel.place(x=15, y=260, width=120, height=40)
        self.id = IntVar()
        self.name=StringVar()
        self.phone = StringVar()
        self.book = StringVar()
        self.delivery=StringVar()
        self.returnn = StringVar()


        self.nameStudent = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.name)
        self.nameStudent.place(x=170,y=20,width=200,height=40)
        self.phoneStudent = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.phone)
        self.phoneStudent.place(x=170, y=80, width=200, height=40)
        self.bookname = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.book)
        self.bookname.place(x=170, y=140, width=200, height=40)
        self.deli = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.delivery)
        self.deli.place(x=170, y=200, width=200, height=40)
        # self.DeliveryDate=Calendar(self.frameleft, year=datetime.today().year)
        # self.DeliveryDate.place(x=170, y=200,width=200,height=200)
        self.ReturnDate = Calendar(self.frameleft, year=datetime.today().year)
        self.ReturnDate.place(x=170, y=260, width=200, height=200)


        
        # self.buttonAdd=Button(self.frameleft,text="ADD", command=self.add ,font=('tahoma',10,'bold'))
        # self.buttonAdd.place(x=20,y=700,width=60,height=60)
        # self.buttonUpdate = Button(self.frameleft,command=self.update, text="UPDATE",font=('tahoma',10,'bold'))
        # self.buttonUpdate.place(x=100, y=700,width=60,height=60)
        # self.buttonDelete = Button(self.frameleft,command=self.delete, text="DELETE",font=('tahoma',10,'bold'))
        # self.buttonDelete.place(x=180, y=700,width=60,height=60)
        # self.buttonRead = Button(self.frameleft, command=self.read, text="SHOW", font=('tahoma', 10, 'bold'))
        # self.buttonRead.place(x=260, y=700, width=60, height=60)
        # self.buttonReset = Button(self.frameleft,command=self.reset, text="RESET", font=('tahoma', 10, 'bold'))
        # self.buttonReset.place(x=340, y=700, width=60, height=60)









    ############################# right frame start here ######################"""
        self.frameright = Frame(self.master, width=800,bg="#8fbc8f")
        self.frameright.pack(side=LEFT, fill=Y)
    ############################# right frame end here ######################"""

        self.framerighttop=Frame(self.frameright,height=50,pady=5,padx=5,bg="#8fbc8f")


        self.searchstudent = Entry(self.framerighttop, fg='#4F4F4F', font=('tahoma', 12, 'bold'),width=110)
        self.searchstudent.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        self.buttonsearch = Button(self.framerighttop,command=self.search, text='Search', fg='black', font=('tahoma', 12, 'bold'),width=50, bg ='#669933')
        self.buttonsearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        self.framerighttop.pack(fill=X)




        
        self.buttonAdd=Button(self.frameleft,text="ADD", command=self.add ,font=('tahoma',10,'bold'), bg = '#669933')
        self.buttonAdd.place(x=60,y=500,width=60,height=60)

        # self.buttonUpdate = Button(self.frameleft,command=self.update, text="UPDATE",font=('tahoma',10,'bold'))
        # self.buttonUpdate.place(x=100, y=500,width=60,height=60)
        self.buttonDelete = Button(self.frameleft,command=self.delete, text="DELETE",font=('tahoma',10,'bold'), bg = '#669933')
        self.buttonDelete.place(x=140, y=500,width=60,height=60)
        self.buttonRead = Button(self.frameleft, command=self.load_data, text="SHOW", font=('tahoma', 10, 'bold'), bg = '#669933')
        self.buttonRead.place(x=220, y=500, width=60, height=60)
        self.buttonReset = Button(self.frameleft,command=self.reset, text="RESET", font=('tahoma', 10, 'bold'), bg = '#669933')
        self.buttonReset.place(x=300, y=500, width=60, height=60)



        ################################# Frame Tree View ######################################"

        self.frameView=Frame(self.frameright,bg='blue')
        self.frameView.pack()
        self.scrollbar=Scrollbar(self.frameView,orient=VERTICAL)
        self.table=ttk.Treeview(self.frameView,columns=("ID","Name","Phone","Book","Delivery Date","Return Date"),show='headings',yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID",text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("Phone", text="Phone")
        self.table.heading("Book", text="Book")
        self.table.heading("Delivery Date", text="Delivery Date")
        self.table.heading("Return Date", text="Return Date")

        self.table.column("ID", anchor=W,width=7)
        self.table.column("Name", anchor=W,width=150)
        self.table.column("Phone",anchor=W,width=150)
        self.table.column("Book", anchor=W,width=150)
        self.table.column("Delivery Date",anchor=W,width=100)
        self.table.column("Return Date",anchor=W,width=100)
        self.load_data()
        self.table.bind("<ButtonRelease>",self.show)
############# Right bottom frame ######################`
        
        self.img_lib = Image.open('Image/Lib_screen.png')
        self.img_lib.thumbnail((400,400))
        self.new_img_lib = ImageTk.PhotoImage(self.img_lib)

        self.frameBot=Frame(self.frameright,bg='blue',width=50,height=50)
        self.frameBot.pack(pady=10)

        self.Lib_label = Label(self.frameBot,image=self.new_img_lib,bg="#8fbc8f")
        self.Lib_label.pack()


       


    def clear_tree_view(self):
        for i in self.table.get_children():
            self.table.delete(i)

    def load_data(self):
        check = 0
        self.clear_tree_view()
        cur = cols.find({})
        cur_stu = cols_student.find({})

        for d in cur:
            p_Id = str(d['ID'])
            p_name = str(d['Name']).encode("UTF-8").decode("UTF-8")

            for k in cur_stu:
                stu_name = (k['Lastname']) + " " + (k['Firstname'])
                if(p_name == stu_name): 
                    check = 1
                    break

            if(not(check)): 
                cols.delete_one({"Name": p_name})
                self.reset()
                break

            p_book = str(d['Book']).encode("UTF-8").decode("UTF-8")
            p_del = str(d['Delivery']).encode("UTF-8").decode("UTF-8")
            p_phone = str(d['Phone'])
            p_return = str(d['Return']).encode("UTF-8").decode("UTF-8")
            self.table.insert('', 'end', values=(p_Id,p_name, p_phone, p_book, p_del, p_return))

    def load_data_name(self, name):
        self.clear_tree_view()
        cur = cols.find({})
        for d in cur:
            p_name = str(d['Name']).encode("UTF-8").decode("UTF-8")
            if(name == p_name): 
                p_Id = str(d['ID'])
                p_book = str(d['Book']).encode("UTF-8").decode("UTF-8")
                p_del = str(d['Delivery']).encode("UTF-8").decode("UTF-8")
                p_phone = 'hello' + str(d['Phone'])
                p_return = str(d['Return']).encode("UTF-8").decode("UTF-8")
                self.table.insert('', 'end', values=(p_Id,p_name, p_phone, p_book, p_del, p_return))

        
    def add(self):
        check = 0
        max_id = 0
        cur = cols.find({})
        cur_stu = cols_student.find({})
        returnn_date = self.ReturnDate.get_date()
        intPattern = '[0-9_*]+'
        phonePattern = '^[0-9]{10,12}'
        self.deli = datetime.now().strftime('%m/%d/%y')
        for d in cur_stu:
            stu_name = (d['Lastname']) + " " + (d['Firstname'])
            if(self.name.get() == stu_name): 
                check = 1
                break

        date1 = datetime.strptime(returnn_date, '%m/%d/%y')
        date2 = datetime.strptime(self.deli, '%m/%d/%y')

        if(date1 < date2):
            messagebox.showwarning("Warning", "Invalid return date")
            return 

        if(not(check)):
            messagebox.showwarning("Warning", "Invalid student")
            return

        if(re.findall(intPattern, self.name.get()) or re.findall(intPattern, self.book.get()) or self.name.get() == "" or self.book.get() == ""):
            messagebox.showwarning("Warning", "Invalid Name ! Should be a string !")
            return
        
        if(not(re.fullmatch(phonePattern, self.phone.get()))):
            messagebox.showwarning("Warning", "Invalid Phone ! Should be phone number !")
            return
        

        for d in cur:
            max_id = int(d['ID']) + 1

        data = {"ID": max_id,"Name": self.name.get(), "Phone": self.phone.get(), "Return": returnn_date, "Delivery": self.deli, "Book": self.book.get()}
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
        self.phone.set(val[2])
        self.book.set(val[3])
        self.delivery.set(val[4])
        self.returnn.set(val[5])
        

    def reset(self):
        self.load_data()
        self.name.set("")
        self.phone.set("")
        self.book.set("")
        self.delivery.set("")
        self.returnn.set("")

    def delete(self):
        if messagebox.askokcancel("Confirm", "Delete?"):
            cols.delete_one({"ID": self.id.get()})
            self.reset()

    def search(self):
        search_name = self.searchstudent.get()
        self.load_data_name(search_name)


# std = LibraryWindow()
# mainloop()