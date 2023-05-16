import random
from replit import clear

def star_game():
    def calculate_score(cards):
        if sum(cards) == 21 and len(2):
            return 0
    
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
    
    
    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "It a Draw"
        elif computer_score == 0:
            return "Lose, opponnent has a BlackJack"
        elif user_score == 0:
            return "You Win"
        elif computer_score > 21:
            return "Computer went over"
        elif user_score > 21:
            return "You went over"
        elif computer_score > user_score:
            return "User wins"
        else:
            return "Computer wins"
    
    
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = int(random.choice(cards))
        return card
    
    
    user_cards = []
    computer_cards = []
    is_gamer_over = False
    #total = user_cards1 + user_cards2
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_gamer_over:
    
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"You card is {user_cards} your total score is {user_score}")
        print(f"Computer first card is {computer_cards[0]}")
    
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_gamer_over = True
        else:
            dealer_should_deal = input(
                "Type 'y' to get anoter card, type 'n' to pass ")
            if dealer_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_gamer_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"Your cards {user_cards} and final score {user_score}")
    print(f"Computer cards {computer_cards} and score {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a BlackJack? ") == "y":
  star_game()
