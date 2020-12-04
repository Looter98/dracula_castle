import tkinter as tk

class Entity:
    #GENERAL
    entity_name = ""
    entity_species = ""

    #DEFENSE
    entity_health = 0 #eneity's health in battle
    entity_defense = 0 #base defense (increased by armour being worn)

    #ATTACK
    entity_attack = 0 #attacks (increasecd by weapons)

    #Inventory
    entity_inv = []
        
    def __init__(self, _name, entity_species, entity_health, entity_defense, entity_attack): #player character object
        self._entity_name = _name
        self._entity_species = entity_species
        self._entity_attack = entity_attack
        self._entity_health = entity_health 
        self._entity_defense = entity_defense


    #Getters and Setters
    #GENERAL
    def getEntity_name( self ):
        return self._entity_name
                            
    def setEntity_name( self, entity_name ):
        self._entity_name = entity_name

    #DEFENSE
    def getEntity_health( self ):
        return self._entity_health
                            
    def setEntity_health( self, entity_health ):
        self._entity_health = entity_health

    def getEntity_defense( self ):
        return self._entity_defense
                            
    def setEntity_defense( self, entity_defense ):
        self._entity_defense = entity_defense

    #ATTACK
    def getEntityt_attack( self ):
        return self._entity_attack
                            
    def setEntity_attack( self, entity_attack ):
        self._entity_attack = entity_attack


class Player_create:
    name = ''

    master = tk.Tk()

    e1 = tk.Entry(master)

    e1.grid(row=0, column=1)

    #name entry system
    def get_name():
        global name
        name=e1.get() #assigning entry text to var
        player = Entity(name, "Human", 100, 10, 20)
        print(player.getEntity_name( ))

    tk.Label(master, 
        text="What is your name?").grid(row=0)

    tk.Button(master, 
              text='Enter', command = get_name ).grid(row=3, 
                                                     column=1, 
                                                        sticky=tk.W, 
                                                           pady=4)







        
