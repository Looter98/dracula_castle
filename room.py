class Rooms:
    
    room_name = ""
    room_desc = ""

    north = 0
    south = 0
    west = 0
    east = 0
    '''Navigation paths will be controlled by a binary 0 or 1 system
    where when a direction is set to 0, the path will be closed
    however when it is set to 1 the path will be open and the player
    will be allowed to treverse the desitred direction.'''

    def __init__ (north, south, east, west):     
        self._north = north
        self._south = south
        self._west = west
        self._east = east

    
    
    
