import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Quer rolar o dado? '
        # Layout
        self.layout = [ 
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('não')]
        ]

                
    def Iniciar(self):
        # Janela
        self.janela = sg.Window('Simulador de Dado', layout = self.layout)

        # ler valores
        self.eventos, self.valores = self.janela.Read()
        # usar os dados

       
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
                #Lembrar de fazer a tela de exibição do número do dado
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Então pq tu iniciou o programa? BABACA!')
            else:
                print('Digite sim ou não')
                simulador.Iniciar()
        except:
            print('Ocorreu um erro. Chame o dev porco que fez esse programa!')

    def GerarValorDoDado(self):

       print(random.randint(self.valor_minimo, self.valor_maximo))
        
simulador = SimuladorDeDado()
simulador.Iniciar()