#!/usr/bin/env python
# coding: utf-8

# In[2]:


from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':0}

class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        self.dealer = False
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
        
class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def shuffleDeck(self):
        shuffle(self.deck)
    
    def remove_one(self):
        return self.deck.pop()
    
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.state = 'playing'
        
        if name == 'dealer':
            self.balance = 0
            self.dealer = True
        else:
            self.dealer = False
            self.balance = 10

    def hitOrStay(self):  
        while True:
            response = input("Hit or Stay? ")
            if response == 'hit' or response == 'Hit':
                self.state = 'hit'
                break
            elif response == 'stay' or response == 'Stay':
                self.state = 'stay'
                break
            else:
                print("invalid response")
    
    def addCard(self, card):
        self.cards.append(card)
        
    def aceVal(self):
        aceValue = 0
        for card in self.cards:
            if card.rank == 'Ace':
                while aceValue != 11 and aceValue != 1:
                    try:
                        aceValue = int(input(f"{self.name}: Ace 1 or 11? "))
                    except:
                        print("Ace has to be either 1 or 11")
            break
                
        for card in self.cards:
            if card.rank == 'Ace':
                card.value = aceValue
        
    def bet(self):
        while True:
            try:
                self.bettingAmount = int(input("Enter betting amount: "))
            except:
                print("the betting amount has to be a number")
            else:
                break

    def __str__(self):
        if len(self.cards) == 2:
            if self.dealer:
                return f"{self.name} has {self.cards[0]}"
            else:
                return f"{self.name} has {self.cards[0]} and {self.cards[1]}"  
        else:
            sentence = f'{self.name} has '
            for card in self.cards:
                sentence += str(card)+ ", "
            return sentence


# In[4]:


my_deck = Deck()
my_deck.shuffleDeck()

human = Player("Watvki")
human.addCard(my_deck.remove_one())
human.addCard(my_deck.remove_one())

dealer = Player("dealer")
dealer.addCard(my_deck.remove_one())
dealer.addCard(my_deck.remove_one())

### Game Logic ###

game_on = True
while game_on:
    print(f'{dealer} and a down facing card')
    print(human)
    human.hitOrStay()
    while human.state == 'hit':
        human.addCard(my_deck.remove_one())
        print(human)
        humanTotal = 0
        human.aceVal()
        for card in human.cards:
            humanTotal += card.value
        if humanTotal > 21:
            human.state = 'BUST'
            break
        human.hitOrStay()
        if human.state == 'stay':
            break
        
                
    if human.state == 'BUST':
        print(f"{human.name} busted, dealer wins")
        game_on = False
        break
    else:
        print(dealer)
        dealer.aceVal()
        dealerTotal = 0
        for card in dealer.cards:
            dealerTotal += card.value
                
        while dealerTotal < 17:
            dealer.addCard(my_deck.remove_one())
            print(dealer)
            dealerTotal = 0
            dealer.aceVal()
            for card in dealer.cards:
                dealerTotal += card.value
                
        if dealerTotal > 21:
            print(dealer)
            dealer.state = 'BUST'
            print(f"{dealer.name} busted, {human.name} wins")
            break
        elif dealerTotal > humanTotal:
            if len(dealer.cards) == 2:
                print(f'{dealer} and {dealer.cards[1]}')
            else:
                print(dealer)
            print(human)
            print(f'{dealerTotal} > {humanTotal}\nDealer Wins!')
            game_on = False
            break
        elif dealerTotal < humanTotal:
            if len(dealer.cards) == 2:
                print(f'{dealer} and {dealer.cards[1]}')
            else:
                print(dealer)
            print(human)
            print(f'{dealerTotal} > {humanTotal}\n{human.name} Wins!')
            game_on = False
            break
        else:
            print("TIE!")


# In[ ]:





# In[ ]:




