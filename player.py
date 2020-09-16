class Entity:
        #GENERAL
        entity_name = ""
        entity_species = ""

        #DEFENSE
        entity_health = 0
        entity_defense = 0
        entity_fire_defense = 0 #defense against fire attacks
        entity_poison_defense = 0 #defense against poison attacks

        #ATTACK
        entity_short_attack = 0 #melee attacks
        entity_long_attack = 0 #ranged attacks
        entity_fire_attack = 0 #fire-based attacks
        entity_poison_attack = 0 #poison-based attacks
        
        #SKILLS
        entity_str = 0 #strength
        entity_dex = 0 #dexterity (agility)
        entity_per = 0 #persuasion
        entity_int = 0 #intellegence/perception
        entity_lck = 0 #luck
        
    def __init__(self, entity_name, entity_species, entity_str, entity_dex, entity_per, entity_int, entity_lck, entity_long_attack, entity_short_attack, entity_defense, entity_fire_defense, entity_poison_defense, entity_fire_attack, entity_poison_attack, entity_str, entity_dex, entity_per, entity_int, entity_lck): #player character object
        self._entity_name = entity_name
        self._entity_species = entity_species
        self._entity_str = entity_str
        self._entity_dex = entity_dex
        self._entity_per = entity_per
        self._entity_int = entity_int
        self._entity_lck = entity_lck
        self._entity_long_attack = entity_long_attack
        self._entity_short_attack = entity_short_attack
        self._entity_fire_attack = entity_fire_attack
        self._entity_poison_attack = entity_poison_attack
        self._entity_defense = entity_defense
        self._entity_fire_defense = entity_fire_defense
        self._entity_poison_defense = entity_poison_defense

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

    def getEntity_fire_defense ( self ):
        return self._entity_fire_defense 

    def setEntity_fire_defense ( self, entity_fire_defense ):
        self._entity_fire_defense  = entity_fire_defense
        
    def getEntity_poison_defense ( self ):
        return self._entity_poison_defense

    def setEntity_poison_defense ( self, entity_poison_defense ):
        self._entity_poison_defense  = entity_poison_defense

    #ATTACK
    def getEntity_short_attack( self ):
        return self._entity_short_attack
                            
    def setEntity_short_attack( self, entity_short_attack ):
        self._entity_short_attack = entity_short_attack

    def getEntity_long_attack( self ):
        return self._entity_long_attack
                            
    def setEntity_long_attack( self, entity_long_attack ):
        self._entity_long_attack = entity_long_attack

    def getEntity_fire_attack ( self ):
        return self._entity_fire_attack 

    def setEntity_fire_attack ( self, entity_fire_attack ):
        self._entity_fire_attack = entity_fire_attack
        
    def getEntity_poison_attack( self ):
        return self._entity_poison_attack

    def setEntity_poison_attack ( self, entity_poison_attack ):
        self._entity_poison_attack = entity_poison_attack
        
    #SKILLS
    def getEntity_str( self ):
        return self._entity_str
                            
    def setEntity_str( self, entity_str ):
        self._entity_str = entity_str

    def getEntity_dex( self ):
        return self._entity_dex
                            
    def setEntity_dex( self, entity_dex ):
        self._entity_dex = entity_dex

    def getEntity_per ( self ):
        return self._entity_per 

    def setEntity_per ( self, entity_per ):
        self.entity_per = entity_per
        
    def getEntity_int ( self ):
        return self._entity_int

    def setEntity_int ( self, entity_int ):
        self._entity_int = entity_int

    def getEntity_lck( self ):
        return self._entity_lck

    def setEntity_lck ( self, entity_lck ):
        self._entity_lck  = entity_lck
        
                
    

            

        
        
    
