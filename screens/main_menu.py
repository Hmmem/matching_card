from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MainMenuScreen(Screen):
    def __init__(self, **paraams):
        super().__init__(**paraams)
        layout = BoxLayout(orientation="vertical")

        start_button = Button(
            text="Start Game",
            size_hint=(0.3, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        start_button.bind(on_press=self.switch_to_game)

        layout.add_widget(start_button)
        self.add_widget(layout)

    def switch_to_game(self, instance):
        self.manager.current = "Game"
