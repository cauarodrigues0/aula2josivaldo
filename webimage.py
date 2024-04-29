from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MyApp(App):
    def build(self):
        return AsyncImage(source = "https://i0.wp.com/innovationyourself.com/wp-content/uploads/2021/01/kivy.png")
    
if __name__ == "__main__":
    MyApp().run()