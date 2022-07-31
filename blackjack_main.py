import time 
import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards = [' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', ' J', ' Q', ' K', ' A']
full_deck = [f"{j} of {i}" for j in cards for i in suits]*4
deck_of_cards = full_deck[:]

def to_float(string):
    price = string
    is_float = False
    while is_float == False:
        try:
            float(price)
            return float(price)
        except ValueError:
            price = input("Invalid response. Please enter a number.").strip('$ ')

# classes

class Dealer:
    
    def __init__(self, name='Dealer'):
        self.name = name
        self.hand = []

    def __str__(self):
        return "This is the dealer."

    def show_hidden_hand(self, hand):
        print(f"Dealer's hand:")
        if hand.hand[1][0][0] == '1':                     
            y = hand.hand[1][0][0:2]
        else:
            y = hand.hand[1][0][0:2]

        for i in range(1):
            print(f' ______\t'+f' ______\t')
            print(f'|# # # |'+f'|{y}    |')
            print(f'| # # #|'+f'|      |')
            print(f'|# # # |'+f'|      |')
            print(f'|_#_#_#|'+f'|____{y}|\n')
        
    def reveal_hand(self, hand):
        print(f"{self.name}'s hand:")         
        a = hand.hand[0][0][0:2]
        b = hand.hand[1][0][0:2]
 
        if len(hand.hand) == 2:                      # [[' 4 of hearts'], [' 7 of hearts']]
            for i in range(1):                       # hand.hand[i][0][0:2]
                print(f' ______\t'*len(hand.hand))
                print(f'|{a}    |'+f'|{b}    |')
                print(f'|      |'*len(hand.hand))
                print(f'|      |'*len(hand.hand))
                print(f'|____{a}|'+f'|____{b}|\n')
        elif len(hand.hand) == 3:
            c = hand.hand[2][0][0:2]
            for i in range(1):
                print(f' ______\t'*len(hand.hand))
                print(f'|{a}    |'+f'|{b}    |'+f'|{c}    |')
                print(f'|      |'*len(hand.hand))
                print(f'|      |'*len(hand.hand))
                print(f'|____{a}|'+f'|____{b}|'+f'|____{c}|\n')
        elif len(hand.hand) == 4:
            c = hand.hand[2][0][0:2]
            d = hand.hand[3][0][0:2]
            for i in range(1):
                print(f' ______\t'*len(hand.hand))
                print(f'|{a}    |'+f'|{b}    |'+f'|{c}    |'+f'|{d}    |')
                print(f'|      |'*len(hand.hand))
                print(f'|      |'*len(hand.hand))
                print(f'|____{a}|'+f'|____{b}|'+f'|____{c}|'+f'|____{d}|\n')
        elif len(hand.hand) == 5:
            c = hand.hand[2][0][0:2]
            d = hand.hand[3][0][0:2]
            e = hand.hand[4][0][0:2]
            for i in range(1):
                print(f' ______\t'*len(hand.hand))
                print(f'|{a}    |'+f'|{b}    |'+f'|{c}    |'+f'|{d}    |'+f'|{e}    |')
                print(f'|      |'*len(hand.hand))
                print(f'|      |'*len(hand.hand))
                print(f'|____{a}|'+f'|____{b}|'+f'|____{c}|'+f'|____{d}|'+f'|____{e}|\n')
        elif len(hand.hand) == 6:
            c = hand.hand[2][0][0:2]
            d = hand.hand[3][0][0:2]
            e = hand.hand[4][0][0:2]
            f = hand.hand[5][0][0:2]
            for i in range(1):
                print(f' ______\t'*len(hand.hand))
                print(f'|{a}    |'+f'|{b}    |'+f'|{c}    |'+f'|{d}    |'+f'|{e}    |'+f'|{f}    |')
                print(f'|      |'*len(hand.hand))
                print(f'|      |'*len(hand.hand))
                print(f'|____{a}|'+f'|____{b}|'+f'|____{c}|'+f'|____{d}|'+f'|____{e}|'+f'|____{f}|\n')
        
    def show_points(self, hand):
        points = 0
        for i in hand:
            if i[0][1] in ('J', 'Q', 'K', '0'):
                points += 10
            elif i[0][1] == 'A':
                points += 11
            else:
                points += int(i[0][1])
        if points <= 21:
            print(f'{self.name} has {points} points')
            return points
        elif points > 21:
            for i in hand:
                if i[0][1] == 'A':
                    points -= 10
                    if points <= 21:
                        print(f"{self.name} has {points} points")
                        return points
                        break
                    else:
                        continue
            else:
                print(f"{self.name} has {points} points")
                return points

class Player(Dealer):
    
    def __init__(self, name, money_in_pocket):
        self.name = name
        self.money_in_pocket = money_in_pocket
        self.hand = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Player: {self.name}"

    def place_bet(self):
        self.bet = input('Place your bet: ')
        float_bet = to_float(self.bet)
        while float_bet > self.money_in_pocket:
            self.bet = input("You don't have that much money in your pocket! Place a different bet: ")
            float_bet = to_float(self.bet)
        return float_bet

