#Python GoFish Card

import random

def __init__(self):
    self.__Rank = rank
    self.__Suit = suit
    self.__faceUp = True
    #Image for the card's back and front at some point when I make a GUI
    #self.__Image = ''

def getSuit(self):
    return self.__Suit

def getRank(self):
    return self.__Rank

def rankName(self, card):
    ranks = ["", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    num = card.getRank()
    return ranks[num]

def suitName(self, card):
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
    num = card.getSuit()
    return suits[num]

def flipCard(self):
    self.__faceUp = not self.__faceUp

def faceUp(self):
    return self.__faceUp

#The image for the back of the card
def cardBack(self):
    self.__Image= ''

#The image for the front of the card
def cardFront(self):
    self.__Image= ''

def getImage(self):
    return self.__Image

def __str__(self):
    #return a string of the card
