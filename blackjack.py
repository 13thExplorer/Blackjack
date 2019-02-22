import random
#Sets one of four suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
#sets a rank for the cards
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#dict lookup passing the rank to get a num value
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card(): #represents a single card
    def __init__(self,suit,rank):
        self.suit = suit #represents cards suit
        self.rank = rank #represents a cards ranks/value

    def __str__(self):
        return self.rank + ' of ' + self.suit
class Deck():
    def __init__(self):
        self.deck = [] #starts with an empty list
        for suit in suits: #nested for loop that takes Each suit value
            for rank in ranks: #and returns a rank for that value
                self.deck.append(Card(suit,rank)) #4x13 gives us our 52 card deck

    def __str__(self):
        deck_comp = '' 'sets the deck to an empty string'
        for card in self.deck: #for loop each card in the deck
            deck_comp += '\n' + card.__str__() #returns string representation of the card
        return 'The deck has: '+deck_comp #Prints out a list of the deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop() #Pops of the last card in the random deck
        return single_card #
class Hand():
    """Represents cards in players hand"""
    def __init__(self):
        self.cards = [] #Start with an empty list like the deck
        self.value =  0 #start with zero value
        self.aces = 0 #tracking aces
    def add_card(self,card):
        #card passed in from Deck.deal -->Single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank] 
        if card.rank == 'Ace':
            self.aces += values[card.rank]

    def adjust_for_ace(self):
        #Determines if the aces is an 11 or a 1
        #if total value > 21 and i still have an ace then change
        #my ace to a 1 instead of a 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -=1 #
class Chips():
    def __init__(self, total=100):
        self.total = total
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet #
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?'))
        except: 
            print('Sorry please provide an integer')
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! You have: {}'.format(chips.total))
            else:
                break
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
def hit_or_stand(deck,hand):
    global playing #to control an upcoming while loop
    while True: 
        x = input('Hit or Stand. Enter h or s') #Hit or hh #stand
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('Player Stands -> Dealers Turn')
            playing = False
        else:
            print('Invalid input, please input "s" or "h" only!')
            continue
        break
def player_bust(player,dealer, chips):
    print('Player busted')
    chips.lose_bet() #subtracts winnings to total chips
def player_wins(player,dealer,chips):
    print('Player has won!')
    chips.win_bet() #Adds winnings to total chips
def dealer_bust(player,dealer,chips):
    print('Player has won! The dealer busted!')
    chips.win_bet() #Adds winnings to total chips
def dealer_wins(player,dealer,chips):
    print('The dealer has won.')
    chips.lose_bet()
def push(player,dealer):
    print('Dealer and player tie! Push.')

while True:
    #print an opening
    print('Welcome to Blackjack')
    #create and shuffle deck. deal 2 cards to each player
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #set player chips
    player_chips = Chips()
    #promt player for their bet
    take_bet(player_chips)
    #showcards(but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    while playing: #recall this variable from hit_or_stand function
        #prompt for player to hit or stand
        hit_or_stand(deck,player_hand)
        #show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        #if players hand exceeds 21, run player_bust() and break loop
        if player_hand.value > 21:
            player_bust(player_hand,dealer_hand,player_chips)
            break
        #if player hasn't busted, play dealers hand until dealer hits 17
        if player_hand <= 21:
            while  dealer_hand.value < 17:
                hit(deck,dealer_hand)
            #show all cards
            show_all(player_hand, dealer_hand)
            #run different winning scenarios
            if dealer_hand.value > 21:
                dealer_bust(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)
        #Show Current Chip Value
        print('\n Player total chips are at: {}'.format(player_chips.total))
        new_game = input('Would you like to play again? y/n')
        if new_game[0].lower == 'y':
            playing = True
            continue
        else:
            print('Thank you for playing.')






























test_deck = Deck()
test_deck.shuffle()
#Player 
test_player = Hand()
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)
        
test_player.add_card(test_deck.deal())


