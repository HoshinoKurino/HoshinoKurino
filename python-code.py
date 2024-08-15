import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# input

terminal_username=input('enter user')
terminal_password=input('enter pass')

# login function

def login():
    input_username=en1.get()
    input_password=en2.get()
    if terminal_username==input_username and terminal_password==input_password:
       tk.messagebox.showinfo(title='Login complete',message='You have logged in succesfully')
    else:
        tk.messagebox.showerror(title='Login Fail',message='Login unsuccesful')
    
# main window

pro=tk.Tk()
pro.title('LOGIN SYSTEM')

pro.geometry('500x500')

pro.resizable(False,False)

pro.config(background='#D1CFCE')

# pro.iconbitmap('C:\\Users\\eslamia\\Downloads\\lock.ico')

title=tk.Label(pro,text='LOGIN SYSTEM',font=('courier', 15, 'bold'),bg='black',fg='white')
title.pack(fill='x')

# frame

fr1=tk.Frame(pro,width='300',height='350',bg='whitesmoke')
fr1.pack(pady=30)

# image

# photo=tk.PhotoImage(file='C:\\Users\\eslamia\\Downloads\\lock.png')
# res=photo.subsample(7,7)
# panel=tk.Label(pro,image=res)
# panel.place(x=160,y=60)

# another label

lbl3=tk.Label(fr1,text='Login',font=('courier',20,'bold'),bg='whitesmoke',fg='black')

# label (again)

lbl1=tk.Label(fr1,text='Username:',font=('courier',15,'bold'),bg='whitesmoke',fg='black')

lbl2=tk.Label(fr1,text='Password:',font=('courier',15,'bold'),bg='whitesmoke',fg='black')

# entry

en1=tk.Entry(fr1)            

en2=tk.Entry(fr1)

# login button

btn1=tk.Button(fr1,bg='black', text='Login',fg='white',command=login)

# grid manager

lbl3.grid(row=0,column=1)

lbl1.grid(row=1,column=0,pady=20)
en1.grid(row=1,column=1,pady=20,padx=20)

lbl2.grid(row=2,column=0,)
en2.grid(row=2,column=1,padx=20)

btn1.grid(row=3,column=0,pady=30)



pro.mainloop()




