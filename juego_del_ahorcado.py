
import random
import sys
from webbrowser import get

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

# Funcion para leer la informacion
with open("./archivos/data.txt", "r", encoding="utf-8") as f:

    list_words = [i.rstrip("\n") for i in f]


secret_word = random.choice(list_words)
correct_letters = [i for i in secret_word]
missed_letters = []
letter = input('Escribe algo: ')

if letter in correct_letters:
    print('Esta')
else:
    print('No esta') 


blank = ['_']*len(secret_word)

print(''.join(blank))
for i in range(len(secret_word)):
    if secret_word[i] in correct_letters:
        blank[i] == secret_word[i]





