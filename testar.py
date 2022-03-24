from quarto import Quarto
from mobilia import Mobilia
from casa import Casa

c = Casa("Normal")
q = Quarto("sala", "6x4", c)
m = Mobilia("armario", "guardar", "madeira")
m2 = Mobilia("sofa", "sentar", "madeira e espuma", q)

print(c, q, m, m2)