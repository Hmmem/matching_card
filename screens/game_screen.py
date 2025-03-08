from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from components import CardManager
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.app import App


class Gamescreen(Screen):
    def __init__(self, **params):
        super().__init__(**params)
        main_layout = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10,
        )

        top_layout = BoxLayout(
            size_hint_y=None, height=100, spacing=20, orientation="horizontal"
        )
        self.timer_label = Label(
            text="Time: 00:00.0",
            font_size=24,
            halign="center",
            size_hint_x=None,
            width=200,
        )
        self.best_time_label = Label(
            text="Best Time: --:--.--",
            font_size=24,
            halign="center",
            size_hint_x=None,
            width=200,
        )

        spacer = Widget(size_hint_x=1)

        stop_anchor = AnchorLayout(anchor_x="right", size_hint_x=None, width=150)

        self.stop_button = Button(
            text="",
            background_normal="icons8-settings-80.png",
            background_down="icons8-settings-80.png",
            border=(0, 0, 0, 0),
            size_hint=(None, None),
            size=(80, 80),
        )
        self.stop_button.bind(on_release=self.toggle_stop_game)
        stop_anchor.add_widget(self.stop_button)

        top_layout.add_widget(self.timer_label)
        top_layout.add_widget(self.best_time_label)
        top_layout.add_widget(spacer)
        top_layout.add_widget(stop_anchor)

        main_layout.add_widget(top_layout)

        middle_layout = AnchorLayout()
        self.grid = GridLayout(spacing=10, size_hint=(None, 1))
        self.grid.bind(minimum_width=self.grid.setter("width"))
        middle_layout.add_widget(self.grid)
        main_layout.add_widget(middle_layout)

        bottom_layout = BoxLayout(size_hint_y=None, height=10)

        main_layout.add_widget(bottom_layout)

        self.add_widget(main_layout)
        self.card_manager = CardManager(self.grid, self)
        self.timer_event = None
        self.time_elapsed = 0
        self.best_time = None
        self.game_active = True
        self.is_stopped = False
        self.popup = None

    def go_to_menu(self, instance=None):
        self.manager.current = "main_menu"  # เปลี่ยนกลับไปที่เมนูหลัก
        self.stop_timer(game_completed=False)
        self.is_stopped = False

        if self.popup:
            self.popup.dismiss()

    def start_timer(self):
        """เริ่มจับเวลา"""
        self.game_active = True
        self.time_elapsed = 0
        self.timer_event = Clock.schedule_interval(self.update_timer, 0.1)

    def update_timer(self, dt):
        """อัปเดตเวลาใน Label ทุก 0.1 วินาที"""
        self.time_elapsed += 1  # นับเป็นหน่วยของ 0.1 วินาที

        minutes = self.time_elapsed // 600  # 1 นาที = 600 หน่วย (0.1 * 600 = 60 วินาที)
        seconds = (self.time_elapsed // 10) % 60  # 1 วินาที = 10 หน่วย
        milliseconds = self.time_elapsed % 10  # เสี้ยววินาที (0.1 วินาที)

        self.timer_label.text = f"Time: {minutes:02}:{seconds:02}.{milliseconds}"

        print(
            f"⏳ Timer Running: {self.time_elapsed} ({minutes}:{seconds}.{milliseconds})"
        )  # ✅ Debug

    def toggle_stop_game(self, instance):
        """กดปุ่มเพื่อสลับระหว่างหยุดเกมกับเล่นเกมต่อ"""
        if self.is_stopped:
            self.resume_game()  # เล่นต่อ
        else:
            self.stop_game()  # หยุดเกม

    def stop_game(self, *args):
        """หยุดเกมชั่วคราว โดยไม่ลบค่าจับเวลา"""
        if self.timer_event:
            Clock.unschedule(self.update_timer)  # หยุดชั่วคราว แต่ไม่ลบค่า
            self.timer_event = None  # ล้างตัวแปร event แต่ไม่รีเซ็ตเวลา
        self.is_stopped = True

        self.popup = PausePopup(
            resume_callback=self.resume_game,
            quit_callback=self.go_to_menu,
        )

        self.popup.open()

        app = App.get_running_app()
        app.stop_music()

    def resume_game(self):
        """เล่นเกมต่อ"""
        if self.timer_event is None:  # ตรวจสอบว่ากำลังหยุดอยู่จริง
            self.timer_event = Clock.schedule_interval(
                self.update_timer, 0.1
            )  # เริ่มจับเวลาต่อ
        self.is_stopped = False

        if self.popup:
            self.popup.dismiss()

        app = App.get_running_app()
        app.resume_music()

    def stop_timer(self, game_completed=False):
        """หยุดจับเวลาเมื่อจบเกม"""
        if self.timer_event:
            Clock.unschedule(self.timer_event)
            self.timer_event = None
        print(f"⏱ Current Time Elapsed: {self.time_elapsed}")

        best_time_text = self.best_time_label.text

        if game_completed:
            if self.best_time is None or self.time_elapsed < self.best_time:
                self.best_time = self.time_elapsed  # ✅ อัปเดตค่าที่ดีที่สุด
                print(f"✅ New Best Time Recorded: {self.best_time}")  # ✅ Debug

                minutes = self.best_time // 600
                seconds = (self.best_time // 10) % 60
                milliseconds = self.best_time % 10

                best_time_text = f"Best Time: {minutes:02}:{seconds:02}.{milliseconds}"
                print(f"🏆 Saving Best Time: {best_time_text}")  # ✅ Debug

                self.best_time_label.text = best_time_text  # ✅ อัปเดต Best Time บนเกม

                # ✅ ส่งค่า Best Time ไปที่หน้าเลือกความยาก
                difficulty_screen = self.manager.get_screen("Difficulty")
                difficulty_screen.update_best_time(best_time_text)

    def set_difficulty(self, difficulty):
        self.game_active = True
        self.card_manager.set_difficulty(difficulty)
        self.start_timer()

        if difficulty == "Easy":
            self.grid.cols = 3
        elif difficulty == "Medium":
            self.grid.cols = 4
        elif difficulty == "Hard":
            self.grid.cols = 6


class PausePopup(Popup):
    def __init__(self, resume_callback, quit_callback, **kwargs):
        super().__init__(**kwargs)
        self.resume_callback = resume_callback
        self.quit_callback = quit_callback

    def resume_game(self):
        self.resume_callback()
        self.dismiss()

    def quit_game(self):
        self.quit_callback()
        self.dismiss()
