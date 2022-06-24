from numpy import diag


class Ingresso:
    def __init__(self, id, sessao, informacao, datetime):
        self.id = id
        self.sessao = sessao
        self.informacao = informacao
        self.datetime = datetime

