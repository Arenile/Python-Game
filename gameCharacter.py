# -*- coding: utf-8 -*-

#----- Class for creating characters for games, top-down pixel art style -----
#----- Author: Thomas Raymond -----

import pygame, os, GameConfig

#Actual object for game characters
class gameCharacter(object):
    _registry = []

    #Initialized characters should have a few important traits by default in their constructor: 
    #Name, File for Pixel art, optional file for full art, and their stats (given as a tuple?)

    def __init__(self, name: "The name of the character"='empty', 
                 pixelArt: "The name of the file for the pixel art of the character"='empty', 
                 fullArt: "The name of the file for the full art of the character (optional)"=None, 
                 stats: "Stats of the character defined as a tuple (HP, STAMINA, MAG, STR, DEX)"=(0, 0, 0, 0, 0)):
        self._registry.append(self)
        self.character_pix = pygame.image.load(os.path.join(GameConfig.game_path, pixelArt)) #Loads the pixel art of the character for the renderer
        self.character_pix = self.character_pix.convert()
        self.pixart_size = self.character_pix.get_size()
        if (fullArt != None):
            self.character_full_pic = pygame.image.load(os.path.join(GameConfig.game_path, fullArt)) #Loads the optional full art of the character for the renderer
            self.character_full_pic = self.character_full_pic.convert()
        self.character_name = name #Sets the name of the character
        #Retrieves the character stats from the tuple that passes the values from the function call and assigns them to variables
        self.character_strength = stats[3]
        self.character_magic = stats[2]
        self.character_stamina = stats[1]
        self.character_dexterity = stats[4]
        self.character_heatlh = stats[0]
        self.character_position = (0, 0)
        self.frames_since_dodge = 0
    #Method to return the converted pixel art for rendering
    def renderCharacterPix(self):
        return self.character_pix
    #Method to return the converted full art for rendering
    def renderCharacterFull(self):
        return self.character_full_pic
    def getCharacterPosition(self) -> tuple:
        return self.character_position
    def setCharacterPosition(self, xpos, ypos):
        self.character_position = (xpos, ypos)
    def modCharacterPosition(self, xpos, ypos):
        self.character_position = (self.character_position[0] + xpos, self.character_position[1] + ypos)
    def getPixartSize(self):
        return self.pixart_size
    def getFramesSinceDodge(self):
        return self.frames_since_dodge
    def setFramesSinceDodge(self, intToSet):
        self.frames_since_dodge = intToSet
    def incrementFramesSinceDodge(self):
        self.frames_since_dodge = self.frames_since_dodge + 1
    def getCharacterName(self):
        return self.character_name
    def __del__(self):
        self._registry.remove(self)
    #Methods to change the stats of a character
    

        
