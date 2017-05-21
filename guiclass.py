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
		tab1label1.grid(column=0,row=0)
		tab2label2 = ttk.Label(tab2frame,text="Please input a number:")
		tab2label2.grid(column=0,row=0)

		#create entry
		tab1entryinput = tk.StringVar()
		tab1entry = ttk.Entry(tab1frame,textvariable=tab1entryinput)
		tab1entry.grid(column=1,row=0)
		tab1entry.focus()

		#create checkbutton
		tab1cb1var = tk.IntVar()
		tab1cb2var = tk.IntVar()

		tab1cb1 = ttk.Checkbutton(tab1frame,text="Name",variabel=tab1cb1var)



gui = GUI()
gui.root.mainloop()


