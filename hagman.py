from ntpath import join
from operator import index
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

def insert_letter(player_letter, letter_of_word):
    chances = 0
    for i, letter in letter_of_word.items():
        if player_letter == letter:
            letter_completed[i] = player_letter
        continue
    return letter_completed


palabra = 'casa'
letter_completed = ['_']*len(palabra)

letter_of_word = dict(enumerate([i for i in palabra]))

while palabra != str(''.join(letter_completed)):

    player_letter = str(input('Ingresa una letra: '))
    insert_letter(player_letter, letter_of_word)
    print(' '.join(letter_completed))