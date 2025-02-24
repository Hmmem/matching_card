from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from components import CardManager
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("gamesceenstyle.kv")

class Gamescreen(Screen):
    def __init__(self, **params):
        super().__init__(**params)
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.grid = GridLayout(cols=4, spacing=10, padding=20, size_hint=(None, None), pos_hint={"center_x": 0.5, "center_y": 0.65})
        self.card_manager = CardManager(self.grid)
        self.add_widget(self.grid)

        back_button = Button (
            text="Back to Menu",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x":0.5}
        )
        back_button.bind(on_release=self.go_to_menu)
        main_layout.add_widget(back_button)

        self.add_widget(main_layout)

    def go_to_menu(self, instance):
        self.manager.current = "main_menu"  # เปลี่ยนกลับไปที่เมนูหลัก

    def set_difficulty(self, difficulty):
        self.card_manager.set_difficulty(difficulty)

        if difficulty == "Easy" :
            self.grid.cols = 2
        elif difficulty == "Medium" :
            self.grid.cols = 4
        elif difficulty == "Hard" :
            self.grid.cols = 6

         # คำนวณขนาด Grid ตามจำนวนการ์ด
        card_width, card_height = 100, 150  # ขนาดการ์ดแต่ละใบ
        total_width = self.grid.cols * card_width + (self.grid.cols - 1) * 10  # รวม spacing
        total_height = (self.card_manager.pairs // self.grid.cols) * card_height + ((self.card_manager.pairs // self.grid.cols) - 1) * 10

        self.grid.size = (total_width, total_height)  # ปรับขนาด Grid