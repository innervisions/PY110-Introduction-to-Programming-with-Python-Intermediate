import random

def prompt(message):
    print(f"=> {message}")

def create_deck():
    suits = ["♤", "♧", "♡", "♢"]
    ranks = [str(num) for num in range(2, 10)] + ["A", "J", "Q", "K"]
    deck = [[suit, rank] for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def total(cards):
    values = [card[1] for card in cards]

    sum_val = 0
    for value in values:
        if value == "A":
            sum_val += 11
        elif value in ["J", "Q", "K"]:
            sum_val += 10
        else:
            sum_val += int(value)

    # correct for Aces
    aces = values.count("A")
    while sum_val > 21 and aces:
        sum_val -= 10
        aces -= 1

    return sum_val

def busted(cards):
    return total(cards) > 21

def player_turn(deck, hand):
    while True:
        player_choice = input("Would you like to (h)it or (s)tay? ").casefold()
        if player_choice not in ['h', 's']:
            prompt("Sorry, must enter 'h' or 's'.")
            continue
        if player_choice == 'h':
            hand.append(deck.pop())
            prompt('You chose to hit!')
            prompt(f"Your cards are now: {hand(hand)}")
            prompt(f"Your total is now: {total(hand)}")

        if player_choice == 's' or busted(hand):
            break
        

def dealer_turn(deck, hand):



def play_hand():
    deck = create_deck()
    dealer_hand = [deck.pop() for _ in range(0, 2)]
    player_hand = [deck.pop() for _ in range(0, 2)]
    print(f"Dealer has {dealer_hand[0][1]}{dealer_hand[0][0]} and an unknown card.")
    print(
        f"You have {player_hand[0][1]}{player_hand[0][0]} and {player_hand[1][1]}{player_hand[1][0]}."
    )
    player_turn(deck, player_hand)
    dealer_turn(deck, dealer_hand)


def play_twentyone():
    while True:
        play_hand()
        while True:
            print("Play again? (y or n)")
            answer = input().lower()
            if answer in ["y", "n"]:
                break
            print("Please choose y or n.")
        if answer == "n":
            break


play_twentyone()
