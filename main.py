from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import Mainmenuscreen, Gamescreen
from screens.difficulty_screen import DifficultyScreen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader

Builder.load_file("gamesceenstyle.kv")
Builder.load_file("cardstyle.kv")
Builder.load_file("popup_style.kv")


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Mainmenuscreen(name="main_menu"))
        self.add_widget(Gamescreen(name="game_screen"))


class MyGame(App):
    def build(self):
        self.background_music = SoundLoader.load("samurai-lofium-292016.mp3")
        if self.background_music:
            self.background_music.loop = True
            self.background_music.volume = 0.5

        SM = ScreenManager()
        SM.add_widget(Mainmenuscreen(name="main_menu"))
        SM.add_widget(DifficultyScreen(name="Difficulty"))
        SM.add_widget(Gamescreen(name="Game"))
        return SM

    def stop_music(self):
        if self.background_music:
            self.background_music.stop()

    def resume_music(self):
        if self.background_music and self.background_music.state != "play":
            self.background_music.play()


if __name__ == "__main__":
    MyGame().run()
