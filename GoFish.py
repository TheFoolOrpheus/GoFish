#Python GoFish Main

import Deck
import Card

def __init__(self):

    self.userHand = []
    self.cpuHand = []
    self.__Status = 'No turns have been taken'
    self.__Info = ''
    self.__Request = ''


def setStatus(self, index):
    STATUS = [ 'No turns have been taken',\
               'You drew.',\
               'The computer drew.',\
               'Your turn.',\
               'Computer\'s Turn.'
               ]
    self.__Status = STATUS[index]

def getStatus(self):
    return self.__Status

def setInfo(self, index):
    INFO = ['You win!',\
            'Computer Wins!',\
            'The deck is empty.'
            ]

    self.__Info

def getInfo(self):
    return self.__Info

def setRequest(self, rank):
    self.__Request = ('The computer asked for your ' + rank + 's.')

def getRequest(self):
    return self.__Request

def startGame(self):
    self.userHand = []
    self.cpuHand = []
    self.deck = Deck()
    self.deck.shuffleDeck()
