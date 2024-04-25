from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

def botao_pressionado(instance):
    print("Botão Pressionado")


class MyApp(App):
    def build(self):
       btn = Button(text = "Clique Aqui!", background_color = get_color_from_hex("3498db"))
       btn.bind(on_press = botao_pressionado)
       return btn

if __name__ == "__main__":
    MyApp().run()