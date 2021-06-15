import random
import time

def get_input():
    hit_or_pass = str(input("> "))
    hit_or_pass = hit_or_pass.lower()
    
    return hit_or_pass


def shuffle_deck():
    cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    random.shuffle(cards)

    return cards


def ask_player():
    print("Hit or pass?")

    while True:

        hit_or_pass = get_input()

        if hit_or_pass == "hit" or hit_or_pass == "pass":
            return hit_or_pass

        else:
            print("Not an option. Type hit or pass!")

    
def card_values(cards):

    if 1 in cards:

        print("You have drawn an ace!")
        print("Do you want it to equal 1 or equal 11, your choice!")
        one_or_eleven = int(input("> "))

        if one_or_eleven == 11:
            return one_or_eleven


def draw_ace(card):
    print("You have drawn an ace!")

    while True:

        one_or_eleven = int(input("Do you want the ace to equal one or eleven? > "))

        if one_or_eleven == 1 or one_or_eleven == 11:

            if one_or_eleven == 11:
                card = 11
                
            elif one_or_eleven == 1:
                card = 1

            return card

        else:
            print("Please type either one or eleven!")


def dealer_draws_ace(card, hand):
    dealer_sum = get_sum(hand)

    if dealer_sum < 11:
        card = 11

    else:
        card = 1
    
    return card


def deal_cards(cards, iterations, hand, which_player):
    for i in range(len(cards)):

        card = (cards[i])
        cards.pop(i)
        
        iterations = iterations + 1

        if which_player == "user" and card == 1:
            card = draw_ace(card)

        elif which_player == "dealer" and card == 1:
            card = dealer_draws_ace(card, hand)
            
        hand.append(card)
        
        if iterations == 2:
            break

    return cards, hand
            

def get_sum(total_cards):
    sum_of_hand = sum(total_cards)

    return sum_of_hand


def dealer_draw_or_pass(dealers_cards):
    sum_of_hand = get_sum(dealers_cards)

    if sum_of_hand > 16:
        choice = ("pass")

    if sum_of_hand <= 16:
        choice = ("hit")

    return choice


def hit_or_pass_funcs(dealers_cards):
    players_choice = ask_player()
    dealers_choice = dealer_draw_or_pass(dealers_cards)

    return players_choice, dealers_choice


def play_again():
    print("Play again?")
    print("[y/n]")

    while True:
        y_or_n = get_input()

        if y_or_n == "y" or y_or_n == "n":
            return y_or_n
        else:
            print("Please answer y or n!")


def exit_app():
    exit(0)


def main():
    
    while True:

        print("Welcome to blackjack.")
        time.sleep(1)
        print("The dealer is drawing. Get ready")
        time.sleep(1)
        cards = shuffle_deck()
        hand = []
        iterations = 0
        which_player = ("user")
        cards, players_cards = deal_cards(cards, iterations, hand, which_player)
        

        which_player = ("dealer")
        hand = []
        cards, dealers_cards = deal_cards(cards, iterations, hand, which_player)

        players_choice = ("hit")
        
        while True:

            iterations = 1
            player_sum = get_sum(players_cards)
            dealer_sum = get_sum(dealers_cards)
            print(f"Your cards are {players_cards}")
            print(f"The sum of your cards are {player_sum}")
            
            
            if player_sum > 21 or dealer_sum > 21:

                print(f"Your sum is {player_sum}")
                time.sleep(2)
                print(f"The dealers sum is {dealer_sum}")


                if player_sum > 21 and dealer_sum > 21:
                    if player_sum > dealer_sum:
                        print("You lose!")

                    elif player_sum < dealer_sum:
                        print("You win!")
                    
                    elif player_sum == dealer_sum:
                        print("Draw!")
                    break


                elif player_sum > 21:
                    print("You lose!")

                elif dealer_sum > 21:
                    print("You win!")
                break
            
            if players_choice == "hit":
                players_choice, dealers_choice = hit_or_pass_funcs(dealers_cards)

            if players_choice == "hit" or dealers_choice == "hit":
               
                if players_choice == "hit":
                    which_player = ("user")
                    cards, players_cards = deal_cards(cards, iterations, players_cards, which_player)

                if dealers_choice == "hit":
                    which_player = ("dealer")
                    cards, dealers_cards = deal_cards(cards, iterations, dealers_cards, which_player)

                time.sleep(2)
                print("The dealer has drawn!")

            elif players_choice == "pass" and dealers_choice == "pass":

                print(f"Your sum is {player_sum}")
                time.sleep(2)
                print(f"The dealers sum is {dealer_sum}")

                if player_sum > 21:
                    print("You lose!")

                elif dealer_sum > 21:
                    print("You win!")

                elif player_sum and dealer_sum <= 21:

                    if player_sum > dealer_sum:
                        print("You win!")
                    
                    elif player_sum < dealer_sum:
                        print("You lose!")
                    
                    elif player_sum == dealer_sum:
                        print("Tie!")

                break
        
        y_or_n = play_again()

        if y_or_n == "y":
            continue

        if y_or_n == "n":
            exit_app()
        
                  
main()
