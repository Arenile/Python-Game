import pygame, os, gameCharacter, GameConfig

class RenderWindow:
    def __init__(self, size: "The size of the window, given as a tuple (w,h)"=(640,480),
                 background: "Optional parameter to set the background of a window to an image"=None, 
                 backgroundColor: "Optional parameter to set the background of a window to a color of the form (R, G, B)"=(0,0,0)):
        self.screen = pygame.display.set_mode(size)
        if (background != None):
            self.screenBackground = pygame.image.load(os.path.join(GameConfig.game_path, background))
        else:
            self.screenBackground = pygame.Surface(self.screen.get_size())
            self.screenBackground.fill(backgroundColor)
        self.to_render = [[self.screenBackground],[0],[0]] #List of objects that will get rendered by the renderer
        self.window_size = size

    #Make a function that adds objects to the list for the renderer to render
    def addToRenderer(self, thing_to_render: "Object to add to the renderer", xpos, ypos):
        self.to_render[0].append(thing_to_render)
        self.to_render[1].append(xpos)
        self.to_render[2].append(ypos)

    #Make a function that actually renders the objects in the "to_render list"
    #This should work like a queue, in that the first object added gets rendered first and
    #as objects get rendered they are removed from the queue
    def render(self):
        for i in range(len(self.to_render[0])):
            self.screen.blit(self.to_render[0][i], (self.to_render[1][i], self.to_render[2][i]))
        self.to_render[0].clear()   #SUPER IMPORTANT
        self.to_render[1].clear()   #CLEARS THE RENDERER
        self.to_render[2].clear()   #LAGS LIKE HELL IF THESE THREE STATEMENTS AREN'T THERE

    def getScreenBackground(self):
        return self.screenBackground

    def getScreen(self):
        return self.screen

    def getWindowSize(self):
        return self.window_size