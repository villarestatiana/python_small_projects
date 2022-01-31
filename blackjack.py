#Lista com as cartas:
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#The last three "10" cards represent "J", "Q", "K".
#"The "11" card represent 'A'

def generate_first_hand_cards():
    """"return a list with two random cards."""
    hand = []
    card_1 = random.choice(cards)
    card_2 = random.choice(cards)    
    hand.append(card_1)
    hand.append(card_2)
    return hand

def calculate_points(hands):
    """Calculate the sum of the cards in hand list """
    score = sum(hands)

    if score == 21 and len(hands) == 2:
        return "blackjack" 
    if score > 21 and 11 in hands:
        hands.remove(11)
        hands.append(1) 
        score = sum(hands)
    return score

    

def winner(user_score, computer_score):
    if user_score == "blackjack":
        user_score = 21

    if user_score > 21:
        print(f"You lose")
    elif computer_score > 21:
        print("You win")
    elif user_score > computer_score:
        print("You win")
    elif user_score == computer_score:
        print("It's a draw.")
    else:
        print("You lose")

def get_new_card():
    new_card = random.choice(cards)   
    return new_card

play_game = 'y' 
while play_game == 'y':
    play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    if play_game == 'y':
        user_hand = generate_first_hand_cards()
        computer_hand = generate_first_hand_cards()
        user_hand = [11, 9]
        while calculate_points(computer_hand) < 17:
            computer_hand.append(get_new_card())
        score = calculate_points(user_hand)
        print(f"Your hand is {user_hand} - your current score is: {score} ")
        #print(computer_hand)
        print(f"The computer hand is {computer_hand[0]}")
        ask_card = "y"
        if str(calculate_points(user_hand)) == "blackjack":
            ask_card = "n"
        lose = False
        while ask_card == 'y':
            ask_card = input("Type 'y' to get another card, type 'n' to pass: " )
            if ask_card == 'y':
                user_hand.append(get_new_card())
                score = calculate_points(user_hand)
                print(f"your hand is {user_hand} - {score} points")
                if calculate_points(user_hand) > 21:
                    print("You lose.")
                    lose = True
                    ask_card = "n"

        if not lose:
            user_score = calculate_points(user_hand)   
            computer_score = calculate_points(computer_hand)   
            print(f"Your final hand: {user_hand}, final score: {user_score}")
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            winner(user_score, computer_score)

