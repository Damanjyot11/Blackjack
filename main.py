from replit import clear
import art
import random

def result(player_cards,computer_cards):
    print(f"Your final hand : {player_cards}, final score : {sum(player_cards)}")
    print(f"Computer's final hand : {computer_cards}, final score : {sum(computer_cards)}")

def current_score(player_cards,computer_cards):
    print(f"Your cards : {player_cards}, current score : {sum(player_cards)}")
    print(f"Computer's first card : {computer_cards}")

def Blackjack():
    clear()
    print(art.logo)

    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    player_cards = []
    computer_cards = []

    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

    player_score = player_cards[0] + player_cards[1]
    computer_score = computer_cards[0]

    current_score(player_cards,computer_cards)

    while True:
        choice = input("Type 'y' to get another card, type 'n' to pass : ").lower()
        flag = False

        if choice == "n":
            while computer_score < 17:
                card = random.choice(cards)
                computer_cards.append(card)
                computer_score += card

                if computer_score >= 17 and computer_score <= 21:
                   break; 
                elif computer_score > 21 :
                    for i in range(len(computer_cards)):
                        if computer_cards[i] == 11:
                            computer_cards[i] = 1
                            computer_score -= 10
                            break

            result(player_cards,computer_cards)
            if computer_score > 21:
                print("You Win !!")
            elif player_score > computer_score:
                print("You Win !!")
            elif player_score < computer_score:
                print("You Lose !!")
            else:
                print("Draw !!")
            break
        else:
            card = random.choice(cards)
            player_cards.append(card)
            player_score += card

            if player_score <= 21:
                current_score(player_cards,computer_cards)
                continue;
            else:
                for i in range(len(player_cards)):
                    if player_cards[i] == 11:
                        flag = True
                        player_cards[i] = 1
                        player_score -= 10
                        break

                if flag == True:
                    current_score(player_cards,computer_cards)
                    continue

                while computer_score < 17:
                    card = random.choice(cards)
                    computer_cards.append(card)
                    computer_score += card
                    if computer_score > 21:
                        for i in range(len(computer_cards)):
                            if computer_cards[i] == 11:
                                computer_cards[i] = 1
                                computer_score -= 10
                                break

                result(player_cards,computer_cards)
                print("You went over. You lose")
                break

    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower()
    if choice == 'n':
        return
    else:
        Blackjack()

Blackjack()