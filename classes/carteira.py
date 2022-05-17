import time
import datetime
import os

from classes.ativo import Ativo
from classes.searcher import Searcher
from bs4 import BeautifulSoup
from classes.utils import get_project_root


class Carteira(object):
    def __init__(self, tickers, url_searcher, path_scrapping, selector):
        self.tickers = tickers
        self.ativos = []
        self.searcher = Searcher(url_searcher)
        self.path_scrapping = path_scrapping
        self.__carregarAtivos()
        self.selector = selector
        self.root_path = get_project_root()

    def __carregarAtivos(self):
        for ticker in self.tickers:
            self.ativos.append(Ativo(ticker))

    def atualizar(self):
        for ativo in self.ativos:
            precisa_coletar = self.precisa_coletar(ativo.ticker)

            if precisa_coletar:
                print(f"Atualizando... ({ativo.ticker})")
                time.sleep(5)
                self.coletar(ativo.ticker)

    def coletar(self, ativo):
        request = self.searcher.search(ativo)

        filepath = f"{self.root_path}{os.sep}{self.path_scrapping}{os.sep}{ativo}.txt"

        with open(filepath, 'w', encoding="utf-8") as f:
            f.write(request.text)

    def precisa_coletar(self, ativo):
        pathfile = f"{self.root_path}{os.sep}{self.path_scrapping}{os.sep}{ativo}.txt"

        if not os.path.exists(pathfile):
            return True

        today = datetime.date.today().strftime("%Y-%m-%d")
        filemodify = datetime.date.fromtimestamp(os.path.getmtime(pathfile)).strftime("%Y-%m-%d")

        return not today.__eq__(filemodify)

    def get_ativos(self):
        return self.ativos

    def resumo(self):
        for ativo in self.ativos:
            contents = open(f"{self.root_path}{os.sep}{self.path_scrapping}{os.sep}{ativo.ticker}.txt", "r",
                            encoding="utf-8").read()
            bs4 = BeautifulSoup(contents, 'html.parser')
            tag_valor = bs4.select(self.selector)

            for valor in tag_valor:
                preco = valor.text.strip().replace("R$ ", "")

                print(f"{ativo.ticker}: R$ {preco}")
