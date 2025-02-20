from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
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
