from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2, spacing = [10, 10], padding = [20, 20])
        for i in range(4):
            btn = Button(text = f"Botão {i + 1}")
            layout.add_widget(btn)

        return layout

if __name__ == '__main__':
    MyApp().run()