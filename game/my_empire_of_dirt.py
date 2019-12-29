    # class CheatMode:
    #     def handle_mouse_press(self):
    #         MAX_CARD_SIZE = 5
    #         ...range(2,MAX_CARD_SIZE + 1)...
    #         Board(dasd, asdasdas, asdd)
    def near_win(self):
        self._hands[0] = [Card(self._window, "yellow", 2), 
        Card(self._window, "yellow", 6), 
        Card(self._window, "yellow", 7), Card(self._window, "blue", 1), 
        Card(self._window, "blue", 10), Card(self._window, "green", 8), 
        Card(self._window, "red", 1), Card(self._window, "red", 7)]

        self._hands[1] = [Card(self._window, "yellow", 3), 
        Card(self._window, "yellow", 1), 
        Card(self._window, "blue", 5), Card(self._window, "blue", 7), 
        Card(self._window, "blue", 9), Card(self._window, "white", 3), 
        Card(self._window, "white", 8), Card(self._window, "green", 3)] 

        self._piles[0] = [[Card(self._window, "yellow", 5), 
        Card(self._window, "yellow", 8),
        Card(self._window, "yellow", 9), Card(self._window, "yellow", 10)], 
        [Card(self._window, "blue", 2), Card(self._window, "blue", 3), 
        Card(self._window, "blue", 8)], [Card(self._window, "white", 4), 
        Card(self._window, "white", 5), Card(self._window, "white", 9),
        Card(self._window, "white", 10)], [Card(self._window, "green", 1), 
        Card(self._window, "green", 4), Card(self._window, "green", 5), 
        Card(self._window, "green", 7)], [Card(self._window, "red", 3), 
        Card(self._window, "red", 5)]] 
        self._piles[1] = [[], [Card(self._window, "blue", 1), 
        Card(self._window, "blue", 4),
        Card(self._window, "blue", 6)], [Card(self._window, "white", 2), 
        Card(self._window, "white", 6), Card(self._window, "white", 7)], 
        [Card(self._window, "green", 1), Card(self._window, "green", 1), 
        Card(self._window, "green", 2)], [Card(self._window, "red", 1), 
        Card(self._window, "red", 2), Card(self._window, "red", 4), 
        Card(self._window, "red", 6)]]

        self._discard = [[Card(self._window, "yellow", 1), 
        Card(self._window, "yellow", 1)], 
        [Card(self._window, "blue", 1), Card(self._window, "blue", 5)], 
        [], [], []]

        self._deck = [Card(self._window, "green", 6), Card(self._window, "green", 9),
        Card(self._window, "green", 10), Card(self._window, "white", 1),
        Card(self._window, "white", 1), Card(self._window, "white", 1), 
        Card(self._window, "red", 1), Card(self._window, "red", 8), 
        Card(self._window, "red", 9), Card(self._window, "red", 10)]

        self._stage_number = 0
        self._turn = 0