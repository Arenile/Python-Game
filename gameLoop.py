import pygame, os, gameCharacter, windowRender, PlayerCharacter, GameConfig, level, LevelList, CharacterList

pygame.init()

mainWindow = windowRender.RenderWindow(GameConfig.main_window_size, backgroundColor=(255,255,255))
CharacterList.loadCharacterList()

playtime = 0
mainloop = True

#bdopic = level.Level('bdopic.png', (-2000, -2000))
#bdopic.addCharacter(elinera)
LevelList.startHomeLevel()
player_character = CharacterList.getGameCharacter('Elinera')

while mainloop:
    mainWindow.addToRenderer(mainWindow.getScreenBackground(), 0, 0)
    for levels in level.Level._registry: #Iterates through all level instances for rendering
        mainWindow.addToRenderer(levels.renderLevel(), levels.getLevelPosition()[0], levels.getLevelPosition()[1])
        for characters in levels.getCharacterList():
            mainWindow.addToRenderer(characters.renderCharacterPix(), characters.getCharacterPosition()[0], characters.getCharacterPosition()[1])
            PlayerCharacter.movement(player_character, levels, mainWindow.getWindowSize(), 1)
    #for characters in gameCharacter.gameCharacter._registry: #Iterates through all character instances for rendering
    #    mainWindow.addToRenderer(characters.renderCharacterPix(), characters.getCharacterPosition()[0], characters.getCharacterPosition()[1])
    mainWindow.render()
    milliseconds = GameConfig.clock.tick(GameConfig.FPS)
    playtime += milliseconds / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
    pygame.display.flip()

pygame.quit()