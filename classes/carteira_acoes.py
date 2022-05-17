import os
from classes.carteira import Carteira


class CarteiraAcoes(Carteira):
    def __init__(self, tickers):
        super().__init__(
            tickers,
            'https://statusinvest.com.br/acoes/',
            f"{os.sep}data{os.sep}acoes{os.sep}info",
            "div[title='Valor atual do ativo'] > strong"
        )
