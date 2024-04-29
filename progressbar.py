from kivy.app import App
from kivy.uix.progressbar import ProgressBar

class MyApp(App):
    def build(self):
        return ProgressBar(value = 50)

if __name__ == '__main__':
    MyApp().run()