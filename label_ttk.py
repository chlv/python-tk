#      -- coding:utf-8 --

import Tkinter as tk
import ttk

root = tk.Tk()
root.title("python")

# label enter you name
label1 = ttk.Label(root,text="Please Enter Your Name:")
label1.grid(column=0,row=0,stick=tk.W)
# entry show you name and set focus
name = tk.StringVar()
entername = ttk.Entry(root,width=12,textvariable=name)
entername.grid(column=0,row=1,stick=tk.W)
entername.focus()
# button and action
def click_button():
	action.configure(text="Your Name is: "+name.get()+"\nChoose number is: "+number.get())
action = ttk.Button(root,text="Click Me",command=click_button)
action.grid(column=1,row=1,stick=tk.W)
#action.configure(state="disable")

#  label show enter you number
lable2 = ttk.Label(root,text="Please Choose a Number:")
lable2.grid(column=0,row=3)
# combo box
number = tk.StringVar()
enternumber = ttk.Combobox(root,width=12,textvariable=number,state="readonly")
enternumber["value"]=(1,2,3,4)
enternumber.grid(column=1,row=3,stick=tk.W)
enternumber.current(0)

#checkbox
cb1disable = tk.IntVar()
checkbutton1 = ttk.Checkbutton(root,text="Disable",variable=cb1disable)
checkbutton1.grid(column=0,row=4,stick=tk.W)


cb2enable = tk.IntVar()
checkbutton2 = ttk.Checkbutton(root,text="Enable",variable=cb2enable)
checkbutton2.grid(column=1,row=4,stick=tk.W)

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
radio1 = tk.Radiobutton(root,text=COLOR1,variable=radvar,value=1,command=radiofun)
radio1.grid(column=0,row=5,stick=tk.W)

radio2 = tk.Radiobutton(root,text=COLOR2,variable=radvar,value=2,command=radiofun)
radio2.grid(column=1,row=5,stick=tk.W)

radio3 = tk.Radiobutton(root,text=COLOR3,variable=radvar,value=3,command=radiofun)
radio3.grid(column=2,row=5,stick=tk.W)




#  label frame
labelsframe = ttk.Labelframe(root,text="Label Frame")
labelsframe.grid(column=0,row=6,padx=10,pady=10)

ttk.Label(labelsframe,text="First").grid(column=0,row=0,stick=tk.W)
ttk.Label(labelsframe,text="Second").grid(column=0,row=1,stick=tk.W)
ttk.Label(labelsframe,text="Third").grid(column=0,row=2,stick=tk.W)



root.mainloop()