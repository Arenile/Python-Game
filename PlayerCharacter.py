import pygame, os, gameCharacter, level, GameConfig

def movement(game_character: gameCharacter.gameCharacter, current_level: level.Level,current_display_size: "Size of current window as tuple" ,move_speed = 1, dodge_distance = 40): 

    keys = pygame.key.get_pressed()
    #Moves up when the 'w' key is pressed and the character is in the middle of the screen
    if keys[pygame.K_w]:
        if ((game_character.getCharacterPosition()[1] > 0) and ((game_character.getCharacterPosition()[1] >= current_display_size[1]/3) or (current_level.getLevelPosition()[1] >= 0))):
            game_character.modCharacterPosition(0, -move_speed)
            if (game_character.getCharacterPosition()[1] < 0):
                game_character.setCharacterPosition(ypos=0)
    #Moves left when the 'a' key is pressed and the character is in the middle of the screen
    if keys[pygame.K_a]:
        if ((game_character.getCharacterPosition()[0] > 0) and ((game_character.getCharacterPosition()[0] >= current_display_size[0]/3) or (current_level.getLevelPosition()[0] >= 0))):
            game_character.modCharacterPosition(-move_speed, 0)
            if (game_character.getCharacterPosition()[0] < 0):
                game_character.setCharacterPosition(0, game_character.getCharacterPosition()[1])
    #Moves down when the 's' key is pressed and the character is in the middle of the screen
    if keys[pygame.K_s]:
        if ((game_character.getCharacterPosition()[1] + game_character.getPixartSize()[1] < current_display_size[1]) and (((game_character.getCharacterPosition()[1]+game_character.getPixartSize()[1]) <= current_display_size[1]*(2/3)) or ((current_level.getLevelPosition()[1] + current_level.getLevelSize()[1]) <= current_display_size[1]))):
            game_character.modCharacterPosition(0, move_speed)
            if (game_character.getCharacterPosition()[1] + game_character.getPixartSize()[1] > current_display_size[1]):
                game_character.setCharacterPosition(game_character.getCharacterPosition()[0], (current_display_size[1] - game_character.getPixartSize()[1]))
    #Moves right when the 'd' key is pressed and the character is in the middle of the screen
    if keys[pygame.K_d]:
        if ((game_character.getCharacterPosition()[0] + game_character.getPixartSize()[0] < current_display_size[0]) and (((game_character.getCharacterPosition()[0]+game_character.getPixartSize()[0]) <= current_display_size[0]*(2/3)) or ((current_level.getLevelPosition()[0] + current_level.getLevelSize()[0]) <= current_display_size[0]))):
            game_character.modCharacterPosition(move_speed, 0)
            if (game_character.getCharacterPosition()[0] + game_character.getPixartSize()[0] > current_display_size[0]):
                game_character.setCharacterPosition(((current_display_size[0] - game_character.getPixartSize()[0]), game_character.getCharacterPosition()[1]))
    #Dodges upwards when the 'w' key and 'space' are pressed together when the character is in the middle of the screen
    if (keys[pygame.K_w] and keys[pygame.K_SPACE] and (game_character.getFramesSinceDodge() > GameConfig.FPS) and ((game_character.getCharacterPosition()[1] >= current_display_size[1]/3) or (current_level.getLevelPosition()[1] >= 0))):
        if (game_character.getCharacterPosition()[1] > 0):
            game_character.modCharacterPosition(0, -dodge_distance)
            game_character.setFramesSinceDodge(0)
            if (game_character.getCharacterPosition()[1] < 0):
                game_character.setCharacterPosition(game_character.getCharacterPosition()[0], 0)
    #Dodges leftwards when the 'a' key and 'space' are pressed together when the character is in the middle of the screen
    if (keys[pygame.K_a] and keys[pygame.K_SPACE] and (game_character.getFramesSinceDodge() > GameConfig.FPS) and ((game_character.getCharacterPosition()[0] >= current_display_size[0]/3) or (current_level.getLevelPosition()[0] >= 0))):
        if (game_character.getCharacterPosition()[0] > 0):
            game_character.modCharacterPosition(-dodge_distance, 0)
            game_character.setFramesSinceDodge(0)
            if (game_character.getCharacterPosition()[0] < 0):
                game_character.setCharacterPosition(0, game_character.getCharacterPosition()[1])
    #Dodges downwards when the 's' key and 'space' are pressed together when the character is in the middle of the screen
    if (keys[pygame.K_s] and keys[pygame.K_SPACE] and (game_character.getFramesSinceDodge() > GameConfig.FPS) and (((current_level.getLevelPosition()[1] + current_level.getLevelSize()[1]) <= current_display_size[1]) or ((game_character.getCharacterPosition()[1] + game_character.getPixartSize()[1]) <= current_display_size[1]*(2/3)))):
        if ((game_character.getCharacterPosition()[1] + game_character.getPixartSize()[1]) < current_display_size[1]):
            game_character.modCharacterPosition(0, dodge_distance)
            game_character.setFramesSinceDodge(0)
    #Dodges rightwards when the 'd' key and 'space' are pressed together when the character is in the middle of the screen
    if (keys[pygame.K_d] and keys[pygame.K_SPACE] and (game_character.getFramesSinceDodge() > GameConfig.FPS) and (((current_level.getLevelPosition()[0] + current_level.getLevelSize()[0]) <= current_display_size[0]) or ((game_character.getCharacterPosition()[0] + game_character.getPixartSize()[0]) <= current_display_size[0]*(2/3)))):
        if ((game_character.getCharacterPosition()[0] + game_character.getPixartSize()[0]) < current_display_size[0]):
            game_character.modCharacterPosition(dodge_distance, 0)
            game_character.setFramesSinceDodge(0)
    #Moves the display upwards relative to the level to follow the character when the character approaches the edge of the screen when 'w' is pressed       
    if (keys[pygame.K_w] and (game_character.getCharacterPosition()[1] < current_display_size[1]/3) and (current_level.getLevelPosition()[1] < 0)):
        current_level.modLevelPosition(0, move_speed)
    #Moves the display leftwards relative to the level to follow the character when the character approaches the edge of the screen when 'a' is pressed
    if (keys[pygame.K_a] and (game_character.getCharacterPosition()[0] < current_display_size[0]/3) and (current_level.getLevelPosition()[0] < 0)):
        current_level.modLevelPosition(move_speed, 0)
    #Moves the display downwards relative to the level to follow the character when the character approaches the edge of the screen when 's' is pressed
    if (keys[pygame.K_s] and ((game_character.getCharacterPosition()[1]+game_character.getPixartSize()[1]) > current_display_size[1]*(2/3)) and ((current_level.getLevelPosition()[1] + current_level.getLevelSize()[1]) > current_display_size[1])):
        current_level.modLevelPosition(0, -move_speed)
    #Moves the display rightwards relative to the level to follow the character when the character approaches the edge of the screen when 'd' is pressed
    if (keys[pygame.K_d] and ((game_character.getCharacterPosition()[0]+game_character.getPixartSize()[0]) > current_display_size[0]*(2/3)) and ((current_level.getLevelPosition()[0] + current_level.getLevelSize()[0]) > current_display_size[0])):
        current_level.modLevelPosition(-move_speed, 0)
    #Moves the display upwards relative to the level to follow the character when the character dodges towards the edge of the screen when 'w' is pressed
    if (keys[pygame.K_w] and keys[pygame.K_SPACE] and (game_character.getFramesSinceDodge() > GameConfig.FPS) and (game_character.getCharacterPosition()[1] < current_display_size[1]/3) and (current_level.getLevelPosition()[1] < 0)):
        if (game_character.getCharacterPosition()[1] > 0):
            current_level.modLevelPosition(0, dodge_distance)
            game_character.setFramesSinceDodge(0)
            if (game_character.getCharacterPosition()[1] < 0):
                game_character.setCharacterPosition(game_character.getCharacterPosition()[0], 0)
    #Moves the display leftwards relative to the level to follow the character when the character dodges towards the edge of the screen when 'a' is pressed
    if (keys[pygame.K_a] and keys[pygame.K_SPACE] and (game_character.getFramesSinceDodge() > GameConfig.FPS) and (game_character.getCharacterPosition()[0] < current_display_size[0]/3) and (current_level.getLevelPosition()[0] < 0)):
        if (game_character.getCharacterPosition()[0] > 0):
            current_level.modLevelPosition(dodge_distance, 0)
            game_character.setFramesSinceDodge(0)
            if (game_character.getCharacterPosition()[0] < 0):
                game_character.setCharacterPosition(0, game_character.getCharacterPosition()[1])
    #Moves the display downwards relative to the level to follow the character when the character dodges towards the edge of the screen when 's' is pressed
    if (keys[pygame.K_s] and keys[pygame.K_SPACE] and (game_character.getFramesSinceDodge() > GameConfig.FPS) and ((game_character.getCharacterPosition()[1] + game_character.getPixartSize()[1]) > current_display_size[1]*(2/3)) and ((current_level.getLevelPosition()[1] + current_level.getLevelSize()[1]) > current_display_size[1])):
        if (game_character.getCharacterPosition()[1] + game_character.getPixartSize()[1] < current_display_size[1]):
            current_level.modLevelPosition(0, -dodge_distance)
            game_character.setFramesSinceDodge(0)
            if (game_character.getCharacterPosition()[1] + game_character.getPixartSize()[1] > current_display_size[1]):
                game_character.setCharacterPosition(game_character.getCharacterPosition()[0], (current_display_size[1] - game_character.getPixartSize()[1]))
    #Moves the display rightwards relative to the level to follow the character when the character dodges towards the edge of the screen when 'd' is pressed
    if (keys[pygame.K_d] and keys[pygame.K_SPACE] and (game_character.getFramesSinceDodge() > GameConfig.FPS) and ((game_character.getCharacterPosition()[0] + game_character.getPixartSize()[0]) > current_display_size[0]*(2/3)) and ((current_level.getLevelPosition()[0] + current_level.getLevelSize()[0]) > current_display_size[0])):
        if (game_character.getCharacterPosition()[1] + game_character.getPixartSize()[1] < current_display_size[1]):
            current_level.modLevelPosition(-dodge_distance, 0)
            game_character.setFramesSinceDodge(0)
            if (game_character.getCharacterPosition()[0] + game_character.getPixartSize()[0] > current_display_size[0]):
                game_character.setCharacterPosition((current_display_size[0] - game_character.getCharacterPosition()[0]), (game_character.getPixartSize()[1]))
    #The following 4 if-statements check for the level not being lined up with the edge of the screen when at the edge of the level and fix that issue if it arises
    if (current_level.getLevelPosition()[0] + current_level.getLevelSize()[0] < current_display_size[0]):
        current_level.setLevelPosition((current_display_size[0] - current_level.getLevelSize()[0], current_level.getLevelPosition()[1]))
    if (current_level.getLevelPosition()[1] + current_level.getLevelSize()[1] < current_display_size[1]):
        current_level.setLevelPosition((current_level.getLevelPosition()[0], current_display_size[1] - current_level.getLevelSize()[1]))
    if (current_level.getLevelPosition()[0] > 0):
        current_level.setLevelPosition((0, current_level.getLevelPosition()[1]))
    if (current_level.getLevelPosition()[1] > 0):
        current_level.setLevelPosition((current_level.getLevelPosition()[0], 0))
    game_character.incrementFramesSinceDodge()