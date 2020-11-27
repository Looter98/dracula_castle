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
        
    def __init__(self, entity_name, entity_species): #player character object
        self._entity_name = entity_name
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

    def getEntity_species( self ):
        return self._entity_species
                            
    def setEntity_species( self, entity_species ):
        self._entity_species = entity_species

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
        
        
