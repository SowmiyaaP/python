import random
from turtle import clear
def dealcard():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calscore(cards):
            if sum(cards) == 21 and len(cards)==2:
                return 0
            if sum(cards)>21 and 11 in cards:
                cards.remove(11)
                cards.append(1)
            return sum(cards)

def compare(user_score,comp_score):
            if user_score == comp_score:
                return "Draw"
            elif comp_score == 0:
                return "You Lose!!"
            elif user_score == 0:
                return "You Win!!"
            elif user_score>21:
                return "You Lose!! You went over 21!!"
            elif comp_score>21:
                return "You Win!! Your opponent went over 21!!"
            elif user_score>comp_score:
                return "You Win!!"
            else:
                return "You Lose!!"

def playgame():   
    user = []
    computer = []
    gameover = False
    for _ in range(2):
        user.append(dealcard())
        computer.append(dealcard())

    while not gameover:
        
    
        user_score = calscore(user)
        comp_score = calscore(computer)
        print(f"   Your cards: {user}, current score: {user_score}")
        print(f"   Computer's first card: {computer[0]}")

        if user_score == 0 or comp_score == 0 or user_score>21:
            gameover = True
        else:
            chance= input("Type 'y' to get another card and type 'n' to pass:")
            if chance == 'y':
                user.append(dealcard())
            else:
                gameover = True    

    while comp_score != 0 and comp_score <17:
        computer.append(dealcard())
        comp_score  = calscore(computer)
    print(f"Your final score:{user_score}")
    print(f"Computer's final score:{comp_score}")
    print(compare(user_score,comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    playgame()
