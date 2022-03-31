from casa import Casa

class Quarto:

    def __init__(self, nome: str, dimensao: str, casa: Casa):
        self.nome = nome
        self.dimensao = dimensao
        self.mobilias = []
        if casa is None:
            raise Exception("O quarto deve pertencer a alguma casa.")
        self.casa = casa
        #if mobilias is not None:
        #   self.mobilias.append(mobilias)
    
    def __repr__(self):
        return str(self.nome) + "," + str(self.dimensao)

#if __name__ == "__main__":
    #q = Quarto("sala", "6x4")
    #m = Mobilia("armario", "guardar", "madeira")
    #c = Casa("Normal")