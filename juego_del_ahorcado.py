
import random
import sys
import os

def clear():
    os.system('clear')


# Funcion para leer la informacion
def read_data():
    with open("./archivos/data.txt", "r", encoding="utf-8") as file:
        data = [i.rstrip("\n") for i in file]

    dict_data = {key:value for key, value in enumerate(data)}
    return dict_data


def run():
    dict_data = read_data()
    secret_word = random.choice(dict_data)
    print(secret_word)

if __name__ == '__main__':
    run()







"""
secret_word = random.choice(list_words)
correct_letters = [i for i in secret_word]
missed_letters = []

print(secret_word)
if letter in correct_letters:
    print('Esta')
else:
    print('No esta') 


letter = input('Escribe algo: ')

blank = ['_']*len(secret_word)

print(''.join(blank))
for i in range(len(secret_word)):
    if secret_word[i] in correct_letters:
        blank[i] == secret_word[i]


for i in correct_letters:
    if letter == i:
        print(letter)



"""
