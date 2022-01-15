from ntpath import join
from operator import index


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


palabra = 'rosa'
letter_completed = ['_']*len(palabra)

letter_of_word = [i for i in palabra]

print(letter_of_word)

#while letter_of_word == letter_completed:


while letter_of_word != letter_completed:
    letter = str(input('Ingresa una letra: '))

    for i in letter_of_word:

        if letter == i:
            letter_completed[letter_of_word.index(i)] = i
            print(letter_completed)    



#    if letra in letter_of_word:


#        print(' '.join(blank))


#        print(letter_of_word.index(letra))
#        blank.insert(letter_of_word.index(letra),letra)
#        print(blank)
#        letter_of_word.remove(letra)