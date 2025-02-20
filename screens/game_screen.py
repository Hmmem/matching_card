from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from components import Card, CardManager


class Gamescreen(Screen):
    def __init__(self, **params):
        super().__init__(**params)

        grid = GridLayout(
            cols=4,
            spacing=10,
            padding=20,
            size_hint=(0.5, 0.8),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        for i in range(16):
            card = Card(symbol="A")
            grid.add_widget(card)
        self.add_widget(grid)

        with self.canvas.before:
            Color(0.92, 0.9, 0.76, 1)
            self.bg_color = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_bg, size=self.update_bg)

    def update_bg(self, *args):
        self.bg_color.pos = self.pos
        self.bg_color.size = self.size
