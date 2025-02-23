from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import Mainmenuscreen, Gamescreen
from screens.difficulty_screen import DifficultyScreen



class MyGame(App):
    def build(self):
        SM = ScreenManager()
        SM.add_widget(Mainmenuscreen(name="Main"))
        SM.add_widget(DifficultyScreen(name="Difficulty"))
        SM.add_widget(Gamescreen(name="Game"))
        return SM


if __name__ == "__main__":
    MyGame().run()
