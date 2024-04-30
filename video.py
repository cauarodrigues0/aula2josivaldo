from kivy.app import App
from kivy.uix.video import Video

class MyApp(App):
    def build(self):
        return Video(source = "C:/Users/aluno.sesipaulista/Downloads/38275-415950942_tiny.mp4")
if __name__ == "__main__":
    MyApp().run()