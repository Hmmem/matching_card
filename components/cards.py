from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.graphics import Color, RoundedRectangle


class Card(Button):
    def __init__(self, symbol, **params):
        super().__init__(**params)
        self.symbol = symbol
        self.is_face_up = False
        self.is_matched = False
        self.setup_facedown()

    def setup_facedown(self):
        self.background_color = (0, 0, 0, 0)
        self.color = (0, 0, 0, 0)

        with self.canvas.before:
            Color(1.0, 0.616, 0.137, 1)
            self.round = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(pos=self.update_border, size=self.update_border)

    def update_border(self, *args):
        self.round.pos = self.pos
        self.round.size = self.size
