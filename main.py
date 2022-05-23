
import re
from tkinter import*
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from ast import*
from pymongo import*
from Menu import Menu_Window


mongo_client = MongoClient("mongodb+srv://Luppy_1005:anhyeuem123456@cuncon.cnyl1.mongodb.net/test")
db = mongo_client["University"]
cols = db["Login Accounts"]


class Signup:
        def __init__(self,window):
                self.master = window
                self.master.title("SignUp")
                # self.master.geometry('925x500+300+200')


################ Căn giữa màn hình #########################################
                self.window_width = 925
                self.window_height = 500
                self.screen_width = window.winfo_screenwidth()
                self.screen_height = window.winfo_screenheight()

                # print(self.screen_height, self.screen_height)
                # print("Width: ", screen_width, "Height: ", screen_height)
                self.x = ( self.screen_width / 2) - ( self.window_width / 2)
                self.y = ( self.screen_height / 2) - ( self.window_height / 2)
                self.master.geometry(f"{ self.window_width}x{ self.window_height}+{int( self.x)}+{int( self.y)}")


                self.master.configure(bg='#fff')
                self.master.resizable(False, False)
                self.img_signup = Image.open('Img/login2.png')
                self.img_signup.thumbnail((350,350))
                self.new_img_signup = ImageTk.PhotoImage(self.img_signup)
                self.Img_Label= Label(window, image=self.new_img_signup,border=0, bg= 'white').place(x=90,y=110)
                self.main_frame=Frame(window, width=350, height=390, bg='#fff')

                self.main_frame.place(x=480, y=50)

                self.heading=Label(self.main_frame, text='Sign up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
                self.heading.place(x=130, y=5)
        ###############################          Username      #########################################
                self.username = StringVar()
                self.code = StringVar()
                self.Cf_pass = StringVar()
        
                self.Label_user=Label(self.main_frame, text='Username', fg='black',bg='white', font =('Microsoft YaHei UI Light',11))
                self.Label_user.place(x=1, y=80)
                self.user=Entry(self.main_frame,width=25,fg='black', border=0, bg='white',font=('Microsoft Yahei UI Light',11),textvariable=self.username)
                self.user.place(x=80, y=80)
                self.Frame1=Frame(self.main_frame,width=295, height=2,bg='black').place(x=75,y=107)
                ##################################        PASSWORD     ###################################
        
                
                self.Label_pass=Label(self.main_frame, text='Password', fg='black',bg='white', font =('Microsoft YaHei UI Light',11))
                self.Label_pass.place(x=1, y=150)
                self.Pass_Entry=Entry(self.main_frame,width=25,fg='black', border=0, bg='white',font=('Microsoft Yahei UI Light',11),show="*",textvariable=self.code)
                self.Pass_Entry.place(x=80, y=150)
                self.Frame2=Frame(self.main_frame,width=295, height=2,bg='black').place(x=75,y=177)
                ######################### CONFIRM PASSWORD##########################

                self.Label_confirm=Label(self.main_frame, text='Confirm', fg='black',bg='white', font =('Microsoft YaHei UI Light',11))
                self.Label_confirm.place(x=1, y=220)

                self.Confirm_pass=Entry(self.main_frame,width=25,fg='black', border=0, bg='white',font=('Microsoft Yahei UI Light',11),show="*",textvariable=self.Cf_pass)
                self.Confirm_pass.place(x=80, y=220)

        
        
                self.Frame3= Frame(self.main_frame,width=295, height=2,bg='black').place(x=75,y=247)


                self.Signup_button= Button(self.main_frame, width=39,pady=7,text='Sign up', bg='#57a1f8',fg='white', border=0, command=self.sign_up).place(x=75, y=280)

                self.checkacc_label=Label(self.main_frame, text='I have an account', fg='black',bg='white', font =('Microsoft YaHei UI Light',9))
                self.checkacc_label.place(x=120,y=340)
                self.signin= Button(self.main_frame,width=6,text='Sign in',border=0, bg='white', cursor='hand2',fg='#57a1f8',command=self.sign_in_button)
                self.signin.place(x=250,y=340)

        def sign_up(self):
                cur = cols.find({})

                for d in cur:
                        d_username = str(d['username'])
                        if(d_username == self.username.get()): 
                                messagebox.showwarning("Warning", "Tên đăng nhập đã tồn tại")
                                return

                passwordPattern =  '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'

                if(not(re.fullmatch(passwordPattern, self.code.get()))):
                    messagebox.showerror("Error", "Mật khẩu không hợp lệ")
                    return

                if(self.Cf_pass.get() != self.code.get()): 
                        messagebox.showerror("Error", "Mật khẩu không trùng khớp")
                        return
                
                if(self.username.get() == "" or self.code.get() == ""): 
                        messagebox.showwarning("Warning", "Nhập tên đăng nhập hoặc mật khẩu")
                        return

                data = {"username": self.username.get(), "password": self.code.get()}
                doc = cols.insert_one(data)
                if doc.inserted_id:
                        messagebox.showinfo("Sign up", "Success !")

        def sign_in_button(self):
                self.master.destroy()
                window = Tk()
                std = Signin(window)

class Signin:
        def __init__(self,window):
                self.master = window
                self.master.title("Signin")
                # self.master.geometry('925x500+300+200')

                self.window_width = 925
                self.window_height = 500
                self.screen_width = window.winfo_screenwidth()
                self.screen_height = window.winfo_screenheight()
                # print("Width: ", screen_width, "Height: ", screen_height)
                self.x = ( self.screen_width / 2) - ( self.window_width / 2)
                self.y = ( self.screen_height / 2) - ( self.window_height / 2)
                self.master.geometry(f"{ self.window_width}x{ self.window_height}+{int( self.x)}+{int( self.y)}")


                self.master.configure(bg='#fff')
                self.master.resizable(False, False)
                self.img_signin = Image.open('Img/login 1.png')
                self.img_signin.thumbnail((350,350))
                self.new_img_signin = ImageTk.PhotoImage(self.img_signin)
                self.Img_Label= Label(window, image=self.new_img_signin,border=0, bg= 'white').place(x=90,y=150)
                self.main_frame=Frame(window, width=350, height=390, bg='#fff')
                self.main_frame.place(x=480, y=50)

                self.heading=Label(self.main_frame, text='Sign in', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
                self.heading.place(x=130, y=5)

                self.username = StringVar()
                self.password = StringVar()
        
                self.Label_user=Label(self.main_frame, text='Username', fg='black',bg='white', font =('Microsoft YaHei UI Light',11))
                self.Label_user.place(x=1, y=120)
                self.user=Entry(self.main_frame,width=25,fg='black', border=0, bg='white',font=('Microsoft Yahei UI Light',11), textvariable= self.username)
                self.user.place(x=80, y=120)
                self.Frame1=Frame(self.main_frame,width=295, height=2,bg='black').place(x=75,y=147)
                ##################################        PASSWORD     ###################################
        

                self.Label_pass=Label(self.main_frame, text='Password', fg='black',bg='white', font =('Microsoft YaHei UI Light',11))
                self.Label_pass.place(x=1, y=190)
                self.Pass_Entry=Entry(self.main_frame,width=25,fg='black', border=0, bg='white',font=('Microsoft Yahei UI Light',11),show="*", textvariable= self.password)
                self.Pass_Entry.place(x=80, y=190)
                self.Frame2=Frame(self.main_frame,width=295, height=2,bg='black').place(x=75,y=217)



                self.Signin_button= Button(self.main_frame, width=39,pady=7,text='Sign in', bg='#57a1f8',fg='white', border=0, command=self.Login).place(x=75, y=280)

                self.checkacc_label=Label(self.main_frame, text='I don\'t have an account ?', fg='black',bg='white', font =('Microsoft YaHei UI Light',9))
                self.checkacc_label.place(x=110,y=340)
                self.signin= Button(self.main_frame,width=6,text='Sign up',border=0, bg='white', cursor='hand2',fg='#57a1f8',command=self.sign_up_button)
                self.signin.place(x=260,y=340)

        def Login(self):
                check_login = False
                cur = cols.find({})
                for d in cur:
                        d_username = str(d['username'])
                        d_password = str(d['password'])
                        if(self.username.get() == d_username and self.password.get() == d_password):
                                check_login = TRUE
                                break
                if(check_login):
                    self.master.destroy()
                    window = Tk()
                    std = Menu_Window(window)     
                else: messagebox.showerror("Error", "Sai tên tài khoản hoặc mật khẩu")

        def sign_up_button(self):
                self.master.destroy()
                window = Tk()
                std = Signup(window)


window = Tk()
std = Signin(window) 
mainloop()
