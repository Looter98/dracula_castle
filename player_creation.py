import tkinter as tk

#name entry system
def get_name():
    name=e1.get() #assigning entry text to var
    print("your name is",name)

master = tk.Tk()
tk.Label(master, 
         text="What is your name?").grid(row=0)

e1 = tk.Entry(master)

e1.grid(row=0, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command = get_name).grid(row=3, 
                                                column=1, 
                                                    sticky=tk.W, 
                                                       pady=4)
'''
from tkinter import *

root = Tk()
w1 = Radiobutton(root, text="option 1")
w2 = Radiobutton(root, text="option 2")
#
w1.pack()
w2.pack()
root.mainloop()
'''
