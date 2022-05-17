class Analisador(object):
    def __init__(self):
        self.carteiras = []

    def adicionarCarteira(self, carteira):
        self.carteiras.append(carteira)

    def analisar(self):
        for carteira in self.carteiras:
            carteira.resumo()

