from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Central Library")
root.configure(bg="grey")
root.geometry("1440x1440")
Label(root, text="WELCOME TO THE CENTRAL LIBRARY",font=("Times New Roman", 16," bold"),bg="light blue",relief=SUNKEN,anchor=CENTER,borderwidth=3).pack(side=TOP,anchor=CENTER)
bookslist = {"Think and grow rich":3,
"Attitude is everything":2,
"The power of subconcious mind":1,
"Rich Dad Poor Dad":4,
"Quantitative Aptitude":2,
"Wings of Fire":1}
signed_user = ""
with open("C:\\Users\\sai krishna\\Desktop\\programs\\python programs\\library_project\\userlist.txt","r") as userfile:
    userlist = userfile.readlines()
    userlogin_list=[]
    for each in userlist:
        userdata = []
        for data in each.strip("\n").split(" "):
            if data != "":
                userdata.append(data)
        userlogin_list.append(userdata)


mybooks=[]
def display_books():
    global mybooks
    for each in bookslist.keys():
        if bookslist[each]!=0:
            mybooks.append(each)
    booksvar = Variable(value=mybooks)
    mybookslist.config(listvariable=booksvar)
booksvar = Variable(value =mybooks)

image_frame = Frame(root,bg="grey")
image_frame.pack(side=TOP)
img = PhotoImage(file="C:\\Users\\sai krishna\\Desktop\\programs\\python programs\\library_project\\R.png")
img_label = Label(image_frame,image=img,width=2050,height=300)
img_label.pack(side=TOP, fill=BOTH)

second_frame=Frame(root,bg="light green")
second_frame.pack(side=TOP,fill=X)

first_frame = Frame(root,bg="light blue")
first_frame.pack(side=TOP)

display_button=Button(first_frame,text="Available books are ",font=("Times New Roman", 12," bold"),width=20,anchor=CENTER,relief=SUNKEN,borderwidth=3,command=display_books,state=DISABLED)
display_button.pack(side=LEFT,fill=Y)

mybookslist = Listbox(first_frame,listvariable=booksvar,font=("Times New Roman", 14," bold"),width= 100,height=5)
mybookslist.pack(side=LEFT,fill=X)

def borrow_books():
    bookname = Entry_book.get()
    if bookname in bookslist.keys():
        result = messagebox.askquestion(title="Confirmation",message="Do you agree for penalty if you won't return by 15 days ")
        if result == "yes":
            bookslist[bookname]-=1
            if bookslist[bookname]== 0:
                bookslist.pop(bookname)
            statement_label.configure(text=f"Book issued to {signed_user} successfully")
            # empty = []
            # booksvar = Variable(value=empty)
            # mybookslist.configure(listvariable=booksvar)
    else:
        statement_label.configure(text="Book is not available at this time")
        
def return_books():
    bookname = Entry_book.get()
    if bookname in bookslist.keys():
        bookslist[bookname]+=1
    else:
        bookslist[bookname]=1
    statement_label.configure(text="Book is returned successfully")
def donate_books():
    bookname = Entry_book.get()
    if bookname in bookslist.keys():
        bookslist[bookname]+=1
    else:
        bookslist[bookname]=1
    statement_label.configure(text="Thankyou for Donating "+signed_user)
def sign_in():
    signin_window = Toplevel(root)
    signin_window.geometry("360x360")
    e1var = StringVar()
    e2var = StringVar()
    namelabel = Label(signin_window,text="mail",bg="grey",width=20,relief=SUNKEN,borderwidth=3)
    passwordlabel= Label(signin_window,text="password",bg="grey",width=20,relief=SUNKEN,borderwidth=3)
    e1 = Entry(signin_window,textvariable=e1var,bg="light green",width=30)
    e2 = Entry(signin_window,textvariable=e2var,bg="light green",width=30)
    submitlabel = Label(signin_window,text="",font=("Times New Roman", 12," bold"),fg="red")
    def submit():
        count = 0
        for each in userlogin_list:
            count+=1
            if e1.get()== each[1] and e2.get() == each[3]:
                display_button.configure(state=ACTIVE)
                borrow_button.configure(state=ACTIVE)
                return_button.configure(state=ACTIVE)
                donate_button.configure(state=ACTIVE)
                Entry_book.configure(state=NORMAL)
                submitlabel.configure(text="logged in successfully")
                global signed_user
                signed_user=e1.get()
                break
            if count == len(userlogin_list):
                submitlabel.configure(text="No records found")
    namelabel.grid(row=0,column=0)
    passwordlabel.grid(row=1,column=0)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    Button(signin_window,text="SUBMIT",bg="light blue",font=("Times New Roman", 12," bold"),command=submit).grid(row=2,column=1)
    Button(signin_window,text="CLOSE",bg="light blue",font=("Times New Roman", 12," bold"),command=signin_window.destroy).grid(row=3,column=1)
    submitlabel.grid(row=4)

