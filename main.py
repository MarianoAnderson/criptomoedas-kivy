# 1º importar o App, Builder (GUI)
# 2º criar o nosso aplicativo
# 3º criar a função buil

import requests
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.lang import Builder


#todo app do build kivy é criado dentro de uma classe
class Aplicativo(App):
    title = "Cotações de Criptomoedas"
    # atualiza/modifica o app aberto
    def on_start(self):
        # root: arquivo do GUI
        self.root.ids["moeda1"]#.text = f"Bitcoin R$ {self.pegar_cotacao('BTC')}"
        self.root.ids["moeda2"]#.text = f"Ethereum R$ {self.pegar_cotacao('ETH')}"
        self.root.ids["moeda3"]#.text = f"Solana R$ {self.pegar_cotacao('SOL')}"
        self.root.ids["moeda4"]#.text = f"XRP R$ {self.pegar_cotacao('XRP')}"
        self.root.ids["moeda5"]#.text = f"Dogecoin R$ {self.pegar_cotacao('DOGE')}"

    cotacao_boxes = {
        'BTC': 'box_bitcoin',
        'ETH': 'box_ethereum',
        'SOL': 'box_solana',
        'XRP': 'box_xrp',
        'DOGE': 'box_dogecoin'
    }


    def mostrar_cotacao(self, moeda):
        box_id = self.cotacao_boxes.get(moeda)
        if not box_id:
            return
        
        box_moeda = self.root.ids[box_id]
        label_moeda = self.root.ids[f'label_{moeda.lower()}']
        
        if box_moeda.height > 50:
            label_moeda.text = ''

            anim_box = Animation(height=50, duration=0.2)
            anim_label = Animation(height=0, duration=0.2)
            anim_box.start(box_moeda)
            anim_label.start(label_moeda)

        else:
            cotacao = self.pegar_cotacao(moeda)
            
            anim_label = Animation(height=50, duration=0.2)
            anim_box = Animation(height=100, duration=0.2)
            def animacao_completa(instance, value):
                label_moeda.text = f"R$ {cotacao}"
            
            anim_box.bind(on_complete=animacao_completa)    
            anim_label.start(label_moeda)
            anim_box.start(box_moeda)
    # cria o app
    def build(self):
        pass

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao

if __name__ == '__main__':
    Aplicativo().run()