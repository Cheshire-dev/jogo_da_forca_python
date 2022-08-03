import time
import os

game_over = False
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letra = ''
palavra = ''
palavra_escondida = ''

os.system('cls')

palavra = input('Digite uma palavra:')

for i in range(0, len(palavra)):
    print(i)
    palavra_escondida += '-'


for letra_palavra in range(0,len(palavra)):
    print(letra_palavra)
        