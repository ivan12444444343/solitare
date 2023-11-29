import random

def make_card(rank,suit):
    name_suffix = ''
    if rank == 11:
        name_suffix = 'Jack'
    elif rank == 12:
        name_suffix = 'Queeen'
    elif rank ==13:
        name_suffix = 'King'
    elif rank== 14:
        name_suffix = 'Ace'
    else:
        name_suffix = str(rank)
    name= name_suffix + " of " + suit
    shortHand = name_suffix[0]+ suit[0] 
    if suit == "Spades" or suit == "Clubs":
        shortHand = "\033[34m"+ shortHand +"\033[37m"
    if suit == "Diamonds" or suit == "Hearts":
        shortHand = "\033[31m"+ shortHand +"\033[37m"
    return (rank, suit, name, shortHand)


def make_deck():
    deck = []
    suits = ["Hearts","Diamonds","Clubs","Spades"]
    for suit in suits:
        for rank in range(2,15):
            deck.append(make_card(rank, suit))
    return deck
    
def shuffle(deck):
    for i in range(len(deck)):
        j = random.randrange(len(deck)) # len(deck) == 52 exclusive so it will be 51
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp
    return deck

def draw(deck,hand): #a_hand is a list
    if deck == []:
        return None
    else: 
        card_drawn = deck.pop()
        hand.append(card_drawn)
        return card_drawn

def deal_one_hand(deck,number_of_cards):
    hand = []
    for _ in range(number_of_cards):
        draw(deck, hand)
    return hand

def main():
    deck = make_deck()
    print(shuffle(deck))
if __name__=="__main__":
    main()