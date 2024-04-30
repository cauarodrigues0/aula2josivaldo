from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2)

        col_esq = BoxLayout(orientation = "vertical", size_hint = (0.3, 1))

        menu_itens = ['Arquivo', 'Editar', 'Seleção', 'Ver', 'Acessar', 'Sair']

        label1 = Label(text = 'Menu')
        col_esq.add_widget(label1)

        for item in menu_itens:
            btn = Button(text = item)
            col_esq.add_widget(btn)

        col_dir = GridLayout(cols = 1, rows = 3)
        for i in range(3):
            botao = Button(text = f"Botão {i + 7}")
            col_dir.add_widget(botao)

        layout.add_widget(col_esq)
        layout.add_widget(col_dir)
        return layout

if __name__ == '__main__':
    MyApp().run()

