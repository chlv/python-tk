#     -- coding:utf-8 --

import tkinter as tk
from tkinter import ttk
import time
from threading import Thread
from queue import Queue
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from os import path


class GUI():
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Python GUI")
		self.createwidgets()


	def menucommand1(self):
		print("This is menucommand1")

	def	menucommand2(self):
		print("This is menucommand2")

	def menucommand3(self):
		print("This is menucommand3")

	def aboutinfo(self):
		tk.messagebox.showinfo("GUI Info","Author:Lv Chao\n2017-05-19")

	def	buttonaction(self):
		self.scroll.insert(tk.INSERT,str(self.tab1cb1var.get())+"\n")
		self.scroll.insert(tk.INSERT,str(self.tab1entry.get())+"\n")
		if self.tab1cb2var.get() == 1:
			self.scroll.insert(tk.INSERT,str(time.asctime(time.localtime(time.time())))+"\n")
		else:
			self.scroll.insert(tk.INSERT,"Time is not selected"+"\n")

	def sleeptime(self):
		for i in range(6):
			time.sleep(10)
			print(str(i))

	def multithread(self):
		self.mthread = Thread(target=self.sleeptime)    # targe = refer  not a real function
		self.mthread.setDaemon(True)
		self.mthread.start()


	def radiofun(self):
		self.radionumber = self.radiovar.get()
		if self.radionumber == 1:
			self.multithread()
			print(10,self.mthread)
		elif self.radionumber == 2:
			self.multithread()
			print(20,self.mthread)
		else:
			self.multithread()
			print(30,self.mthread)


	def spinaction(self):
		print(self.spin.get())

	def showaction(self):
		self.tab2scr.insert(tk.INSERT,"Combo box current variable:"+str(self.combox.get())+"\n")
		self.tab2scr.insert(tk.INSERT,"Spin box current variable:"+str(self.spin.get())+"\n")

	def broweraction(self):
		self.tab2scr.insert(tk.INSERT,"Open File Location:\n")
		self.fl = path.dirname(__file__)
		self.filelocvar = filedialog.askopenfilename(parent=self.root,initialdir=self.fl)
		self.tab2scr.insert(tk.INSERT,self.filelocvar+"\n")
		self.fileloc.delete(0,tk.END)
		self.fileloc.insert(0,self.filelocvar)

	def createwidgets(self):
		# create menu
		menubar = tk.Menu(self.root)
		self.root.config(menu=menubar)
		settingmenu = tk.Menu(menubar,tearoff=0)

		settingmenu.add_command(label="label-1",command=self.menucommand1)
		settingmenu.add_command(label="label-2",command=self.menucommand2)
		settingmenu.add_separator()
		settingmenu.add_command(label="label-3",command=self.menucommand3)
		menubar.add_cascade(label="Setting",menu=settingmenu)


		helpmenu = tk.Menu(menubar)
		helpmenu.add_command(label="About",command=self.aboutinfo)
		menubar.add_cascade(label="Help",menu=helpmenu)

		#   create tabs1
		controltabs = ttk.Notebook(self.root)
		tab1 = ttk.Frame(controltabs)
		tab2 = ttk.Frame(controltabs)
		controltabs.add(tab1,text="Tab1")
		controltabs.add(tab2,text="Tab2")
		controltabs.grid(column=0,row=0,stick=tk.W)

		#	create tableframe
		tab1frame = ttk.Labelframe(tab1,text="Tab1-toplevel-Frame")
		tab1frame.grid(column=0,row=0)
		tab2frame = ttk.Labelframe(tab2,text="Tab2-toplevel-Frame")
		tab2frame.grid(column=0,row=0)

		#	create label
		tab1label1 = ttk.Label(tab1frame,text="Please Enter your name:")
		tab1label1.grid(column=0,row=0,stick=tk.W)
		tab2label2 = ttk.Label(tab2frame,text="Please Select a Number:")
		tab2label2.grid(column=0,row=0,stick=tk.W)
		tab2labelcomment = ttk.Label(tab2frame,text="#Use sleep and MultiThread#")
		tab2labelcomment.grid(column=1,row=0,stick=tk.W)

		#create entry
		self.tab1entryinput = tk.StringVar()
		self.tab1entry = ttk.Entry(tab1frame,textvariable=self.tab1entryinput)
		self.tab1entry.grid(column=1,row=0,stick=tk.W)
		self.tab1entry.focus()

		#create checkbutton
		self.tab1cb1var = tk.IntVar()
		self.tab1cb2var = tk.IntVar()

		self.tab1cb1 = ttk.Checkbutton(tab1frame,text="Name",variable=self.tab1cb1var,state="disabled")
		self.tab1cb2 = ttk.Checkbutton(tab1frame,text="Time",variable=self.tab1cb2var)
		self.tab1cb1.grid(column=0,row=1,stick=tk.W)
		self.tab1cb2.grid(column=0,row=2,stick=tk.W)
		self.tab1cb1var.set(1)

		#create button
		tab1button = ttk.Button(tab1frame,text="Run",command=self.buttonaction)
		tab1button.grid(column=1,row=2,stick=tk.W)

		#create scrolltext
		scrolW = 50
		scrolH = 8
		self.scroll = scrolledtext.ScrolledText(tab1frame,width=scrolW,height=scrolH,wrap=tk.WORD)
		self.scroll.grid(column=0,columnspan=3,stick=tk.W)

		#create radiobutton
		self.radiovar = tk.IntVar()
		for i in range(1,4):
			self.radiobutton = ttk.Radiobutton(tab2frame,text=i,variable=self.radiovar,value=i,command=self.radiofun)
			self.radiobutton.grid(column=0,row=i,stick=tk.W)

		# create combo box
		self.comboxvar = tk.IntVar()
		self.combox = ttk.Combobox(tab2frame,value=(1,2,3,4,5,10),width=6,textvariable=self.comboxvar,state="readonly")
		self.combox.grid(column=0,row=5,stick=tk.W)
		self.combox.current(0)

		# create spin box
		self.spinvar = tk.IntVar()
		self.spin = tk.Spinbox(tab2frame,from_=1,to=20,width=5,command=self.spinaction,state="readonly")
		self.spin.grid(column=0,row=6,stick=tk.W)

		# create show button
		self.show = ttk.Button(tab2frame,text="Show",command=self.showaction)
		self.show.grid(column=1,row=6,stick=tk.W)

		# create show info label
		showlabel = ttk.Label(tab2frame,text="Show Widget current info:")
		showlabel.grid(column=0,row=7,stick=tk.W)

		# create show info windows scrolltext
		self.tab2scr = tk.scrolledtext.ScrolledText(tab2frame,width=scrolW,height=scrolH,wrap=tk.WORD)
		self.tab2scr.grid(column=0,row=8,columnspan=2,stick=tk.EW)

		# file manage
		filemanage = ttk.Labelframe(tab2,text="File Manage")
		filemanage.grid(column=0,row=1,stick=tk.W)

		self.browse = ttk.Button(filemanage,text="Browse",command=self.broweraction)
		self.browse.grid(column=0,row=0,padx=5,pady=5,stick=tk.W)

		self.filelocvar = tk.StringVar()
		self.fileloc = ttk.Entry(filemanage,width=40)
		self.fileloc.grid(column=1,row=0,padx=25,pady=5,stick=tk.W)
		self.fileloc.delete(0,tk.END)
		self.fileloc.insert(0,"<default>")



gui = GUI()
gui.root.mainloop()


