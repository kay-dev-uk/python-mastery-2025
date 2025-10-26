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
    
    def define_winner(user, bot):
        if user > 21:
            return "Bust! You lost!"
        elif user == 0 and bot == 0 or user == bot:
            return "It's a draw!"
        elif user == 0 or user > bot:
            return "You won!"
    
    keep_playing = True
    while keep_playing:
        user_cards = []
        computer_cards = []
        is_game_over = False

        for n in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        while is_game_over == False:
            user_choice = input("Type 'y' to hit, type 'n' to pass:\n").lower()

            if user_choice == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"Your score: {user_score}, your cards: {user_cards}. Computer's cards: {computer_cards[0]}")
                if calculate_score(user_cards) == 0:
                    print("You won!")
                    is_game_over = True
                elif calculate_score(user_cards) > 21:
                    print("Bust! You lost!")
                    is_game_over = True

            else:
                while computer_score < 17 and computer_score > 0:
                    computer_cards.append(deal_card())
                    print(f"Computer drew a card, now computer cards are: {computer_cards}")
                    computer_score = calculate_score(computer_cards)
                print(f"Your score: {user_score}, your cards: {user_cards}. Computer's cards: {computer_cards} computer's score {computer_score}")
                print(define_winner(calculate_score(user_cards), calculate_score(computer_cards)))
                is_game_over = True
        play_again = input("Type 'y' to play again or 'n' to stop:\n").lower()
        if play_again == "y":
            continue
        else:
            keep_playing = False

blackjack()
