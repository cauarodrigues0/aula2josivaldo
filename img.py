from kivy.app import App
from kivy.uix.image import Image

class MyApp(App):
    def build(self):
        return Image(source="C:/Users/aluno.sesipaulista/Downloads/images1.jpg")
    
if __name__=="__main__":
    MyApp().run()