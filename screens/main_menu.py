from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, RoundedRectangle


class CustomButton(Button):
    def __init__(self, **params):
        super().__init__(**params)
        self.font_size = 24
        self.size_hint = (None, None)
        self.size = (180, 70)
        self.bold = True
        self.color = (1, 1, 1, 1)
        self.background_normal = ""
        self.background_color = (0, 0, 0, 0)
        self.border = (16, 16, 16, 16)

        with self.canvas.before:
            Color(0, 0.6, 1, 1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class Mainmenuscreen(Screen):
    def __init__(self, **params):
        super().__init__(**params)
        layout = FloatLayout()

        start_button = CustomButton(
            text="Start Game",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        start_button.bind(on_press=self.switch_to_game)

        layout.add_widget(start_button)
        self.add_widget(layout)

    def switch_to_game(self, instance):
        self.manager.current = "Game"
