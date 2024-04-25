from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build (self):
        return Button(text='Hello World', size_hint = (0.2, 0.5))
if __name__ == '__main__':
    MyApp().run()