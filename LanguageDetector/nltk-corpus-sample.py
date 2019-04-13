import nltk

from nltk.corpus import stopwords
from nltk import word_tokenize

print(stopwords.words('english')[0:3])
print(len(stopwords.words('english')))
print()
print(stopwords.words('french')[0:3])
print(len(stopwords.words('french')))
print()
print(stopwords.words('german')[0:3])
print(len(stopwords.words('german')))
print()
print(stopwords.words('spanish')[0:3])
print(len(stopwords.words('spanish')))

english= "A pencil is an implement for writing or drawing, constructed of a narrow, solid pigment core in a protective casing that prevents the core from being broken and/or marking the user’s hand. Pencils create marks by physical abrasion, leaving a trail of solid core material that adheres to a sheet of paper or other surface. They are distinct from pens, which dispense liquid or gel ink onto the marked surface."

french = "Un crayon est un instrument de dessin et d'écriture. Il est constitué d'une petite baguette servant de gaine à une mine de la même longueur, l'extrémité de la baguette étant parfois recouverte d'une gomme à effacer. Lorsque la mine est usée, on taille le bois en maintenant la forme conique de l’extrémité, de manière à dégager une nouvelle longueur de mine, au moyen d’un canif ou d’un taille-crayon ou d'un bouton à retour sur certains types de crayon à mine rechargeable."

german = "Ein Bleistift ist ein Schreibgerät mit einer Mine, die in einem Schaft eingebettet ist. Der bis ins späte 18. Jahrhundert zur Herstellung der Mine verwendete Graphit wurde irrtümlich für das Bleierz Galenit (Bleiglanz) gehalten. Die sich daraus ergebende Bezeichnung „Bleistift“ (umgangssprachlich auch manchmal Bleier) hat bis heute überdauert. Seit dem 19. Jahrhundert wird die Mine aus einem Graphit-Ton-Gemisch gebrannt. Der Schaft wird in der Regel aus Holz gefertigt, häufig aus dem Zedernholz genannten Holz des Virginischen Wacholders. Geläufig sind auch Druckbleistifte und Fallminenstifte mit Kunststoff- oder Metallmantel."

spanish = "Un lápiz o lapicero1​ es un instrumento de escritura o de dibujo. Consiste en una mina o barrita de pigmento (generalmente de grafito y una grasa o arcilla especial. También puede ser pigmento coloreado de carbón de leña) y encapsulado generalmente en un cilindro de madera fina, aunque también en envolturas plásticas, de papel y metal."

english_token = nltk.word_tokenize(english)
spanish_token = nltk.word_tokenize(spanish)
print(english_token)

