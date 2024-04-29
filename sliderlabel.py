from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # layout principal
        layout = BoxLayout(orientation = "vertical", padding = 20)

        # Slider
        slider = Slider(min = 0, max = 100, value = 50, step = 1)

        slider.bind(value = self.atualizar_label)

        self.label = Label(text = f"Valor do slider: {int(slider.value)}")

        layout.add_widget(slider)
        layout.add_widget(self.label)

        return layout
    
    def atualizar_label(self, instance, value):
        self.label.text = f"Valor do slider: {int(value)}"

if __name__ == "__main__":
    MyApp().run()

