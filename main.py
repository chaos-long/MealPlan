from kivymd.app import MDApp
from kivy.clock import Clock
from layout import My

class MainApp(MDApp):
    def change800(self):
        M = self.root.ids.bar100

        TEXT = M.children[0].children[0].children[0].children[0].children[0]
        TEXT.font_style = "Caption"

        TEXT = M.children[0].children[0].children[1].children[0].children[0]
        TEXT.font_style = "Caption"

        TEXT = M.children[0].children[0].children[2].children[0].children[0]
        TEXT.font_style = "Caption"


    def __init__(self):
        super().__init__()

    def build(self):
        self.icon = 'icons_and_images/logo.png'
        Clock.schedule_once(lambda x: self.change800(), 2)
        return My()

    def on_start(self):
        Clock.schedule_once(self.main, 4)

    def main(self, x):
        self.root.current = 'main'


if __name__ == "__main__":
    MainApp().run()
