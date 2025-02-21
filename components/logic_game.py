import random
from kivy.clock import Clock
from .cards import Card


class CardManager:
    def __init__(self, grid_layout):
        self.grid = grid_layout
        self.cards = []
        self.selected_cards = []
        self.pairs = 8
        self.create_board()

    def create_board(self):
        symbols = [chr(65 + i) for i in range(self.pairs)] * 2
        random.shuffle(symbols)

        self.grid.clear_widgets()
        for symbol in symbols:
            card = Card(symbol=symbol, size_hint=(None, None), size=(100, 150))
            card.bind(on_release=lambda c=card: self.check_match(c))
            self.cards.append(card)
            self.grid.add_widget(card)

    def check_match(self, card):
        if card.is_matched or card in self.selected_cards:
            return
