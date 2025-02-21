from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file("cardstyle.kv")


class Card(Button):
    def __init__(self, symbol, **params):
        super().__init__(**params)
        self.symbol = symbol
        self.is_face_up = False
        self.is_matched = False
        self.setup_facedown()

    def setup_facedown(self):
        self.background_normal = ""
        self.background_color = (1, 0.616, 0.137, 1)  # สีเมื่อคว่ำ
        self.text = ""
