import os
from classes.carteira import Carteira


class CarteiraFundos(Carteira):
    def __init__(self, tickers):
        super().__init__(
            tickers,
            'https://www.fundsexplorer.com.br/funds/',
            f"{os.sep}data{os.sep}fundos{os.sep}info",
            "span.price"
        )


