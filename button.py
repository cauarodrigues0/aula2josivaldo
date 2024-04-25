from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

class MyApp(App):
    def build(self):
        return Button(text = "Clique Aqui!", background_color = get_color_from_hex("3498db"))

if __name__ == "__main__":
    MyApp().run()