#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import os
path="k:\python"
os.chdir(path)
def submit():
    getf=first.get()
    getl=last.get()
    geta=age.get()
    
    print(getf,getl,geta)
    
    file=open('database.txt','a')
    file.write(getf+","+getl+","+str(geta)+"\n")
    file.close()
    
    
    print("USER REGISTERED")
    
    entry_first.delete(0,END)
    entry_last.delete(0,END)
    entry_age.delete(0,END)
    
win=Tk()
win.title("REGISTRATION FORM")
win.geometry("350x350")
L1=Label(win,text="PLEASE REGISTER NOW", bg="black",fg="white",font="times 12")
L1.pack()

first=StringVar()
last=StringVar()
age=IntVar()

Label(win,text="First Name", bg="black",fg="white",font="times 12").place(x=50,y=60)
entry_first=Entry(win,textvariable=first)
entry_first.place(x=200,y=60)

Label(win,text="Second Name", bg="black",fg="white",font="times 12").place(x=50,y=120)
entry_second=Entry(win,textvariable=last)
entry_second.place(x=200,y=120)

Label(win,text="Age", bg="black",fg="white",font="times 12").place(x=50,y=180)
entry_age=Entry(win,textvariable=age)
entry_age.place(x=200,y=180)
Button(win,text="SUBMIT", bg="black",fg="white",font="times 12",command=submit).place(x=120,y=230)


# In[ ]:





# In[ ]:





# In[ ]:




