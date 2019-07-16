from deckofcards import FrenchDeckOfCards
from player import Player

playing = True

def make_bet(player_chips):

    while True:
        print(f'you have {player_chips} chips.')
        try:
            bet_value = int(input("How many chips would you like to bet? "))
        except ValueError:
            print('Please enter an integer.')
        else:
            if bet_value > player_chips:
                print('You cannot bet more than', player_chips, 'chips.')
            else:
                break
    return bet_value


def show_cards():
    print('Dealer is showing an: ')
    print(f'{dealer.hand[0]} \n')
    print("Player's Cards: ", *player1.hand, sep='\n')


def hit_or_stand():
    global playing

    while True:
        hitorstand = input('Would you like to hit(h) or stand(s)? ')

        if hitorstand[0].lower() == 'h':
            player1.addtohand(deck.deal())
            show_cards()
            add_cards(player1)
        elif hitorstand[0].lower() == 's':
            print('Player stands. Dealer is playing.')
            playing = False
        else:
            print('Please try again.')
            continue
        break

def add_cards(player):
    values = {'2':2,
              '3':3,
              '4':4,
              '5':5,
              '6':6,
              '7':7,
              '8':8,
              '9':9,
              '10':10,
              'J':10,
              'Q':10,
              'K':10,
              'A':11}

    cards = [player.hand[i].rank for i in range(len(player.hand))]
    for card in cards:
        player.handvalue += values[card]


while True:
    print('Welcome to blackjack! Try and beat the dealer by getting to 21 without going over!')

    deck = FrenchDeckOfCards()
    deck.shuffle()

    player1 = Player()
    dealer = Player()
    player1.addtohand(deck.deal())
    dealer.addtohand(deck.deal())
    player1.addtohand(deck.deal())
    dealer.addtohand(deck.deal())
    
    bet = make_bet(player1.chips)
    show_cards()

    while playing:
        add_cards(player1)
        add_cards(dealer)
        hit_or_stand()
        if player1.handvalue > 21:
            player1.losechips(losses=bet)
            print(player1.chips)
            print("player busts!")
            break
    break


