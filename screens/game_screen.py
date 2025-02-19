from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label


class Gamescreen(Screen):
    def __init__(self, **params):
        super().__init__(**params)
        label = Label(text="Welcome To The Game!!", font_size=40)
        self.add_widget(label)
