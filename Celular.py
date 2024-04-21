import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

kivy.require('1.11.1')

class MyApp(App):
    def build(self):
        self.orientation = 'vertical'

        # Layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=(20))

        # Label
        label = Label(text="Você quer namorar comigo?", font_size=24, halign='center')
        layout.add_widget(label)

        # Botões
        btn_sim = Button(text='Sim', size_hint=(None, None), width=100, height=50)
        btn_nao = Button(text='Não', size_hint=(None, None), width=100, height=50)

        # Funções de clique para os botões
        btn_sim.bind(on_release=self.sim_clicked)
        btn_nao.bind(on_release=self.nao_clicked)

        layout.add_widget(btn_sim)
        layout.add_widget(btn_nao)

        return layout

    def sim_clicked(self, instance):
        layout = instance.parent  # Obtém o layout pai do botão clicado
        layout.clear_widgets()  # Limpa os widgets atuais

        # Cria uma nova label com a mensagem "Eu sabia"
        label = Label(text="Eu sabia!", font_size=24, halign='center')
        layout.add_widget(label)

    def nao_clicked(self, instance):
        layout = instance.parent  # Obtém o layout pai do botão clicado
        layout.clear_widgets()  # Limpa os widgets atuais

        # Cria uma nova label com a mensagem "Você disse não :("
        label = Label(text="Você disse não :(", font_size=24, halign='center')
        layout.add_widget(label)

if __name__ == '__main__':
    MyApp().run()
