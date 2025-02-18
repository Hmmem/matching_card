from kivy.app import App
from kivy.uix.label import Label


class MyGame(App):
    def build(self):
        return Label(text="STARTED!!", font_size=40)


if __name__ == "__main__":
    MyGame().run()