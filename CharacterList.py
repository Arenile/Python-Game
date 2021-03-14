import gameCharacter, GameConfig, os, pygame

def loadCharacterList():
    elinera = gameCharacter.gameCharacter('Elinera', 'placeholder-sprite.png', stats=(10, 10, 10, 10, 10))

def getGameCharacter(characterToGet: "Name of the character to get as a string"):
    for characters in gameCharacter.gameCharacter._registry:
        if (characters.getCharacterName() == characterToGet):
            return characters
    return None
