from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import Mainmenuscreen, Gamescreen
from screens.difficulty_screen import DifficultyScreen
from kivy.lang import Builder

Builder.load_file("gamesceenstyle.kv")
Builder.load_file("cardstyle.kv")


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Mainmenuscreen(name="main_menu"))
        self.add_widget(Gamescreen(name="game_screen"))


class MyGame(App):
    def build(self):
        SM = ScreenManager()
        SM.add_widget(Mainmenuscreen(name="main_menu"))
        SM.add_widget(DifficultyScreen(name="Difficulty"))
        SM.add_widget(Gamescreen(name="Game"))
        return SM


if __name__ == "__main__":
    MyGame().run()
