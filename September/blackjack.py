# Do you want to play y/n?
# Get 2 random cards
# Show computer first card
# Type y to get another card or n to pass
# show your final hand and computer final hand (apparently bot doesnt hit)
# print who wins
# start over
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random

def blackjack():


    user_cards = []
    computer_cards = []

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    for n in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(user_cards)
    print(computer_cards)

blackjack()
