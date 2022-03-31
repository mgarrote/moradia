from quarto import Quarto

class Mobilia:

    def __init__(self, nome: str, funcao: str, material: str, quarto = None):
        self.nome = nome
        self.funcao = funcao
        self.material = material
        self.quarto = quarto

    def __repr__(self):
        s = self.nome + "," + self.funcao + "," + self.material 
        if self.quarto:
            st = "," + str(self.quarto.nome)
            s += st
            return s
        return s