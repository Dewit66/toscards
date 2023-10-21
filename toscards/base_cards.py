import random
import os
 
 
suits = ["clubs","spades","hearts","diamonds"]
values = ["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]
 
 
class Card:
   # Gives the card class suits and value
   def __init__(self,suit,value):
       self.suit = suit
       self.value = value
  
   # Allows instances of cards to be printed in a readiable format
   def to_string(self):
       return self.suit + "_" + self.value
  
   # Same as to_string, but with only the first char of the suit and is used for testing games
   def to_short_string(self):
       return (self.suit[0]).capitalize() + " " + (self.value[0]).capitalize()
  
 
 
 
class Deck:
 
   # Gives Deck color and whether it is an empty deck or not, if it isn't populates the deck.
   # It also sets the color of the deck and the list cards as its properties
   def __init__(self,color,empty):
       self.color = color
       self.cards = []
       if not empty:
           for i in suits:
               for j in values:
                   self.cards.append(Card(i,j))
           random.shuffle(self.cards)
 
   # Class method that uses reverse boolean logic to return if the deck is empty or not
   def is_empty(self) -> bool:
       if self.cards:
           return False
       else:
           return True
 
   # Class method that allows for the drawing of the first card instance from the list cards, by poping the 0th index of the list     
   def draw(self):
       return self.cards.pop(0)
  
   # Passes in a card instance
   # Class method that allows for a card instance to be put in the 0th or first position of the list cards
   def put(self,card):
       self.cards.insert(0,card)
  
   # TODO put comment
   def get_cards(self):
       return self.cards
    
   # Passes in a deck instance
   # Class method that allows for
   def append(self,deck,shuffle):
       self.cards.extend(deck.get_cards())
       if shuffle == True: # meant for games that go faster when cards are shuffled
            random.shuffle(self.cards) #
  
   # TODO put comment
   def size(self):
       return len(self.cards)
    
    # TODO write a print function for Deck
    
  
 
class Player:
 
   # TODO put comment
   def __init__(self,id,deck):
       self.id = id
       self.deck = deck
  
   # TODO put comment
   def draw(self):
       return self.deck.draw()
 
   # TODO put comment
   def append(self,deck : type[Deck],fast):
       self.deck.append(deck,fast)
  
   # TODO put comment
   def has_cards(self):
       return not self.deck.is_empty()
 
   # TODO put comment 
   def deck_size(self):
       return self.deck.size()
