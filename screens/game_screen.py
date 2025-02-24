from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from components import CardManager

Builder.load_file("gamesceenstyle.kv")

class Gamescreen(Screen):
    def __init__(self, **params):
        super().__init__(**params)
        self.grid = GridLayout(cols=4, spacing=10, padding=20, size_hint=(None, None), pos_hint={"center_x": 0.5, "center_y": 0.65})
        self.card_manager = CardManager(self.grid)
        self.add_widget(self.grid)

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