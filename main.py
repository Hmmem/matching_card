from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import MainMenuScreen


class MyGame(App):
    def build(self):
        SM = ScreenManager()
        SM.add_widget(MainMenuScreen(name="main"))
        return SM


if __name__ == "__main__":
    MyGame().run()
