class Rooms:
    room_name = ""
    room_desc = ""
    room_position = []
    room_links = []
    room_player = []
    #room_chest = #Calls a chest to appear in the room 
    #room_fight = #Calls a fight to play out when you enter the room
    

    def __init__ (room_name, room_desc):
        self._room_name = room_name
        self._room_desc = room_desc
        self._room_position = room_position
        self._room_links = room_links

    def player_travel():
        if("N" in self._player_room and "S" in self._player_room + [0,1] ):
            pass

        if("W" in self._player_room and "E" in self._player_room + [1,0] ):
            pass

        if("N" in self._player_room and "S" in self._player_room + [0,1] ):
            pass

        if("S" in self._player_room and "N" in self._player_room + [0,-1] ):
            pass

        else:
            print("You are trapped")
        
    
