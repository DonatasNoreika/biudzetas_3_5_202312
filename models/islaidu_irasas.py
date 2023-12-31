from models.irasas import Irasas

class IslaiduIrasas(Irasas):
    def __init__(self, suma, budas, isigyta, info):
        super().__init__(suma)
        self.budas = budas
        self.isigyta = isigyta
        self.info = info

    def __str__(self):
        return f"Išlaidos: {self.suma} ({self.budas}, {self.isigyta}, {self.info})"

    def __repr__(self):
        return f"Išlaidos: {self.suma} ({self.budas}, {self.isigyta}, {self.info})"