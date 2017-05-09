<<<<<<< HEAD
#       --coding:utf-8 --

import Tkinter as tk
import ttk

class APP():
	def __init__(self,master):
		frame = tk.Frame(master)
		frame.pack()

		self.button = tk.Button(frame,text="QUIT",fg="red",command=frame.quit)
		self.button.pack(side="left")
		self.sayhello = tk.Button(frame,text="Show Message",command=self.saywelcome)
		self.sayhello.pack(side="left")

	def saywelcome(self):
		print("Welcome to the Thinter.")


def open():
	print "just open a file"

def save():
	print "just save a file"

def edit():
	print "just edit a file"
root = tk.Tk()
root.title("Python_TK")
#root.resizable(0,0)
app = APP(root)
menu_bar = tk.Menu(root)
filemenu = tk.Menu(menu_bar,tearoff=0)
filemenu.add_command(label="Open",command=open)
filemenu.add_command(label="Save",command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)
menu_bar.add_cascade(label="File",menu=filemenu)

editmenu = tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=open)
editmenu.add_command(label="Copy",command=save)
editmenu.add_command(label="Paste",command=edit)

helpmenu = tk.Menu(menu_bar,tearoff=0)
helpmenu.add_command(label="About",command=open)
menu_bar.add_cascade(label="Help",menu=helpmenu)

#ttk.Label(root,text="Ver:0.0.0.1").grid(column=0,row=0)

root.config(menu=menu_bar)
root.mainloop()
=======
#       --coding:utf-8 --

import Tkinter as tk
import ttk

class APP():
	def __init__(self,master):
		frame = tk.Frame(master)
		frame.pack()

		self.button = tk.Button(frame,text="QUIT",fg="red",command=frame.quit)
		self.button.pack(side="left")
		self.sayhello = tk.Button(frame,text="Show Message",command=self.saywelcome)
		self.sayhello.pack(side="left")

	def saywelcome(self):
		print("Welcome to the Thinter.")


def open():
	print "just open a file"

def save():
	print "just save a file"

def edit():
	print "just edit a file"
root = tk.Tk()
root.title("Python_TK")
#root.resizable(0,0)
app = APP(root)
menu_bar = tk.Menu(root)
filemenu = tk.Menu(menu_bar,tearoff=0)
filemenu.add_command(label="Open",command=open)
filemenu.add_command(label="Save",command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)
menu_bar.add_cascade(label="File",menu=filemenu)

editmenu = tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=open)
editmenu.add_command(label="Copy",command=save)
editmenu.add_command(label="Paste",command=edit)

helpmenu = tk.Menu(menu_bar,tearoff=0)
helpmenu.add_command(label="About",command=open)
menu_bar.add_cascade(label="Help",menu=helpmenu)

#ttk.Label(root,text="Ver:0.0.0.1").grid(column=0,row=0)

root.config(menu=menu_bar)
root.mainloop()
>>>>>>> 870930f121641ccdf1fb9bac41aa28a1c16207e7
