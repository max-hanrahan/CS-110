'''
file: final_project.py
name: Max Hanrahan
date: 11/30/2019
decr: This is my implementation of lost cities.
The game involves objects such as cards, the deck (of cards), a player's hand 
of eight cards, the piles of cards (one for each 
player plus a discard pile), and a game class that controls and executes the 
rules.
'''

################################################################################
#note: this program will expect MANY files in the same directory upon completion
################################################################################

import random
from cs110graphics import *

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
BACKGROUND = 'maroon'

COLOR_DICT = {'red': 0, 'green': 1, 'blue': 2, 'white': 3, 'yellow': 4}
MAX_CARD_VALUE = 10 # ADJUST ME TO 2 FOR THE FASTEST POSSIBLE GAME

class Card:
    def __init__(self, window, color, value):
        '''Card objects need a value and a suit, and can be moved and rendered.'''
        self._color = color
        self._value = value # where value of 1 is a handshake
        self._window = window

        self._body = Image(self._window, self._color + str(self._value) + \
        ".png", 64 * WINDOW_WIDTH // 625, 4 * WINDOW_HEIGHT // 25, (0, 0)) 
        # This (0, 0) a placeholder position
    
    def __str__(self):
        return 'color: {} value: {}'.format(self._color, self._value)   

    def get_color(self):
        return self._color

    def get_value(self):
        return self._value

    def move_card(self, pos):
        self._body.move_to(pos)

    def hide_card(self):
        self._window.remove(self._body)

    def render_card(self, pos):
        self._body.move_to(pos)
        self._body.set_depth(0 - self._value)
        self._window.add(self._body)
        
class Deck():
    def __init__(self, window):
        ''' the deck we draw from'''
        self._contents = []
        self._window = window

        for color in ('blue', 'red', 'white', 'yellow', 'green'):
            for value in range(2, MAX_CARD_VALUE + 1):
                self._contents.append(Card(self._window, color, value))
        for color in ('blue', 'red', 'white', 'yellow', 'green'):
            for value in range(3):
                self._contents.append(Card(self._window, color, 1))

        # shuffle the cards
        random.shuffle(self._contents)

    def draw(self):
        return self._contents.pop()

    def get_length(self):
        return len(self._contents)

    def render_deck(self):
        downface = Image(self._window, "cardback.png", 
            64 * WINDOW_WIDTH // 625, 4 * WINDOW_HEIGHT // 25, 
            (WINDOW_WIDTH // 20, 3 * WINDOW_HEIGHT //10))
        downface.set_depth(0)
        self._window.add(downface)
        if len(self._contents) == 0:
            self._window.remove(downface)

class Hand():
    def __init__(self):
        '''each player has a hand of eight cards at any given time'''
        self._contents = []

    def remove_from_hand(self, index):
        return self._contents.pop(index)

    def get_card(self, index):
        return self._contents[index]
        # at some point we'll need to know the contents of the hand

    def render_hand(self):
        for i in range(len(self._contents)):
            self._contents[i].render_card(((i + 1) * WINDOW_WIDTH // 9, 
                9 * WINDOW_HEIGHT // 10))

    def hide_hand(self):
        for card in self._contents:
            card.hide_card()

    def add_to_hand(self, drawn_card):
        self._contents.append(drawn_card)

class Pile():
    def __init__(self):
        '''there are three piles: each player's tableau and the discard pile'''
        self._contents = [[], [], [], [], []]

    def place_card(self, placed_card, index):
        self._contents[index].append(placed_card)

    def calc_score(self):
        score = 0
        for exped in self._contents:
            handshakes = 0
            exped_score = 0
            bonus = 0

            if len(exped) == 0:
                exped_score = 0
            else:
                exped_score = -20
                for card in exped:
                    if card.get_value() == 1:
                        handshakes += 1
                    else:
                        exped_score += card.get_value()
            if len(exped) >= 8:
                bonus = 20
            score += exped_score * (handshakes + 1) + bonus
        return str(score)

    def get_card(self, window, index):
        if len(self._contents[index]) == 0:
            return Card(window, 'grey', 0)
        return self._contents[index][-1]

    def sub_pile_is_empty(self, index):
        if len(self._contents[index]) == 0:
            return True

class Discard_Pile(Pile):
    '''the only two attributes unique to a discard pile is the ability to remove
    cards and the fact that the cards must be reorderd acording to their order
    in the list (the other piles do not need to do this because they will always
    be played in order.)'''
    def remove_card(self, index):
        return self._contents[index].pop()

    def reorder(self):
        for sub_pile in self._contents:
            for card in sub_pile:
                card._body.set_depth(0 - sub_pile.index(card))

class TextZone:
    def __init__(self, window, deck):
        '''the upper region that displays what the player has to do, the scores, 
        the number of remaining cards, and whose turn it is anyway.'''
        self._window = window
        self._deck = deck

        self._instructions = ["Select a card from your hand by pressing a number 1 through 8.",
                              'Press "a" to place on tableau, or "b" to discard.',
                              'Press "c" to draw from deck, or "d" to draw from the discard.',
                              'Select a discard pile to draw from by pressing a number 1 through 5.']

        self._score_text = Text(self._window, "Player 1's score: 0\nPlayer 2's score: 0", 
            size = WINDOW_HEIGHT // 70, center = (WINDOW_WIDTH // 10, WINDOW_HEIGHT // 10))
        self._score_text.set_depth(0)
        self._window.add(self._score_text)

        self._turn_text = Text(self._window, "It is player 1's turn.", 
            size = WINDOW_HEIGHT // 70, center = (9 * WINDOW_WIDTH // 10, 
                WINDOW_HEIGHT // 10))
        self._turn_text.set_depth(0)
        self._window.add(self._turn_text)

        self._instruction_text = Text(self._window, self._instructions[0], 
            size = WINDOW_HEIGHT // 70, center = (WINDOW_WIDTH // 2, 
                WINDOW_HEIGHT // 10))
        self._instruction_text.set_depth(0)
        self._window.add(self._instruction_text)

        cards_in_deck = -1 + 5 * (MAX_CARD_VALUE - 1)

        self._deck_text = Text(self._window, 
            'There are {} cards left in the deck.'.format(cards_in_deck), 
            size = WINDOW_HEIGHT // 70, 
            center = (WINDOW_WIDTH // 2, 3 * WINDOW_HEIGHT // 20))
        self._deck_text.set_depth(0)
        self._window.add(self._deck_text)

    def update_scores(self, score_a, score_b):
        self._score_text.set_text("Player 1 score: " + str(score_a) + \
            "\nPlayer 2 score: " + str(score_b))

    def update_turn(self, turn_number):
        self._turn_text.set_text("It is player " + str(turn_number + 1) + "'s turn.")

    def update_instructions(self, stage_number):
        self._instruction_text.set_text(self._instructions[stage_number])

    def update_deck(self, value):
        self._deck_text.set_text('There are {} cards left in the deck.'.format(value))

class Banner(EventHandler):
    '''Banners show up above the text in the text zone to explain to the user
    what went wrong.'''
    def __init__(self, window, message):
        self._window = window
        self._banner = Text(window, message, 12, 
            (WINDOW_WIDTH // 2, WINDOW_HEIGHT //20))
        self._banner.set_depth(-10)
        self._dummy_img = Rectangle(self._window, WINDOW_HEIGHT, WINDOW_WIDTH, 
            (WINDOW_WIDTH // 2, WINDOW_HEIGHT //2))
        self._dummy_img.set_fill_color(BACKGROUND)

        self._dummy_img.add_handler(self)
        self._banner.add_handler(self)

        self._window.add(self._banner)
        self._window.add(self._dummy_img)

    def handle_mouse_press(self, event):
        self._window.remove(self._banner)
        self._window.remove(self._dummy_img)

class Game(EventHandler):
    def __init__(self, window):
        '''I need to make players hand, the board (the pile for each player plus
        the discard), the deck, and then (the hard part) a huge chunk of code 
        that takes user input and uses it to manipulate deck, piles, and hands.
        This manipulation will continue until some sort of end condition is met,
        upon which the winner is declared.
        '''
        self._window = window

        self._handler = Rectangle(self._window, 1, 1, (0, 0))
        self._handler.add_handler(self)
        self._handler.set_depth(100)
        self._window.add(self._handler)

        self._hands = [Hand(), Hand()]

        self._piles = [Pile(), Pile()]

        self._discard = Discard_Pile()

        self._deck = Deck(self._window)

        self._text_zone = TextZone(self._window, self._deck) 

        for _ in range(8):
            self._hands[0].add_to_hand(self._deck.draw())
            self._hands[1].add_to_hand(self._deck.draw())

        self._stage_number = 0
        self._turn = 0

        self._hands[0].render_hand()
        self._deck.render_deck()

    def end_game(self):
        celebration = Rectangle(self._window, WINDOW_WIDTH, 
            3 * WINDOW_HEIGHT // 5, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        celebration.set_fill_color(BACKGROUND)
        celebration.set_depth(-10)
        self._window.add(celebration)
        if int(self._piles[0].calc_score()) > int(self._piles[1].calc_score()):
            winner_text = Text(self._window, "Player 1 wins!", 24, 
                (WINDOW_HEIGHT //2, WINDOW_WIDTH //2))

        elif int(self._piles[0].calc_score()) < int(self._piles[1].calc_score()):
            winner_text = Text(self._window, "Player 2 wins!", 24, 
                (WINDOW_HEIGHT //2, WINDOW_WIDTH //2))
        else:
            winner_text = Text(self._window, "It's a tie.", 24, 
                (WINDOW_HEIGHT //2, WINDOW_WIDTH //2))
        winner_text.set_depth(-11)
        self._window.add(winner_text)

    def get_legth_deck(self):
        return self._deck.get_length()

    def _end_turn(self):
        if self._deck.get_length() == 0:
            self.end_game()
        else:
            self._text_zone.update_scores(self._piles[0].calc_score(), 
                self._piles[1].calc_score())
            self._hands[self._turn].hide_hand()
            self._turn += 1
            self._turn %= 2
            self._hands[self._turn].render_hand()
            self._text_zone.update_turn(self._turn)
            self._stage_number = 0
            self._text_zone.update_instructions(self._stage_number)

    def handle_key_press(self, event):
        # a turn has three stages: choose card (1), play chosen card (2), redraw
        if self._stage_number == 0 and event.get_key().isdigit() and 1 <= int(event.get_key()) <= 8:
            self._chosen_card = self._hands[self._turn].get_card(int(event.get_key()) - 1)
            self._hands[self._turn].remove_from_hand(int(event.get_key()) - 1)
            self._stage_number = 1
            self._text_zone.update_instructions(self._stage_number)

            # now that the card has been picked it is time to move to phase 2
        elif self._stage_number == 1 and (event.get_key() == 'a' or event.get_key() == 'b'):
            # automatically remove the chosen card from the players hand
            # give them the choice of either the pile in front (a) or discard (b)

            if event.get_key() == 'a':
                # move the card in hand to the PLAYER's pile

                if self._chosen_card.get_value() >= self._piles[self._turn].get_card(self._window, COLOR_DICT[self._chosen_card.get_color()]).get_value():
                    self._piles[self._turn].place_card(self._chosen_card, COLOR_DICT[self._chosen_card.get_color()])
                    if self._turn == 0:
                        self._chosen_card.move_card((WINDOW_WIDTH * (COLOR_DICT[self._chosen_card.get_color()] +1) // 6, 7 * WINDOW_HEIGHT // 10))
                        self._text_zone.update_scores(self._piles[0].calc_score(), 
                            self._piles[1].calc_score())

                        self._stage_number = 2
                    elif self._turn == 1:
                        self._chosen_card.move_card((WINDOW_WIDTH * (COLOR_DICT[self._chosen_card.get_color()] +1) // 6, 3 * WINDOW_HEIGHT // 10))
                        self._text_zone.update_scores(self._piles[0].calc_score(), 
                            self._piles[1].calc_score())
                        self._stage_number = 2
                else:
                    # INVENT A CASE WHERE STAGE # IS ZERO AND THE GET KEY IS 'A'
                    # FORCE USER TO REPICK CARD. NOT SURE HOW TO DO THIS
                    Banner(self._window, 'Cards have to ascend! Please discard.')

            elif event.get_key() == 'b':
                # move the card in hand to the DISCARD pile
                self._discard.reorder()
                self._discard.place_card(self._chosen_card, COLOR_DICT[self._chosen_card.get_color()])
                self._chosen_card.move_card((WINDOW_WIDTH * (COLOR_DICT[self._chosen_card.get_color()] +1) // 6, WINDOW_HEIGHT // 2))
                self._stage_number = 2

            self._text_zone.update_instructions(self._stage_number)

        elif self._stage_number == 2 and (event.get_key() == 'c' or event.get_key() == 'd'):
            if event.get_key() == 'c':
                # then we redraw a card from the DECK
                self._hands[self._turn].add_to_hand(self._deck.draw())
                # if self._deck.get_length == 0:
                #   self.end_game()
                self._text_zone.update_deck(self._deck.get_length())
                # if they went down this path, then the turn is done!
                self._end_turn()
            elif event.get_key() == 'd':
                # then we redraw a card from the DISCARD (if possible)
                # ask the player to choose from the discard
                # this is the ONLY TIME phase 3 is in effect
                self._stage_number = 3
                self._text_zone.update_instructions(self._stage_number)

        elif self._stage_number == 3 and event.get_key().isdigit() and 1 <= int(event.get_key()) <= 5:
            # this will not be valid if the length of the sub-pile is zero
            if self._discard.sub_pile_is_empty(int(event.get_key()) - 1):
                Banner(self._window, 'You can\'t draw from nothing!\nTry again by pressing "c" or "d".')
                self._stage_number = 2
            elif self._chosen_card == self._discard.get_card(self._window, int(event.get_key()) - 1):
                Banner(self._window, 'You can\'t pick up the card you just drew!\nTry again by pressing "c" or "d".')
                self._stage_number = 2
            else:
                self._hands[self._turn].add_to_hand(self._discard.remove_card(int(event.get_key()) - 1))
                self._end_turn()

def draw_board(window):
    # The discard board:
    discard_board = Image(window, "board5.png", 9 * WINDOW_WIDTH // 10, 
        WINDOW_HEIGHT // 5, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    discard_board.set_depth(10)
    window.add(discard_board)


    # The hand zone:
    hand_zone = Rectangle(window, WINDOW_WIDTH, WINDOW_HEIGHT // 5, 
        (WINDOW_WIDTH // 2, 9 * WINDOW_HEIGHT // 10))
    hand_zone.set_fill_color("brown")
    hand_zone.set_depth(10)
    window.add(hand_zone)

    # The text zone:
    text_zone = Rectangle(window, WINDOW_WIDTH, WINDOW_HEIGHT // 5, 
        (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 10))
    text_zone.set_fill_color("seagreen")
    text_zone.set_depth(10)
    window.add(text_zone)

def main(window):
    # some graphics window setup:
    window.set_width(WINDOW_WIDTH)
    window.set_height(WINDOW_HEIGHT)
    window.set_background(BACKGROUND)

    draw_board(window)

    my_game = Game(window)
    # Extra bells and whistles:
    # make cheat button reset in a set state with 10 cards left in the deck
    # make button that asks user to play again.
if __name__ == '__main__':
    StartGraphicsSystem(main)