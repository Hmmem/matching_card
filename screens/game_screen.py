from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from components import CardManager

Builder.load_file("gamesceenstyle.kv")

class Gamescreen(Screen):
    def __init__(self, **params):
        super().__init__(**params)
        self.grid = GridLayout(cols=4, spacing=10, padding=20, size_hint=(0.5, 0.8), pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.card_manager = CardManager(self.grid)
        self.add_widget(self.grid)

    def set_difficulty(self, difficulty):
        self.card_manager.set_difficulty(difficulty)