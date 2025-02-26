from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, RoundedRectangle


class Mainmenuscreen(Screen):
    def __init__(self, **params):
        super().__init__(**params)

    def go_to_difficulty(self, instance):
        self.manager.current = "Difficulty"

    def switch_to_game(self, difficulty):
        self.manager.get_screen("Game").set_difficulty(difficulty)
        self.manager.current = "Game"
