from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from components import CardManager
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.clock import Clock
from kivy.uix.label import Label


class Gamescreen(Screen):
    def __init__(self, **params):
        super().__init__(**params)
        main_layout = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10,
        )

        top_layout = BoxLayout(size_hint_y=None, height=100, spacing=20)
        self.timer_label = Label(text="Time: 00:00.0", font_size=24, halign="center")
        self.best_time_label = Label(
            text="Best Time: --:--.--", font_size=24, halign="center"
        )

        top_layout.add_widget(self.timer_label)
        top_layout.add_widget(self.best_time_label)
        main_layout.add_widget(top_layout)

        middle_layout = AnchorLayout()
        self.grid = GridLayout(spacing=10, size_hint=(None, 1))
        self.grid.bind(minimum_width=self.grid.setter("width"))
        middle_layout.add_widget(self.grid)
        main_layout.add_widget(middle_layout)

        bottom_layout = AnchorLayout(size_hint_y=None, height=50)
        back_button = Button(
            text="Back to Menu",
            size_hint=(None, None),
            size=(200, 50),
        )

        back_button.bind(on_release=self.go_to_menu)
        bottom_layout.add_widget(back_button)
        main_layout.add_widget(bottom_layout)

        self.add_widget(main_layout)
        self.card_manager = CardManager(self.grid)
        self.timer_event = None
        self.time_elapsed = 0
        self.best_time = None

    def go_to_menu(self, instance):
        self.manager.current = "main_menu"  # เปลี่ยนกลับไปที่เมนูหลัก
        self.stop_timer()

    def start_timer(self):
        """เริ่มจับเวลา"""
        self.time_elapsed = 0
        self.timer_event = Clock.schedule_interval(self.update_timer, 0.1)

    def update_timer(self, dt):
        """อัปเดตเวลาใน Label ทุก 0.1 วินาที"""
        self.time_elapsed += 1  # นับเป็นหน่วยของ 0.1 วินาที

        minutes = self.time_elapsed // 600  # 1 นาที = 600 หน่วย (0.1 * 600 = 60 วินาที)
        seconds = (self.time_elapsed // 10) % 60  # 1 วินาที = 10 หน่วย
        milliseconds = self.time_elapsed % 10  # เสี้ยววินาที (0.1 วินาที)

        self.timer_label.text = f"Time: {minutes:02}:{seconds:02}.{milliseconds}"

    def stop_timer(self):
        """หยุดจับเวลาเมื่อจบเกม"""
        if self.timer_event:
            Clock.unschedule(self.timer_event)
            self.timer_event = None

        if self.best_time is None or self.time_elapsed < self.best_time:
            self.best_time = self.time_elapsed  # อัปเดตค่าที่ดีที่สุด
            minutes = self.best_time // 600
            seconds = (self.best_time // 10) % 60
            milliseconds = self.best_time % 10
            self.best_time_label.text = (
                f"Best Time: {minutes:02}:{seconds:02}.{milliseconds}"
            )

    def set_difficulty(self, difficulty):
        self.card_manager.set_difficulty(difficulty)
        self.start_timer()

        if difficulty == "Easy":
            self.grid.cols = 4
        elif difficulty == "Medium":
            self.grid.cols = 4
        elif difficulty == "Hard":
            self.grid.cols = 6
