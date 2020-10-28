class Rooms:
    
    def __init(self, pName, pContents, pNorth, pSouth, pWest, pEast):
        self._name = pName
        self._contents = pContents
        self._north = pNorth
        self._south = pSouth
        self._east = pEast
        self._west = pWest

    def getRoom(self):
        return self.name
    
    def north(self):
        return self._north

rooms = {0:['Dining','A dining room',1],
         1:['Hallway','A hallway'],
         2:['Kitchen','A kitchen']}

enterance = Rooms(rooms[i],rooms[0][0],rooms[0][1],rooms[0][2])
rooms = {0:enterance}
room = 0

while(True):
    pChoice = input('Enter the direction you wish to travel:')
    print(rooms_ob[room], rooms_ob.getRoom())
    if(rooms_ob[room].north() != 99):
        print("You can go north(N)")
        if(pChoice == 'n'):
            room = rooms_ob.north()
            break
            
    if(rooms_ob[room].south() != 99):
        print("You can go south(S)")
        if(pChoice == 's'):
            room = rooms_ob.south()
            break
            
    if(rooms_ob[room].west() != 99):
        print("You can go west(W)")
        if(pChoice == 'w'):
            room = rooms_ob.west()
            break

    if(rooms_ob[room].east() != 99):
        print("You can go east(E)")
        if(pChoice == 'e'):
            room = rooms_ob.east()
            break
        
    pChoice = input('Enter the direction you wish to travel:') #REPLACE W/Button LATER
    continue
        
