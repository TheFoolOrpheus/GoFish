#Python GoFish Deck

import random
import Card

def __init__(self):
    self.__Deck = []
    #TODO: Delete
    #suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
    #ranks = ["", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    for r in ranks:
        for s in suits:
            self.__Deck.append([r,s])

    random.shuffle(self.__Deck)

def Draw(self):
    draw = self.__Deck[0]
    self.__Deck.pop(0)
    return draw

def getNumCards(self):
    return len(self.__Deck)

def Shuffle(self):
    random.shuffle(self.__Deck)

def __str__(self):
    num = 0
    deckString = ''
    while num < len(self.__Deck):
        seeDeck += self.__Deck[num] + '\n'
        num += 1
    return deckString
