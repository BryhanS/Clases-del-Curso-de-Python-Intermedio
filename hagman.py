HAGMAN_PICS = [
[r"""
  +--+
  |  |
     |
     |
     |
     |
  =====""",

 r"""
  +--+
  |  |
  O  |
     |
     |
     |
  =====""",
 r"""
  +--+
  |  |
  O  |
  |  |
     |
     |
 =====""",
 r"""
  +--+
  |  |
  O  |
 /|  |
     |
     |
 =====""",
 r"""
  +--+
  |  |
  O  |
 /|\ |
     |
     |
=====""",
 r"""
   +--+
  |  |
  O  |
 /|\ |
 /   |
     |
 =====""",
 r"""
  +--+
  |  |
  O  |
 /|\ |
 / \ |
     |
 ====="""]
]


palabra_adivinar = {'rosa'}
palabra_adivinando = len(palabra_adivinar)* '-'

print(list(palabra_adivinando))

while palabra_adivinar != palabra_adivinando:
    print(palabra_adivinando)
    letra = input("Ingresa una letra: ")
    if letra in palabra_adivinar:
        palabra_adivinando = list(palabra_adivinando)
        for i, x in enumerate(palabra_adivinar):
            if x == letra:
                palabra_adivinando[i] = x
            palabra_adivinando = ''.join(palabra_adivinando)