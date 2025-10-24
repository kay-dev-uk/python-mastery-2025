# Do you want to play y/n?
# Get 2 random cards
# Show computer first card
# Type y to get another card or n to pass
# show your final hand and computer final hand (apparently bot doesnt hit)
# print who wins
# start over

import random

def blackjack():
    # Main func
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)
    # Main func
    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0 
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)
    

    
    keep_playing = True
    while keep_playing:
        user_cards = []
        computer_cards = []
        is_game_over = False
        # First time dealing the cards
        for n in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())


        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}, ")

    user_choice = input("Type 'y' to hit, type 'n' to pass:\n").lower()
    if user_choice == 'y':
        user_cards.append(deal_card())
    else:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards}, current score: {computer_score}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

    
        


blackjack()
