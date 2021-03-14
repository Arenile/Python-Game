import gameCharacter, GameConfig, level, CharacterList

def startHomeLevel():
    home_level = level.Level('placeholder-background.jpg', (1000, 1000))
    home_level.addCharacter(CharacterList.getGameCharacter('Elinera'))