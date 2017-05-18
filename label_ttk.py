#      -- coding:utf-8 --

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
import time
from threading import Thread
from queue import  Queue
import customerQueue


root = tk.Tk()
root.title("python")
# root.iconbitmap(r'C:\Python34\DLLs\pyc.ico')
# root.withdraw()

# independence message box
tk.messagebox.showinfo("","This ia an independence message box")
# add tabs
tablecontrol = ttk.Notebook(root)

tab1 = ttk.Frame(tablecontrol)
tablecontrol.add(tab1,text="tab1")
tab2 = tk.Frame(tablecontrol)
tablecontrol.add(tab2,text="tab2")

tablecontrol.grid(column=0,row=0,stick=tk.W)


# top level labelframs
toplevel = ttk.Labelframe(tab1,text="Top-Level")
toplevel.grid(column=0,row=1)
# label enter you name
label1 = ttk.Label(toplevel,text="Please Enter Your Name:")
label1.grid(column=0,row=0,stick=tk.W)
# entry show you name and set focus
name = tk.StringVar()
entername = ttk.Entry(toplevel,width=12,textvariable=name)
entername.grid(column=0,row=1,stick=tk.W)
entername.focus()
# button and action
def click_button():
	action.configure(text="Your Name is: "+name.get()+"\nChoose number is: "+number.get())
	threadusequeue()
#	customerQueue.writetoscreen()

def usequeue():
	queue = Queue()
	count = 0
	for i in range(6):
		count += 1
		queue.put("Message from Queue:" + str(i) )
	while count >= 0:
		print(queue.get())
		count -= 1

def threadusequeue():
	tusequeue = Thread(target=usequeue)
	tusequeue.setDaemon(True)
	tusequeue.start()

action = ttk.Button(toplevel,text="Click Me",command=click_button)
action.grid(column=1,row=1,stick=tk.W)
#action.configure(state="disable")

#  label show enter you number
lable2 = ttk.Label(toplevel,text="Please Choose a Number:")
lable2.grid(column=0,row=3)
# combo box
number = tk.StringVar()
enternumber = ttk.Combobox(toplevel,width=12,textvariable=number,state="readonly")
enternumber["value"]=(1,2,3,4)
enternumber.grid(column=1,row=3,stick=tk.W)
enternumber.current(0)

# checkbox
cb1disable = tk.IntVar()
checkbutton1 = ttk.Checkbutton(toplevel,text="Disable",variable=cb1disable)
checkbutton1.grid(column=0,row=4,stick=tk.W)


cb2enable = tk.IntVar()
checkbutton2 = ttk.Checkbutton(toplevel,text="Enable",variable=cb2enable)
checkbutton2.grid(column=1,row=4,stick=tk.W)

# radio在top level里，root颜色被盖住，没有显示
# radio button
COLOR1 = "Red"
COLOR2 = "Blue"
COLOR3 = "Yellow"

def radiofun():
	radiocolor = radvar.get()
	if radiocolor == 1:
		root.configure(background=COLOR1)
	elif radiocolor == 2:
		root.configure(background=COLOR2)
	elif radiocolor == 3:
		root.configure(background=COLOR3)


radvar = tk.IntVar()
radio1 = tk.Radiobutton(toplevel,text=COLOR1,variable=radvar,value=1,command=radiofun)
radio1.grid(column=0,row=5,stick=tk.W)

radio2 = tk.Radiobutton(toplevel,text=COLOR2,variable=radvar,value=2,command=radiofun)
radio2.grid(column=1,row=5,stick=tk.W)

radio3 = tk.Radiobutton(toplevel,text=COLOR3,variable=radvar,value=3,command=radiofun)
radio3.grid(column=2,row=5,stick=tk.W)




#  label frame
labelsframe = ttk.Labelframe(toplevel,text="Label Frame")
labelsframe.grid(column=0,row=6,stick=tk.W)

ttk.Label(labelsframe,text="First").grid(column=0,row=0,stick=tk.W)
ttk.Label(labelsframe,text="Second").grid(column=0,row=1,stick=tk.W)
ttk.Label(labelsframe,text="Third").grid(column=0,row=2,stick=tk.W)

def choose__message():
	answer = tk.messagebox.askyesno("Python choose message","Do you real want to open a file")
	print(answer)

menubar = tk.Menu(root)
root.config(menu=menubar)

filemenu = tk.Menu(menubar,tearoff=0)

filemenu.add_command(label="Open",command=choose__message)
filemenu.add_command(label="Call Button",command=click_button)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)

menubar.add_cascade(label="Setting",menu=filemenu)



# define message box
def aboutmessage():
#	tk.messagebox.showinfo("Python Info Message Box","Author:LC  2017-05-11")
#	tk.messagebox.showwarning("Python Warning Message Box","You need to add comment")
	tk.messagebox.showerror("Python Error Message Box","You'd better use python3.\nPython 2 not add messagebox package ")

helpmenu = tk.Menu(menubar)
helpmenu.add_command(label="About",command=aboutmessage)
menubar.add_cascade(label="Help",menu=helpmenu)


# add tab2 toplevel
topleveltab2 = ttk.Labelframe(tab2,text="toplevel TAB2")
topleveltab2.grid(column=0,row=0)
tab2label1 = ttk.Label(topleveltab2,text="this is tab2")
tab2label1.grid(column=0,row=0,stick=tk.W)

# add scroll text
scrolW = 40
scrolH = 10
scr = tk.scrolledtext.ScrolledText(topleveltab2,width=scrolW,height=scrolH,wrap=tk.WORD)
scr.grid(column=0,columnspan=100)

def multithread():
	thread1 = Thread(target=_spin)
	thread1.setDaemon(True)
	thread1.start()
	print(thread1)

def _spin():
#	value = spin.get()
#	print(value)
	for i in range(10):
		time.sleep(5)
		scr.insert(tk.INSERT,str(i) + "\n")
# add spin box
spin = tk.Spinbox(topleveltab2,from_=10,to=20,width=5,bd=6,command=multithread)
spin.grid(column=0,row=4)



root.mainloop()