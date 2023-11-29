import cards

def test_make_deck():
    deck = cards.make_deck()
    print(deck)
    assert deck[0] == (2, 'Hearts', '2 of Hearts', '\x1b[31m2H\x1b[37m')
    assert(deck[13] == (2, 'Diamonds', '2 of Diamonds', '\x1b[31m2D\x1b[37m'))
    assert(deck[26] == (2, 'Clubs', '2 of Clubs', '\x1b[34m2C\x1b[37m'))
    assert(deck[39] == (2, 'Spades', '2 of Spades', '\x1b[34m2S\x1b[37m'))

def test_deal_one_hand():
    deck=cards.make_deck()
    number_of_cards = 5
    hand = cards.deal_one_hand(deck, number_of_cards)
    assert len(hand) == number_of_cards