from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal', spacing = 10, padding = [20, 10])
        for i in range(3):
            btn = Button(text = f"Botão {i+1}")
            layout.add_widget(btn)

        return layout


if __name__ == '__main__':
    MyApp().run()