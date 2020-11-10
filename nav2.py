

from tkinter import *

class GUI:

    rooms = [  ]
    img_ob = [ ]
    
    def __init__(self,parent):

        self._n = [1,2,3]
        self._s = [99,0,1]
        self._e = [99,12,15]
        self._w = [99,4,99]

        self._curr_room = 0
        #-----image objects------
        self._eh = PhotoImage(file='images/Entrance Hall.gif')
        self._mh = PhotoImage(file='images/Main Hall.gif')
        self._bh = PhotoImage(file='images/Back Hall.gif')

        #----adding to list--
        GUI.img_ob.append(self._eh)
        GUI.img_ob.append(self._mh)
        GUI.img_ob.append(self._bh)
        
        self._room_des = [{"Entrance Hall":"Its the entrance"},
                          {"Main Hall": "This is the main hall"},
                          {"Back Hall": "This is the back hall"}
                         ]

        #room displaying label
        self._room = Label(parent, image = GUI.img_ob[self._curr_room])
        self._room.pack()

        #descript display label----------
        

        self._btn_north = Button(parent, text="North", command = lambda x = "North": self.move(x))
        self._btn_north.pack()
        self._btn_south = Button(parent, text="South", command = lambda x = "South": self.move(x))
        self._btn_south.pack()
        #self._btn_east = Button(parent, text="East", command = lambda move())
        #self._btn_east.pack()
        #self._btn_west = Button(parent, text="West", command = lambda move())
        #self._btn_west.pack()

    def move(self, btn):
        
        if(btn == "North"):
            if(self._n[self._curr_room] != 99):
                self._curr_room = self._n[self._curr_room]
                self._room.config(image = GUI.img_ob[self._curr_room])  #changing image object
        elif(btn == "South" ):
            if(self._s[self._curr_room] != 99):
                self._curr_room = self._s[self._curr_room]
                self._room.config(image = GUI.img_ob[self._curr_room])

        
        



        
        
        



#----main routine----------

root = Tk()
root.geometry("500x500")
root.title("navigation")

gui = GUI(root)

root.mainloop()

