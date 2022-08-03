from __future__ import barry_as_FLUFL
import time
import os


def boneco():

        print('_____________|')
        print('||-----------|')
        print('||          ( )')
        print('||          /|\ ')
        print('||          / \ ')
        print('||')
        print('||')
        print('-----------')


vidas = 6
game_over = False
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letra = ''
palavra = ''
palavra_escondida = []
cont_letra=0
cont_carac=0
ola = False


os.system('cls')

palavra = input('Digite uma palavra:').lower()

for i in range(0, len(palavra)):
    if palavra[i] == ' ':
        palavra_escondida.append(' ')
    elif palavra[i] == '-':
        palavra_escondida.append('-')
    else:
        palavra_escondida.append('_')

while game_over != True:
    

    os.system('cls')

    palavra_escondida_str = str(' '.join(palavra_escondida))
    print(f'Vidas: {vidas}\n\n')
    print(palavra_escondida_str)
    print('__________________________________________')
    print(str(' ' .join(alfabeto)))
    print('__________________________________________')

    #testa e imprime a derrota na tela
    if vidas == 0:
        print('\n\nVOCÊ ESTÁ ELIMINADO! SUCUMBA!!!!') 
        break

    #testa e imprime a vitória na tela
    if ola == True:
        print('\n\nVocê venceu!!!')
        break
    letra = input('Digite uma letra:')   
    print('__________________________________________')

    for letra_palavra in range(0,len(palavra)):
        if letra == palavra[letra_palavra]:
            palavra_escondida[letra_palavra] = letra
        else:
            cont_letra += 1

    if len(palavra) == cont_letra:
        vidas -= 1

    cont_letra = 0


    #Passagem pela palavra escondida verificando se a pos é diferente de um caracter
    for i in range(0, len(palavra_escondida)):
        #Caso o conteúdo da array não seja os carcteres
        if palavra_escondida[i] != ' ' and palavra_escondida[i] != '-' and palavra_escondida[i] != '_':
            cont_carac += 1

    #Verificando se o tamanho da palavra escondida é igual ao contador
    if len(palavra_escondida) == cont_carac:
        ola = True

    cont_carac = 0

    for letra_alfabeto in range(0,len(alfabeto)):
        print(letra_alfabeto)
        if letra == alfabeto[letra_alfabeto]:
            del(alfabeto[letra_alfabeto])
            break