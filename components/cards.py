from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.properties import BooleanProperty


class Card(Button):
    is_face_up = BooleanProperty(False)

    def __init__(self, symbol, **params):
        super().__init__(**params)
        self.symbol = symbol
        self.is_face_up = False
        self.is_matched = False

    def card_state_change(self, *args):
        self.is_face_up = not self.is_face_up

    def flip(self):
        original_width = self.width
        self.minimum_width = original_width
        ani = Animation(width=0, duration=0.15) + Animation(
            width=original_width, duration=0.15
        )
        ani.bind(on_complete=self.card_state_change)
        ani.start(self)