class Hand:

    def __init__(self):
        self.hand = []

    def __str__(self):
        if self.hand == []:
            return "This hand is empty!"
        return f"This hand contains the {self.hand[0][0]} and the {self.hand[1][0]}."

    def __repr(self):
        return f"<Cards | {self.hand[0][0]} {self.hand[1][0]}>"

    def create_hand(self):                                                  # deals two cards
        self.hand.append(random.choices(deck_of_cards, k=1))
        deck_of_cards.remove(self.hand[-1][0])                              # deletes each one from deck_of_cards
        self.hand.append(random.choices(deck_of_cards, k=1))
        deck_of_cards.remove(self.hand[-1][0])
        return self.hand

    def hit(self):
        self.hand.append(random.choices(deck_of_cards, k=1))
        deck_of_cards.remove(self.hand[-1][0])
        print(self.hand)
        return self.hand

# main function to run game

def play_blackjack():
    ask = input('Hi there! Can I interest you in a game of Blackjack? y/n ').lower()
    if ask == 'n':
        print('Suit yourself! ...hehe... Get it?')
    while ask not in ('y', 'n'):
        ask = input('Invalid response. Please enter y or n. ')
    if ask == 'y':
        player_name = input('To start, what is your name? ').title()
        player_money = input('How much money are you starting off with? ')
        total_money = to_float(player_money)                                            # converting input to float using to_float method
        if total_money == 0:
            print("You have no money? Sorry, but you can't play. Come back when you have something to bet.")
            return  
        dealer = Dealer()                                                               # creating instance of Dealer
        player1 = Player(player_name, total_money)                                      # creating instance of Player
        again = 'y'
        while again == 'y':
            global deck_of_cards
            if len(deck_of_cards) < 25:
                deck_of_cards = full_deck[:]
            player1.money_in_pocket = total_money
            print("Let's play!")
            time.sleep(1)
            print(f"You have ${total_money:.2f}.")                      # change float_money to money they had at end of last game
            if total_money == 0:
                print("Oh. Seems like you lost all your money. Come back when you get some more!")
                return
            bet = player1.place_bet()
            total_money -= bet
            print("Dealing...")
            time.sleep(2)
            player_hand = Hand()
            player_hand.create_hand()
            dealer_hand = Hand()
            dealer_hand.create_hand()
            player1.reveal_hand(player_hand)
            dealer.show_hidden_hand(dealer_hand)
            player_points = player1.show_points(player_hand.hand)
            if player_points == 21:
                print(f'BLACKJACK!! Your winnings: ${bet*1.5:.2f}')
                total_money += (bet + bet*1.5)
            else:
                print(f"Dealer's visible card: {dealer_hand.hand[1][0]}")
                decision = input('Do you want to hit or stand? h/s ')
                while decision not in ('h', 's'):
                    decision = input('Invalid response. Please enter h for hit or s for stand. ')
                while decision == 'h':
                    player_hand.hit()
                    player1.reveal_hand(player_hand)
                    player_points = player1.show_points(player_hand.hand)
                    if player_points == 21:
                        print(f'You won! Your winnings: ${bet:.2f}')
                        total_money += bet*2
                        break
                    elif player_points > 21:
                        print('You BUSTED. Better luck next time!')
                        break
                    else:
                        print(f"Dealer's visible card: {dealer_hand.hand[1][0]}")
                        decision = input('Another hit? h/s ')
                        while decision not in ('h', 's'):
                            decision = input('Invalid response. Please enter h for hit or s for stand. ')
                else:
                    # if stand 
                    # winner is determined
                    # show dealers cards
                    if player_points >= 21:
                        continue
                    else: 
                        dealer.reveal_hand(dealer_hand)
                        dealer_points = dealer.show_points(dealer_hand.hand)
                        while dealer_points < 17:
                            print("Dealer hits")
                            dealer_hand.hit()
                            dealer.reveal_hand(dealer_hand)
                            dealer_points = dealer.show_points(dealer_hand.hand)
                            time.sleep(1)
                        if 17 <= dealer_points <= 21:
                            if dealer_points > player_points:
                                player1.show_points(player_hand.hand)
                                print('Dealer wins!')
                            elif dealer_points == player_points:
                                player1.show_points(player_hand.hand)
                                print("It's a tie. Nobody wins this one.")
                            else:
                                player1.show_points(player_hand.hand)
                                print('You win!')
                                print(f"Your winnings: ${bet:.2f}")
                                total_money += bet*2
                        else:
                            player1.show_points(player_hand.hand)
                            print('Dealer BUSTED. You win!')
                            print(f"Your winnings: ${bet:.2f}")
                            total_money += bet*2
            again = input('Would you like to play again? y/n ')
            while again not in ('y', 'n'):
                again = input('Invalid response. Please enter y or n. ')
            if again == 'n':
                print('Thanks for playing!')

play_blackjack()