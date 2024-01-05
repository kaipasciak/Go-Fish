# Go Fish Program
# Authors: Kai Pasciak, KJ McCrosson

import random
import time

# A shuffled deck is created before each game using a nested for statement
# as well as the random module's shuffle method.

DECK = []
suits = ('♦','♣','♥','♠')
for card in ('A','2','3','4','5','6','7','8','9','10','Jack','Queen','King'):
    for letter in suits:
        DECK.append(str(card) + letter)
random.shuffle(DECK)
user_pairs = 0
computer_pairs = 0

def deal_hands():
    ''' Distributes seven random cards for each the computer and the user to their
    hands. Returns two lists as a tuple. '''
    user_hand = []
    computer_hand = []
    new_user_pairs = 0
    new_computer_pairs = 0

    # for loops are used to remove items from deck and append to hands

    for i in range(1,8):
        user_hand.append(DECK.pop())
    for i in range(1,8):
        computer_hand.append(DECK.pop())
    time.sleep(1)
    print(f'Your hand is {user_hand}')
    time.sleep(1)
    print('\nLooking for matches...')

    # The next two for loops pair up any matches in dealt out hands at beginning of the game

    for i in user_hand:
        user_other_cards = []
        for y in user_hand:
            user_other_cards.append(y)
        user_other_cards.pop(user_other_cards.index(i))
        for x in user_other_cards:
            if i[0:-1] == x[0:-1]:
                user_hand.pop(user_hand.index(i))
                user_hand.pop(user_hand.index(x))
                new_user_pairs += 1
                break

    for i in computer_hand:
        computer_other_cards = []
        for y in computer_hand:
            computer_other_cards.append(y)
        computer_other_cards.pop(computer_other_cards.index(i))
        for x in computer_other_cards:
            if i[0:-1] == x[0:-1]:
                computer_hand.pop(computer_hand.index(i))
                computer_hand.pop(computer_hand.index(x))
                new_computer_pairs += 1
                break

    return (user_hand, computer_hand, new_user_pairs, new_computer_pairs)

def go_fish(hand):
    ''' Chooses a card from the deck and pops the dictionary item '''
    new_pairs = 0
    new_card = DECK.pop()
    for i in hand:
        if new_card[0:-1] == i[0:-1]:
            hand.pop(hand.index(i))
            new_pairs = 1
    if new_pairs == 0:
        hand.append(new_card)

    return (hand, new_pairs)

def end_turn_user(request, user_hand, computer_hand):
    ''' Adds to the accumulator and displays the number of pairs the user has '''

    # For loop checks if the requested card is in the computer's hand

    user_new_pairs = 0
    for i in computer_hand:
        if request == i[0:-1]:
            computer_hand.pop(computer_hand.index(i))
            for x in user_hand:
                if request == x[0:-1]:
                    time.sleep(1)
                    print('Card found in computer\'s hand!')
                    user_hand.pop(user_hand.index(x))
            user_new_pairs += 1
            break

    # If is used for if no matches were found in computer's hand, calling Go Fish function

    if user_new_pairs == 0:
        time.sleep(1)
        print('Go Fish!')
        fish = go_fish(user_hand)
        user_hand = fish[0]
        user_new_pairs +=  fish[1]
    return (user_new_pairs, user_hand, computer_hand)


def end_turn_computer(request, computer_hand, user_hand):
    ''' Adds to an accumulator and displays the number of pairs the computer has '''

    # Contains same code as previous function with variables switched out for computer

    computer_new_pairs = 0
    for i in user_hand:
        if request == i[0:-1]:
            user_hand.pop(user_hand.index(i))
            for x in computer_hand:
                if request == x[0:-1]:
                    time.sleep(1)
                    print('Card found in your hand!')
                    computer_hand.pop(computer_hand.index(x))
                    time.sleep(1)
                    print(f'Your hand is now {user_hand}')
            computer_new_pairs += 1
            break

    if computer_new_pairs == 0:
        time.sleep(1)
        print('Go Fish!')
        fish = go_fish(computer_hand)
        computer_hand = fish[0]
        computer_new_pairs +=  fish[1]
    return (computer_new_pairs, computer_hand, user_hand)

def main():

    ''' Calls the deal_hand function. An if statement will determine
    if either player still has cards left in their hand. If not, the game ends and
    the player who runs out of cards first wins. '''

    # First group of statements automatically displays message and deals cards

    print('Welcome to Go Fish!')
    time.sleep(1)
    print('\nDealing Hands...')
    user_pairs = 0
    computer_pairs = 0
    hands = deal_hands()
    user_hand = hands[0]
    computer_hand = hands[1]
    user_pairs += hands[2]
    computer_pairs += hands[3]
    time.sleep(1)
    print(f'Your hand is now {user_hand}')
    time.sleep(1)
    print(f'\nYou have {user_pairs} pairs')
    time.sleep(1)
    print(f'The computer has {len(computer_hand)} cards left and has {computer_pairs} pairs')

    # While loop checks if either hand or the deck is empty before proceeding with turn

    while len(user_hand) != 0 and len(computer_hand) != 0 and DECK != 0:
        time.sleep(2)
        request = str(input('What card would you like to ask for? '))
        in_hand = False

        while in_hand == False:
            for i in user_hand:
                if request == i[0:-1]:
                    in_hand = True
                    time.sleep(1)
                    break
            if in_hand == False:
                time.sleep(0.5)
                request = str(input('Card not in hand. What card would you like to ask for?'))

        # Functions return tuples whose items either replace variables or are added to accumulators

        user_end = end_turn_user(request, user_hand, computer_hand)
        user_pairs += user_end[0]
        user_hand = user_end[1]
        computer_hand = user_end[2]
        time.sleep(1)
        print(f'\nYou have {user_pairs} pairs')
        time.sleep(1)
        print(f'Your hand: \n{user_hand}')

        if len(user_hand) == 0 or len(computer_hand) == 0 or len(DECK) == 0:
            break

        request = computer_hand[random.randint(0,len(computer_hand)-1)][0:-1]
        time.sleep(1)
        print(f'\nComputer\'s Guess: {request}')

        computer_end = end_turn_computer(request, computer_hand, user_hand)

        computer_pairs += computer_end[0]
        computer_hand = computer_end[1]
        user_hand = computer_end[2]
        time.sleep(1)
        print(f'\nComputer has {computer_pairs} pairs')
        time.sleep(1)
        print(f'Computer has {len(computer_hand)} cards left')


    if computer_pairs > user_pairs:
        print(f'Computer wins with {computer_pairs} pairs!')
    elif user_pairs > computer_pairs:
        print(f'User wins with {user_pairs} pairs!')
    else:
        print(f'Tie!')

main()
