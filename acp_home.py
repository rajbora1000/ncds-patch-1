from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os

t=tk.Tk()
t.title('NCDS - Commisioner ')
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))

def enter_profile():
    os.system('python police_profile.py')
    return
def dashboard():
    return
def search():
    t.destroy()
    os.system('python police_search.py')
    return
def last():
    tkinter.messagebox.showinfo('Title', 'Last Login Session was recorded on 02/28/2020 05:57:51 ')
    return
def logout():
    t.destroy()
    os.system('python login_page_first.py')

t.configure(background = 'grey')

name=Label(t, text='Commissioner - Parambir Singh', fg='orange',font=tkFont.Font(family="Times New Roman", size=40), borderwidth=2, relief="solid")
profile=Button(t, text='Your Profile', command=enter_profile, borderwidth=2, relief="solid")
dash=Button(t, text='Dashboard', command=dashboard, borderwidth=2, relief="solid")
access=Button(t, text='Access Records', command=search, borderwidth=2, relief="solid")
last=Button(t, text='Last Login Details', command=last, borderwidth=2, relief="solid")
logout=Button(t, text='Logout ', command=logout, borderwidth=2, relief="solid")

name.place(x=0, y=50, width=w, height=100)
profile.place(x=0.8*w, y=200, width=0.175*w, height=100)
logout.place(x=0.8*w, y=350, width=0.175*w, height=100)
dash.place(x=50, y=200, width=0.175*w, height=100)
access.place(x=50, y=350, width=0.175*w, height=100)
last.place(x=50, y=500, width=0.175*w, height=100)

mainloop()



'''
from tkinter import*
import os
t=Tk()
t.title("DCP")

t.geometry("1500x800+30+30")

def update_detail():
    os.system('python acp_updates.py')

update=Button(t,text="UPDATE", command = update_detail, borderwidth=2,relief="solid")
update.place(x=50,y=60,width=200,height=50)

create=Button(t,text="CREATE",borderwidth=2,relief="solid")
create.place(x=50,y=120,width=200,height=50)

Delete=Button(t,text="DELETE",borderwidth=2,relief="solid")
Delete.place(x=50,y=180,width=200,height=50)

fn=Label(t, text="FIRST NAME",borderwidth=2,relief="solid")
fn.place(x=1000,y=150,width=70,height=20)
n=Label(t, text="SIDDHANT",borderwidth=2,relief="solid")
n.place(x=1080,y=150,width=100,height=20)

ln=Label(t, text="LAST NAME",borderwidth=2,relief="solid")
ln.place(x=1000,y=210,width=70,height=20)
b=Label(t, text="BURSE",borderwidth=2,relief="solid")
b.place(x=1080,y=210,width=100,height=20)

Ar=Label(t, text="AREA",borderwidth=2,relief="solid")
Ar.place(x=1000,y=270,width=70,height=20)
a=Label(t, text="WORLI",borderwidth=2,relief="solid")
a.place(x=1080,y=270,width=100,height=20)

ge=Label(t, text="GENDER",borderwidth=2,relief="solid")
ge.place(x=1000,y=320,width=70,height=20)
g=Label(t, text="MALE",borderwidth=2,relief="solid")
g.place(x=1080,y=320,width=100,height=20)

''
img=PhotoImage(file='dawood.png')
l1=Label(t,image=img)
l1.place(x=1080,y=320)
''

mainloop()
'''