from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        
        layout = BoxLayout(orientation = 'vertical', spacing = 10)

        btn1 = Button(text = "Botão 1", background_color = (0.2, 0.7, 0.3, 1), font_size = 20)
        

        btn2 = Button(text = "Clique Aqui", halign = "center")

        btn3 = Button(text = "Clique aqui para continuar", background_color = (0.9, 0.5, 0.1, 1), font_size = 30)

        def AcaoBotao(instance):
            instance.text = "Botão Pressionado"
        
        btn4 = Button(text = "Botão 4")
        btn4.bind(on_press = AcaoBotao)

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)



        info = Label(text = "Pressione para ver diferentes propriedades em ação.")

        layout.add_widget(info)

        return layout

if __name__ == "__main__":
    MyApp().run()