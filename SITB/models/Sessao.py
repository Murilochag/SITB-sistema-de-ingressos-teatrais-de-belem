from msilib.schema import Class


class Sessao:
    def __init__(self, id, teatro, show , data, hora):
        self.id = id
        self.teatro = teatro
        self.show = show
        self.data = data
        self.hora = hora
