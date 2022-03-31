from config import *

class Casa (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formato = db.Column(db.String(254))
    
    def __str__(self):
        return f'Casa: {self.formato}'
        
class Quarto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    dimensoes = db.Column(db.String(254))

    casa_id = db.Column(db.Integer, db.ForeignKey(Casa.id), 
                          nullable=False)
    casa = db.relationship("Casa")

    def __str__(self):
        s = f'Quarto: {self.nome}, {self.dimensoes}, em: {str(self.casa)}'          
        return s

class Mobilia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    funcao = db.Column(db.String(254))
    material = db.Column(db.String(254))

    quarto_id = db.Column(db.Integer, db.ForeignKey(Quarto.id),
    nullable=True)

    quarto = db.relationship("Quarto")

    def __str__(self):
        s = f"Mobilia: {self.nome}, Função: {self.funcao}, Material: {self.material}"
        if self.quarto_id:
            s += f", {str(self.quarto)}"
        return s


if __name__ == "__main__": # teste das classes
    
    if os.path.exists(arquivobd): # se houver o arquivo...
        os.remove(arquivobd) # ...apagar!

    db.create_all() # criar tabelas

    print("*** TESTE criando objetos")

    c1 = Casa(formato="Germânica") # cria uma casa

    # persiste para criar o id
    db.session.add(c1)
    db.session.commit()

    #print(c1) # exibir atributos da casa

    q1 = Quarto(nome="Sala", dimensoes="6x5 metros", casa=c1)
    q2 = Quarto(nome="Banheiro", dimensoes="3x4 metros", casa=c1)
    
    db.session.add(q1)
    db.session.add(q2)
    db.session.commit()

    #print(q1, q2)

    m1 = Mobilia(nome="Mesa", funcao="colocar coisas", material="Madeira", quarto=q1)
    m2 = Mobilia(nome="Sofa", funcao="u", material="m", quarto=q1)
    m3 = Mobilia(nome="Mesa denovo", funcao="u2", material="m2", quarto=q1)
    m4 = Mobilia(nome="teste", funcao="teste", material="teste", quarto=q2)

    db.session.add(m1)
    db.session.add(m2)
    db.session.add(m3)
    db.session.add(m4)
    db.session.commit()

    #print(m1)

    print("*** TESTE com todos os dados")
    #print(c1) # casa
    # quartos da casa, sem lista reversa
    #for q in db.session.query(Quarto).filter(Quarto.casa_id == c1.id).all():
    #    print(q)
    for m in db.session.query(Mobilia).filter(Mobilia.quarto_id == q1.id).all():
        print(m)