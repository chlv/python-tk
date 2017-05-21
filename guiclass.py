#     -- coding:utf-8 --

import tkinter as tk
from tkinter import ttk
import time
from threading import Thread
from queue import Queue
from tkinter import messagebox
from tkinter import scrolledtext


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
		time.sleep(10)

	def multithread(self):
		self.mthread = Thread(target=self.sleeptime())
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

		tab1label1 = ttk.Label(tab1frame,text="Please Enter your name:")
		tab1label1.grid(column=0,row=0,stick=tk.W)
		tab2label2 = ttk.Label(tab2frame,text="Please Select a Number:")
		tab2label2.grid(column=0,row=0,stick=tk.W)

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







gui = GUI()
gui.root.mainloop()


