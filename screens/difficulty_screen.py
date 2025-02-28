from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class DifficultyScreen(Screen):
    def __init__(self, **params):
        super().__init__(**params)
        layout = FloatLayout()

        title = Button(
            text="Choose Difficulty",
            size_hint=(None, None),
            size=(250, 70),
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            background_color=(0, 0, 0, 0),
        )
        easy_button = Button(
            text="Easy",
            size_hint=(None, None),
            size=(150, 60),
            pos_hint={"center_x": 0.3, "center_y": 0.5},
        )
        medium_button = Button(
            text="Medium",
            size_hint=(None, None),
            size=(150, 60),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        hard_button = Button(
            text="Hard",
            size_hint=(None, None),
            size=(150, 60),
            pos_hint={"center_x": 0.7, "center_y": 0.5},
        )

        easy_button.bind(on_press=lambda instance: self.switch_to_game("Easy"))
        medium_button.bind(on_press=lambda instance: self.switch_to_game("Medium"))
        hard_button.bind(on_press=lambda instance: self.switch_to_game("Hard"))

        layout.add_widget(title)
        layout.add_widget(self.best_time_label)
        layout.add_widget(easy_button)
        layout.add_widget(medium_button)
        layout.add_widget(hard_button)
        self.add_widget(layout)

    def switch_to_game(self, difficulty):
        """ส่งค่าความยากไปที่ Gamescreen แล้วเปลี่ยนหน้า"""
        self.manager.get_screen("Game").set_difficulty(difficulty)
        self.manager.current = "Game"

    def update_best_time(self, best_time):
        """อัปเดตค่า Best Time ที่ได้รับจาก Gamescreen"""
        self.best_time_label.text = best_time
