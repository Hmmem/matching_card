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
        self.background_normal = ""
        self.background_color = (0.2, 0.6, 0.9, 1)
        self.color = (0, 0, 0, 0)
