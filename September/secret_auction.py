# Prompt the user to input their name
# Prompt the user to input their bid starting with $
# Prompt the user to respond if anyone else is bidding
# After everyone is in declare the winner


def silent_auction():
    print('Welcome to the Silent Auction!')
    players_bids = {}
    keep_adding_players = True
    while keep_adding_players:
        new_username = input('Please, input your name:\n')
        new_bid = int(input('Please, input your bid:\n$'))
        players_bids[new_username] = new_bid

        user_choice = input('Add another player? "yes" or "no"?:\n').lower()
        if user_choice == 'no':
            keep_adding_players = False

    highest_bid = max(players_bids.values())
    winners = [k for k, v in players_bids.items() if v == highest_bid]
    print(f'The winner is {winners[0]} with whopping bid of ${highest_bid}!')
    

silent_auction()
