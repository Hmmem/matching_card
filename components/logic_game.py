import random
from kivy.clock import Clock
from .cards import Card
from kivy.animation import Animation


class CardManager:
    def __init__(self, grid_layout):
        self.grid = grid_layout
        self.cards = []
        self.selected_cards = []
        self.pairs = 8
        self.is_processing = False
        self.create_board()

    def set_difficulty(self, difficulty):
        if difficulty == "Easy":
            self.pairs = 4
        elif difficulty == "Medium":
            self.pairs = 8
        elif difficulty == "Hard":
            self.pairs = 12
        self.create_board()

    def create_board(self):
        symbols = [chr(65 + i) for i in range(self.pairs)] * 2
        random.shuffle(symbols)

        self.grid.clear_widgets()
        self.cards = []
        for symbol in symbols:
            card = Card(symbol=symbol, size_hint=(None, None), size=(100, 150))
            card.bind(on_release=lambda c=card: self.check_match(c))
            self.cards.append(card)
            self.grid.add_widget(card)

    def check_match(self, card):
        if (
            card.is_matched
            or card in self.selected_cards
            or self.is_processing
            or len(self.selected_cards) >= 2
        ):
            return

        card.flip()
        self.selected_cards.append(card)

        if len(self.selected_cards) == 2:
            self.is_processing = True
            Clock.schedule_once(self.compare_cards, 0.7)

    def compare_cards(self, dt):
        c1, c2 = self.selected_cards
        if c1.symbol == c2.symbol:
            c1.is_matched = c2.is_matched = True
            self.match_animate(c1, c2)
        else:
            for c in [c1, c2]:
                c.flip()
        self.selected_cards.clear()
        self.is_processing = False

    def match_animate(self, *cards):
        for card in cards:
            Animation(opacity=0, duration=0.3).start(card)
            card.disabled = True
            card.is_matched = True
