import random

def draw_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
    return random.choice(cards)

def calculate_hand(hand):
    total = 0
    aces = 0
    for card in hand:
        if card == 'Ace':
            aces += 1
        elif isinstance(card, int):
            total += card
        else:
            total += 10
    for i in range(aces):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
    return total

def play_game():
    print('Welcome to Blackjack!')
    print('You will start with two cards.')
    dealer_hand = [draw_card(), draw_card()]
    player_hand = [draw_card(), draw_card()]
    print(f"The dealer's face-up card is {dealer_hand[0]}.")
    print(f"Your hand is {player_hand} with a total of {calculate_hand(player_hand)}")
    while True:
        choice = input('Do you want to hit or stand? ').lower()
        if choice == 'hit':
            player_hand.append(draw_card())
            print(f'Your new card is {player_hand[-1]}.')
            total = calculate_hand(player_hand)
            if total > 21:
                print(f'You busted with a total of {total}! Dealer wins.')
                return
            print(f'Your hand now has a total of {total}.')
        elif choice == 'stand':
            player_total = calculate_hand(player_hand)
            dealer_total = calculate_hand(dealer_hand)
            print(f"The dealer's hand is {dealer_hand} with a total of {dealer_total}")
            while dealer_total < 17:
                dealer_hand.append(draw_card())
                dealer_total = calculate_hand(dealer_hand)
                print(f"The dealer drew {dealer_hand[-1]} for a new total of {dealer_total}")
            if dealer_total > 21:
                print(f"The dealer busted with a total of {dealer_total}! You win.")
            elif dealer_total > player_total:
                print(f"The dealer wins with a total of {dealer_total}.")
            elif dealer_total < player_total:
                print(f"You win with a total of {player_total}!")
            else:
                print(f"It's a tie with a total of {player_total}.")
            return
while True:
    play_game()
