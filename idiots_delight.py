import cards
def deal_hand():
	deck = cards.make_deck()
	cards.shuffle(deck)
	hand = cards.deal_one_hand(deck,4)
	return hand, deck

def discard(hand,n):
	if len(hand) < 4 or n not in [2,4]:
		return hand
	elif n == 4:
		hand = hand[:-4]
	elif n == 2:
		del hand [-2:-4:-1]
	return hand

def play_round(deck,hand_of_cards):

		while (len(hand_of_cards) < 4):
			cards.draw(deck,hand_of_cards)
		discard_bol = False
		while len(hand_of_cards)>=4:
			card1 = hand_of_cards[-4]
			card4 = hand_of_cards[-1]
			card2 = hand_of_cards[-2]
			card3 = hand_of_cards[-3]
			rank1 = card1[0]
			rank4 = card4[0]
			suit2 = card2[1]
			suit3 = card3[1]
			if rank1 == rank4:
				hand_of_cards = discard(hand_of_cards,4)
				discard_bol = True
			elif suit2 == suit3:
				hand_of_cards = discard(hand_of_cards,2)
				discard_bol = True
			if len(deck)>=1:
				cards.draw(deck,hand_of_cards)
			else:
				break
		return deck, hand_of_cards

def main():
	deal_hand()
	deck = cards.make_deck()
	hand, deck = deal_hand()
	print("Hand at the end of the round: ", end="")
	for card in hand:
		print(card[-1], end=" ")
	print()

	deck, hand = play_round(deck,hand)
	for card in hand:
		print(card[-1], end=" ")
	deck = cards.shuffle(deck)
	while len(deck)>0:
		deck, hand = play_round(deck,hand)
		print("Hand: ", end =" ")
		for card in hand:
			print(card[-1], end=" ")
		print()
	print("\nGame is over! You have", len(hand), "cards left in your hand.")
	print("Better luck next time!")
	if len(hand)==0:
		print("\nGame is over! You have 0 cards left in your hand.")
		print("You are a winner!")
	# print(hand)
	# print(play)
	# hand = deal_hand()
	# print("Hand dealt: ", hand)
	# x = deal_hand()
	# n = 2
	# print(discard(x,n))
if __name__ == "__main__":
	main()