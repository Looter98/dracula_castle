

from tkinter import *
from tkinter.scrolledtext import *   #lets us use a ScrolledText widget 
from tkinter import ttk              #extended tkinker 
import random

class GUI:

    rooms = [  ]
    img_ob = [ ]
    
    def __init__(self,parent):

        self._objects = ['Old cheese', 'coins', 'new cheese' , 'key', 'coins','butter', 'soap']
        self._your_items = []

        #blank list of all rooms
        self._room_items = ['','','','','','','','','','',
                            '','','','','','','','','']

        
        for i in range(len(self._objects)):
            rand = random.randint(0,18)
            if(self._room_items[rand] == ''):
                self._room_items[rand] = self._objects[i]
            else:
                continue
        
        print(self._room_items)

        self._n = [1,2,3,99,5,99,9,6,99,10,99,99,99,12,18,99,16,99,99]
        self._s = [99,0,1,2,99,4,7,99,99,6,9,99,13,99,99,99,17,99,15,99]
        self._e = [99,12,15,99,1,99,4,8,99,99,11,99,99,14,99,16,99,99,19,99]
        self._w = [99,4,99,99,6,99,99,99,7,99,99,10,1,99,13,2,15,5,99,18]

        self._curr_room = 0
        #-----image objects------
        self._eh = PhotoImage(file='images/Entrance Hall.gif')
        self._mh = PhotoImage(file='images/Main Hall.gif')
        self._bh = PhotoImage(file='images/Back Hall.gif')
        ###Post usb break
        self._sr = PhotoImage(file='images/Sun Room.gif')
        self._wh = PhotoImage(file='images/West Hallway.gif')
        self._tl = PhotoImage(file='images/Toilet.gif')
        self._wt = PhotoImage(file='images/West Tower.gif')
        self._dr = PhotoImage(file='images/Drawing Room.gif')
        self._li = PhotoImage(file='images/Library.gif')
        self._bd = PhotoImage(file='images/Bedroom.gif')
        self._de = PhotoImage(file='images/Dressing Room.gif')
        self._br = PhotoImage(file='images/Bath Room.gif')
        self._cr = PhotoImage(file='images/Corridor.gif')
        self._lo = PhotoImage(file='images/Lounge.gif')
        self._et = PhotoImage(file='images/East Tower.gif')
        self._pa = PhotoImage(file='images/Passage.gif')
        self._sc = PhotoImage(file='images/Scullery.gif')
        self._cl = PhotoImage(file='images/Cellar.gif')
        self._kt = PhotoImage(file='images/Kitchen.gif')
        self._pn = PhotoImage(file='images/Pantry.gif')
        

        #----adding to list--
        GUI.img_ob.append(self._eh)
        GUI.img_ob.append(self._mh)
        GUI.img_ob.append(self._bh)
        ###Post usb break
        GUI.img_ob.append(self._sr)
        GUI.img_ob.append(self._wh)
        GUI.img_ob.append(self._tl)
        GUI.img_ob.append(self._wt)
        GUI.img_ob.append(self._dr)
        GUI.img_ob.append(self._li)
        GUI.img_ob.append(self._bd)
        GUI.img_ob.append(self._de)
        GUI.img_ob.append(self._br)
        GUI.img_ob.append(self._cr)
        GUI.img_ob.append(self._lo)
        GUI.img_ob.append(self._et)
        GUI.img_ob.append(self._pa)
        GUI.img_ob.append(self._sc)
        GUI.img_ob.append(self._cl)
        GUI.img_ob.append(self._kt)
        GUI.img_ob.append(self._pn)
        
        
        self._room_des = ["Entrance Hall - Its the entrance",
                          "Main Hall - This is the main hall",
                          "Back Hall - This is the back hall",
                          "Sun Room - This is the Sun Room",
                          "West Hallway - This is the West Hallway",
                          "Toilet - This is the Toilet",
                          "West Tower - This is the West Tower",
                          "Drawing Room - This is the Drawing Room",
                          "Library - This is the Library",
                          "Bedroom - This is the Bedroom",
                          "Dressing Room - This is the Dressing Room",
                          "Bath Room - This is the Bath Room",
                          "Corridor - This is the Corridor",
                          "Lounge - This is the Lounge",
                          "East Tower - This is the East Tower",
                          "Passage - This is the Passage",
                          "Scullery - This is the Scullery",
                          "Cellar - This is the Cellar",
                          "Kitchen - This is the Kitchen",
                          "Pantry - This is the Pantry"
                         ]

        #room displaying label
        self._room = Label(parent, image = GUI.img_ob[self._curr_room])
        self._room.pack()

        #Movement buttons----------

        self._btn_north = Button(parent, text="North", command = lambda x = "North": self.move(x))
        self._btn_north.place(x=160, y=230)
        self._btn_south = Button(parent, text="South", command = lambda x = "South": self.move(x))
        self._btn_south.place(x=260, y=230)
        self._btn_east = Button(parent, text="East", command = lambda x = "East": self.move(x))
        self._btn_east.place(x=210, y=230)
        self._btn_west = Button(parent, text="West", command = lambda x = "West": self.move(x))
        self._btn_west.place(x=310, y=230)

        #descript display label----------
        self._descr_lbl = Label(parent, text= "Information")
        self._descr_lbl.place(x=100, y=300)
        self._st = ScrolledText(root,width=40,height=10,wrap='word',state='disabled',bg='grey')
        self._st.place(x=100, y=350)
        self._st.configure(state='normal')  #change the state property to write on it
        self._st.insert(END,self._room_des[self._curr_room]+ "\n")
        self._st.configure(state='disabled')

        #----your inventory---------
        
        self._inv = Label(parent, text = '', width=5, height=5, bg='green')
        self._inv.place(x = 10, y= 10)
        

    def move(self, btn):

    
        print(self._curr_room)
        new_items = ''
        print("north",self._n[self._curr_room])
        if(btn == "North"):
            if(self._n[self._curr_room] != 99):
                self._curr_room = self._n[self._curr_room]
                self._room.config(image = GUI.img_ob[self._curr_room])  #changing image object

                self._st.configure(state='normal')  #change the state property to write on it
                self._st.insert(END,self._room_des[self._curr_room]+ "\n")
                if (self._room_items[self._curr_room] != ''):
                    self._st.insert(END,self._room_items[self._curr_room]+ "\n")

                    #---------adding item to your list -----------
                    self._your_items.append(self._room_items[self._curr_room])
                    for i in range(len(self._your_items)):
                        new_items += self._room_items[self._curr_room]
                self._st.configure(state='disabled')
                #add item to inventory
                '''
                for item in range( len(things) ):    #looping through length of list
                    st.insert(END,things[item]+ "\n") #adding list onto scrolled text area
                '''
                #---update inventory-------------
                self._inv.config(text= new_items)
        
        elif(btn == "South" ):
            if(self._s[self._curr_room] != 99):
                self._curr_room = self._s[self._curr_room]
                self._room.config(image = GUI.img_ob[self._curr_room])

                self._st.configure(state='normal')  #change the state property to write on it
                self._st.insert(END,self._room_des[self._curr_room]+ "\n")
                if (self._room_items[self._curr_room] != ''):
                    self._st.insert(END,self._room_items[self._curr_room]+ "\n")
                    #---------adding item to your list -----------
                    self._your_items.append(self._room_items[self._curr_room])
                    for i in range(len(self._your_items)):
                        new_items += self._room_items[self._curr_room]
                self._st.configure(state='disabled')
                #add item to inventory
                '''
                for item in range( len(things) ):    #looping through length of list
                    st.insert(END,things[item]+ "\n") #adding list onto scrolled text area
                '''
                #---update inventory-------------
                self._inv.config(text= new_items)
                
        elif(btn == "East" ):
            if(self._e[self._curr_room] != 99):
                self._curr_room = self._e[self._curr_room]
                self._room.config(image = GUI.img_ob[self._curr_room])

                self._st.configure(state='normal')  #change the state property to write on it
                self._st.insert(END,self._room_des[self._curr_room]+ "\n")
                if (self._room_items[self._curr_room] != ''):
                    self._st.insert(END,self._room_items[self._curr_room]+ "\n")
                    #---------adding item to your list -----------
                    self._your_items.append(self._room_items[self._curr_room])
                    for i in range(len(self._your_items)):
                        new_items += self._room_items[self._curr_room]
                self._st.configure(state='disabled')
                #add item to inventory
                '''
                for item in range( len(things) ):    #looping through length of list
                    st.insert(END,things[item]+ "\n") #adding list onto scrolled text area
                '''
                #---update inventory-------------
                self._inv.config(text= new_items)
                
        elif(btn == "West" ):
            if(self._w[self._curr_room] != 99):
                self._curr_room = self._w[self._curr_room]
                self._room.config(image = GUI.img_ob[self._curr_room])

                self._st.configure(state='normal')  #change the state property to write on it
                self._st.insert(END,self._room_des[self._curr_room]+ "\n")
                if (self._room_items[self._curr_room] != ''):
                    self._st.insert(END,self._room_items[self._curr_room]+ "\n")
                    #---------adding item to your list -----------
                    self._your_items.append(self._room_items[self._curr_room])
                    for i in range(len(self._your_items)):
                        new_items += self._room_items[self._curr_room]
                self._st.configure(state='disabled')
                #add item to inventory
                '''
                for item in range( len(things) ):    #looping through length of list
                    st.insert(END,things[item]+ "\n") #adding list onto scrolled text area
                '''
                #---update inventory-------------
                self._inv.config(text= new_items)
                
        



        
        
        



#----main routine----------

root = Tk()
root.geometry("500x500")
root.title("navigation")

gui = GUI(root)

root.mainloop()

