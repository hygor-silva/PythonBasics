import random

class ChuteUmNumero:
    def __init__(self):
        self.valor = 0
        self.valorMinimo = 1
        self.valorMaximo = 100
        self.tentativa = True
    
    def Iniciar(self):
        self.GerarValor()
        self.PedirValor()

        try:
            while self.tentativa == True:
                if int(self.chute) > self.valor:
                    print('Tente um número menor')
                    self.PedirValor()
                elif int(self.chute) < self.valor:
                    print('Tente um número maior')
                    self.PedirValor()
                else:
                    print('Acertô Mizeravi!')
                    self.tentativa = False
        except:
            print('Favor digitar apenas números')
            self.Iniciar()

    def PedirValor(self):
        self.chute = input('Chute um número')
        
    def GerarValor(self):
        self.valor = random.randint(self.valorMinimo, self.valorMaximo)

chute = ChuteUmNumero()
chute.Iniciar()

