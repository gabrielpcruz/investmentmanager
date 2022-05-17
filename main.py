from classes.carteira_fundos import CarteiraFundos
from classes.carteira_acoes import CarteiraAcoes
from classes.analisador import Analisador

carteiraFundos = CarteiraFundos(['BCFF11', 'BBRC11', 'MXRF11'])
carteiraAcoes = CarteiraAcoes(['VIIA3', 'MGLU3'])

carteiraFundos.atualizar()
carteiraAcoes.atualizar()


analisador = Analisador()
analisador.adicionarCarteira(carteiraFundos)
analisador.adicionarCarteira(carteiraAcoes)

analisador.analisar()
