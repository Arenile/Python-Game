import pygame, windowRender, GameConfig, gameCharacter, os

class Level:

    _registry = []
    def __init__(self, level_art: "Filename of image to initialize the renderer with for the level as a string",
                 rel_pos: "Position of the level relative to the screen (optional)"=(0,0)):
        self._registry.append(self)
        self.level_image = pygame.image.load(os.path.join(GameConfig.game_path, level_art))
        self.level_image = self.level_image.convert()
        self.level_size = self.level_image.get_size()
        self.level_position = rel_pos

    def renderLevel(self): #Returns the level art for rendering
        return self.level_image
    
    def getLevelSize(self): #Returns the size of the level as a tuple
        return self.level_size

    def getLevelPosition(self): #Returns the position of the level relative to the screen
        return self.level_position
    
    def setLevelPosition(self, position: tuple): #Sets the level position relative to the screen
        self.level_position = position
    
    def modLevelPosition(self, xposmod, yposmod): #Modifies the level position by defined amount relative to the screen
        self.level_position = (self.level_position[0] + xposmod, self.level_position[1] + yposmod)
    
    def __del__(self):
        self._registry.remove(self)