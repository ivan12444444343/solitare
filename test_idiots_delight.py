import idiots_delight
import cards
def test_deal_hand():
    expected = 2
    hand= idiots_delight.deal_hand()
    actual = len(hand)
    assert actual == expected

def test_discard():
    hand = [cards.make_card(2, "Clubs"),cards.make_card(3, "Diamonds"),cards.make_card(4,"Hearts"),cards.make_card(5,"Spades"),cards.make_card(6,"Clubs"),cards.make_card(7,"Diamonds")]
    count = 4
    expected = hand[:-4]
    actual = idiots_delight.discard(hand,count)
    assert expected == actual