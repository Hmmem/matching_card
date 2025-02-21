from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file("cardstyle.kv")


class Card(Button):
    def __init__(self, symbol, **params):
        super().__init__(**params)
        self.symbol = symbol
        self.is_face_up = False
        self.is_matched = False
