import gameCharacter, GameConfig, level, CharacterList

def startHomeLevel():
    home_level = level.Level('bdopic.png', (1000, 1000))
    home_level.addCharacter(CharacterList.getGameCharacter('Elinera'))