import random
from kivy.clock import Clock
from .cards import Card
from kivy.animation import Animation

class CardManager:
    def __init__(self, grid_layout):
        self.grid = grid_layout
        self.cards = []
        self.selected_cards = []
        self.pairs = 8  # ค่าเริ่มต้น
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
        if card.is_matched or card in self.selected_cards:
            return

        card.flip()
        self.selected_cards.append(card)

        if len(self.selected_cards) == 2:
            Clock.schedule_once(self.compare_cards, 1)

    def compare_cards(self, dt):
        c1, c2 = self.selected_cards
        if c1.symbol == c2.symbol:
            c1.is_matched = c2.is_matched = True
            self.match_animate(c1, c2)
        else:
            for c in [c1, c2]:
                c.flip()
        self.selected_cards.clear()

    def match_animate(self, *cards):
        ani = Animation(background_color=(0, 1, 0, 1), duration=0.5) + Animation(background_color=(1, 1, 1, 1), duration=0.5)
        for card in cards:
            ani.start(card)