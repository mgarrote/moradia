class Casa:

    def __init__(self, formato: str):
        self.formato = formato
        self.quartos = []

    def __repr__(self):
        s = self.formato
        for q in self.quartos:
            s += "," + str(q)
        return s