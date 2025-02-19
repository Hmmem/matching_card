from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import Mainmenuscreen, Gamescreen


class MyGame(App):
    def build(self):
        SM = ScreenManager()
        SM.add_widget(Mainmenuscreen(name="Main"))
        SM.add_widget(Gamescreen(name="Game"))
        return SM


if __name__ == "__main__":
    MyGame().run()