def sign_up():
    signup_Window = Toplevel(root)
    signup_Window.title("Sign up")
    signup_Window.geometry("360x360")
    l = Label(signup_Window,text="name",bg="grey",width=20,relief=SUNKEN,borderwidth=3)
    l2 = Label(signup_Window,text="mail",bg="grey",width=20,relief=SUNKEN,borderwidth=3)
    l3 = Label(signup_Window,text="mobile",bg="grey",width=20,relief=SUNKEN,borderwidth=3)
    l4 = Label(signup_Window,text="password",bg="grey",width=20,relief=SUNKEN,borderwidth=3)
    l5 = Label(signup_Window,text="cofirm-pword",bg="grey",width=20,relief=SUNKEN,borderwidth=3)
    l.grid(row=0,column=0)
    l2.grid(row=1,column=0)
    l3.grid(row=2,column=0)
    l4.grid(row=3,column=0)
    l5.grid(row=4,column=0)
    e1var = StringVar()
    e2var = StringVar()
    e3var = StringVar()
    e4var = StringVar()
    e5var = StringVar()
    e1 = Entry(signup_Window,textvariable=e1var,bg="light green",width=30)
    e2 = Entry(signup_Window,textvariable=e2var,bg="light green",width=30)
    e3 = Entry(signup_Window,textvariable=e3var,bg="light green",width=30)
    e4 = Entry(signup_Window,textvariable=e4var,bg="light green",width=30)
    e5 = Entry(signup_Window,textvariable=e5var,bg="light green",width=30)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    e3.grid(row=2,column=1)
    e4.grid(row=3,column=1)
    e5.grid(row=4,column=1)
    submitlabel = Label(signup_Window,text="",font=("Times New Roman", 12," bold"),fg="red")
    def submit():
        datalist = []
        flag = True
        for each in userlogin_list:
            if e2.get() == each[2]:
                flag=False
        if flag:
            if e4.get() == e5.get():
                datalist.append(e1.get())
                datalist.append(e2.get())
                datalist.append(e3.get())
                datalist.append(e4.get())
                datalist.append(e5.get())
                userlogin_list.append(datalist)
                submitlabel.configure(text="submit successfully")
            else:
                submitlabel.configure(text="Error in signing try again")
        else:
            print("records already exist")
            

    Button(signup_Window,text="SUBMIT",bg="light blue",font=("Times New Roman", 12," bold"),command=submit).grid(row=5,column=1)
    Button(signup_Window,text="CLOSE",bg="light blue",font=("Times New Roman", 12," bold"),command=signup_Window.destroy).grid(row=6,column=1)
    submitlabel.grid(row=7)

def close_window():
    with open("C:\\Users\\sai krishna\\Desktop\\programs\\python programs\\library_project\\userlist.txt","w") as userfile:
        if userlogin_list != []:
            for each in userlogin_list:
                for data in each:
                    if data != "":
                        userfile.write(data+" ")
                userfile.write("\n")
    root.destroy()
    
third_frame = Frame(root,bg= "#F0F0F8")
third_frame.pack(side=TOP,fill=X)

fourth_frame = Frame(root,bg="grey")
fourth_frame.pack(side = TOP)


signup_button=Button(second_frame,text="Sign-up ",font=("Times New Roman", 12," bold"),width=20,anchor=CENTER,borderwidth=3,command=sign_up)
signup_button.pack(side=LEFT,fill=Y)
signin_button=Button(second_frame,text="Sign-in ",font=("Times New Roman", 12," bold"),width=20,anchor=CENTER,borderwidth=3,command=sign_in)
signin_button.pack(side=LEFT,fill=Y)
borrow_button=Button(third_frame,text="Borrow-book ",font=("Times New Roman", 12," bold"),width=20,anchor=CENTER,borderwidth=3,command=borrow_books,state=DISABLED)
borrow_button.pack(side=LEFT,fill=Y)
return_button=Button(third_frame,text="Return-book ",font=("Times New Roman", 12," bold"),width=20,anchor=CENTER,borderwidth=3,command=return_books,state=DISABLED)
return_button.pack(side=LEFT,fill=Y)
donate_button=Button(third_frame,text="Donate-book ",font=("Times New Roman", 12," bold"),width=20,anchor=CENTER,borderwidth=3,command=donate_books,state=DISABLED)
donate_button.pack(side=LEFT,anchor=CENTER,fill=Y)
close_button = Button(third_frame,text=" CLOSE ",font=("Times New Roman", 12," bold"),width=20,anchor=CENTER,borderwidth=3,command=close_window)
close_button.pack(side=LEFT)

bookentry_label = Label(fourth_frame,bg="grey",text="Enter book name :",font=("Times New Roman", 12," bold"),width=30,anchor=CENTER,borderwidth=3)
bookentry_label.grid(row=0,column=0)
bookvariable = StringVar()
bookvariable.set("Enter here")
Entry_book = Entry(fourth_frame,textvariable=bookvariable,bg="light green",font=("Times New Roman", 12," bold"),width=50,state="readonly")
Entry_book.grid(row=1,column=0)
statement_label = Label(fourth_frame,text="",font=("Times New Roman", 14," bold"),width=30,height=3,bg="grey")
statement_label.grid(row=3,column=0,columnspan=4)

root.mainloop()