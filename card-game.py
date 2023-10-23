import random
ranks = ['Ace' ,'Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
suits = ['Hearts','Clubs','Spades','Diamonds']
points = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,
          'King':10, 'Ace':[1,11]}    

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
class Deck():
      
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                mycard = Card(suit,rank)
                self.all_cards.append(mycard)
    
    def __str__(self):
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n' + card.__str__()            
        return deck_comp
                
    def Shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()
    

def gameon_choice():
    
    choice = ' '
    
    while choice.upper() not in ['Y','N']:
        choice = (input('Replay? (Y/N) ')).upper()
        
        if choice not in ['Y','N']:
            print('Sorry please enter (Y/N).')
        
    if choice == 'Y':
        return True
    else:
        print('💕 Thank you for playing! 💕')
        return False    
    
class Player():
    
    def __init__(self,bank):
        self.all_cards = []
        self.bank = bank
        self.score = 0
        
    def in_hand(self):
        mycard = new_deck.deal_one()
        self.all_cards.append(mycard)
    
    def add_value(self):
        
        card = self.all_cards[-1]
        if type(points[card.rank]) == type([]):
            ace_value = 0
            
            while ace_value not in [1,11]:
                
                ace_value = input('Enter the value for ace: ')
                if ace_value.isdigit() == False: 
                    print('Please enter a proper value. ')
                elif int(ace_value) not in [1,11]:
                    print('Please enter 1 or 11')
                else:   
                    ace_value = int(ace_value)
                    self.score += ace_value
        else:
            self.score += points[card.rank]
                
        return self.score           
    
    def check_balance(self,bet,bank):
        if not bet.isdigit():
            print('Please enter a number. ')
            return False
        elif int(bet) == 0:
            print('Bet amount cannot be zero!')
        elif  abs(int(bet)) <= bank:
            return True
        else:
            print('Bet is greater than available bank balance.')
            return False
        
class Dealer():
        
    def __init__(self):
        self.all_cards = []
        self.score = 0
        
    def in_hand(self):
        mycard = new_deck.deal_one()
        self.all_cards.append(mycard)
        
    def add_value(self):
        
        card = self.all_cards[-1]
        if type(points[card.rank]) == type([]):
            ace_value = 0
            if self.score + 11 > 21:
                ace_value = 1
            else:
                ace_value = 11
            self.score += ace_value

        else:
            self.score += points[card.rank]
                
        return self.score
    
gameon = True
print('WELCOME TO BLACKJACK!')
bank = 1000

while gameon:
    new_deck = Deck()
    new_deck.Shuffle()
    player = Player(bank)
    dealer = Dealer()
    gameover = 'a'
    print(f'\nCurrent bank balance: {bank}')
    while True:
        bet = input('\nDear Player, place the bet: ')
        if player.check_balance(bet,bank):
            break
    bank -= int(bet)
    print(f'\nCurrent bank balance: {bank}')
    print('\nPlayer\'s cards are: ')
    for num in range(2):            
        player.in_hand()
        print(player.all_cards[num])
        player.add_value()
    print(f'Player\'s points: {player.score}')

    for num in range(2):   
        dealer.in_hand()
        dealer.add_value()
    print('\nDealer\'s first card is: ')
    print(dealer.all_cards[0])
    if type(points[dealer.all_cards[0].rank]) == type([]):
        first_card = 11
    else:
        first_card = points[dealer.all_cards[0].rank]
    print(f'Points for Dealer\'s first card: {first_card}')
    
    while True:

        if player.score > 21:
            print('PLAYER BUSTS! DEALER WINS!')
            gameover = 'yes'
            gameon = gameon_choice()
            break

        elif player.score == 21:
            print('\nBLACKJACK FOR PLAYER!')
            break

        else:
            player_choice = input('\nDear Player, Hit or Stand? ')

            if player_choice.upper() == 'HIT':
                player.in_hand()
                print(player.all_cards[-1])
                player.add_value()
                print(f'Player\'s points: {player.score}')


            elif player_choice.upper() == 'STAND':
                print(f'\nDealer\'s second card: \n{dealer.all_cards[-1]}')
                print(f'Dealer\'s points: {dealer.score}') 
                break

            else:
                print('Please enter \'Hit\' or \'Stand\'')

    while True:
        
        if gameover=='yes':
            break
        
        elif dealer.score > 21:
            print('\nDEALER BUSTS! PLAYER WINS!')
            bank += int(bet)
            gameon = gameon_choice()
            gameover='yes'
            break

        elif dealer.score == 21:
            print('\nBLACKJACK FOR DELAER!')
            break

        elif dealer.score <= 16:
            dealer.in_hand()
            dealer.add_value()
            print(dealer.all_cards[-1])
            print(f'Dealer\'s points: {dealer.score}')
            
        else:
            break

    if player.score == 21 and dealer.score == 21 or player.score == dealer.score:
        print('\nDRAW MATCH! Bet money has been returned')
        bank += int(bet)
        gameon = gameon_choice()
        gameover='yes'
        
    elif player.score <= 21 and dealer.score <= 21:
        if dealer.score > player.score:
            print('\nDealer wins! Player loses!'.upper())
        else:
            print('\nPlayer wins! Dealer loses!'.upper())
            bank += int(bet)
            
    if bank <= 0:
        if bank == 0:
            print('\nBank balance is zero!')
        else:
            print('\nPlayer in debt!')
        print('GAME OVER! ')
        gameon = False
        gameover='yes'
        
    if gameover!='yes':
        gameon = gameon_choice()
