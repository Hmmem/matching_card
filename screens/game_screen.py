from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout

from components import CardManager
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.label import Label


class Gamescreen(Screen):
    def __init__(self, **params):
        super().__init__(**params)
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # เพิ่ม Label แสดงเวลา
        self.time_elapsed = 0
        self.best_time = None

        self.timer_label = Label(
            text="Time: 00:00.0", size_hint=(1, None), height=50, font_size=24
        )
        self.best_time_label = Label(
            text="Best Time: --:--.--", size_hint=(1, None), height=50, font_size=24
        )

        main_layout.add_widget(self.timer_label)
        main_layout.add_widget(self.best_time_label)

        # เรียกใช้งานจับเวลา
        self.timer_event = None

        self.grid = GridLayout(
            cols=4,
            spacing=10,
            padding=20,
            size_hint=(None, None),
            pos_hint={"center_x": 0.5, "center_y": 0.65},
        )
        self.card_manager = CardManager(self.grid)
        self.add_widget(self.grid)

        back_button = Button(
            text="Back to Menu",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5},
        )
        back_button.bind(on_release=self.go_to_menu)
        main_layout.add_widget(back_button)

        self.add_widget(main_layout)

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

        # คำนวณขนาด Grid ตามจำนวนการ์ด
        card_width, card_height = 100, 150  # ขนาดการ์ดแต่ละใบ
        total_width = (
            self.grid.cols * card_width + (self.grid.cols - 1) * 10
        )  # รวม spacing
        total_height = (self.card_manager.pairs // self.grid.cols) * card_height + (
            (self.card_manager.pairs // self.grid.cols) - 1
        ) * 10

        self.grid.size = (total_width, total_height)  # ปรับขนาด Grid
