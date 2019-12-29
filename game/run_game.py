#the following is the verbatim copy of my messy "run game" function from earlier
def run_game(self):
        while len(self._deck.get_deck()) != 0:
            print('Player 1:', self._pile_1.calc_score(), 'Player 2:', self._pile_2.calc_score())
            print(self._pile_2.get_printable_pile())

            print(self._discard.get_printable_pile())


            print(self._pile_1.get_printable_pile(), '\n')
            print(self._hand_1.get_printable_hand())


            while self._can_play == False:
                self._played = int(input('Which card in your hand do you want to play?'))
                self._pile = int(input('and which pile do you want to play it onto?'))
                self._pos = COLOR_DICT.get(self._hand_1.get_hand()[self._played].get_color())

                if self._pile == 0:
                    if self._pile_1.get_card(self._pos).get_value() < self._hand_1.get_hand()[self._played].get_value():
                        self._can_play = True
                    else:
                        print('No, senor.')

                if self._pile == 1:
                    if self._pile_1.get_card(self._pos).get_value() < self._discard.get_hand()[self._played].get_value():
                        self._can_play = True
                    else:
                        print('No, senor.')

            if self._pile == 0:
                self._pile_1.place_card(self._hand_1.get_hand()[self._played], self._pos)
            if self._pile == 1:
                self._discard.place_card(self._hand_1.get_hand()[self._played], self._pos)
            self._hand_1.remove_from_hand(self._played)


            self._draw_deck = int(input('Would you like to draw from discard or deck?'))
            if self._draw_deck == 0:
                self._hand_1.add_to_hand(self._deck.draw())
            if self._draw_deck == 1:
                self._pos = input('Where would you like to draw from?')
                self._hand_1.add_to_hand(self._discard.remove_card(self._pos))
            self._can_play = False

            # this is a break between player 1 and player2

            input("Player 2's turn")

            print('Player 1:', self._pile_1.calc_score(), 'Player 2:', self._pile_2.calc_score())

            print(self._pile_1.get_printable_pile())

            print(self._discard.get_printable_pile())


            print(self._pile_2.get_printable_pile(), '\n')
            print(self._hand_2.get_printable_hand())

            while self._can_play == False:
                self._played = int(input('Which card in your hand do you want to play?'))
                self._pile = int(input('and which pile do you want to play it onto?'))
                self._pos = int(COLOR_DICT.get(self._hand_2.get_hand()[self._played].get_color()))

                if self._pile == 0:
                    if self._pile_2.get_card(self._pos).get_value() < self._hand_2.get_hand()[self._played].get_value():
                        self._can_play = True
                    else:
                        print('No, senor.')
                if self._pile == 1:
                    if self._pile_2.get_card(self._pos).get_value() < self._hand_2.get_hand()[self._played].get_value():
                        self._can_play = True
                    else:
                        print('No, senor.')
            if self._pile == 0:
                self._pile_2.place_card(self._hand_2.get_hand()[self._played], self._pos)
            if self._pile == 1:
                self._discard.place_card(self._hand_2.get_hand()[self._played], self._pos)
            self._hand_2.remove_from_hand(self._played)


            self._draw_deck = int(input('Would you like to draw from discard or deck?'))
            if self._draw_deck == 0:
                self._hand_2.add_to_hand(self._deck.draw())
            if self._draw_deck == 1:
                self._pos = input('Where would you like to draw from?')
                self._hand_2.add_to_hand(self._discard.remove_card(self._pos))
            self._can_play = False

            input("Player 1's turn")
        if self._pile_1.calc_score() == self._pile_2.calc_score():
            print('AAAAA')
        elif self._pile_1.calc_score() > self._pile_2.calc_score():
            print("Player 1 wins!")
        else:
            print('Player 2 wins!')
