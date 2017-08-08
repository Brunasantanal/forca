# o import é utilizado para importar um arquivo para o outro
import random

palavras = ['abacate','chocolate','paralelepipedo','goiaba']
letrasErradas = ''
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def palavraz():
    global palavras
    while True :
        a = input('Ditige a palavra:')
        if a == "":
           break
        palavras.append(a)

    
#o def é utilizado para criar funçẽs
def principal():
    """
    Função Princial do programa
    """
# empressa na tela oque for(depois do print é claro) escrito entre paretes ou em aspas(abrindo e fexando) 
    print('F O R C A')
    palavraz()

    palavraSecreta = sortearPalavra()
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)
# while true é é utilizado enquanto as 'questoẽs' forem verdadeiras
    while True:
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)

#if e else são comandos de fluxo, ou seja podem mudar a sequencia de execução de um programa.
#O bloco da instrução if será execultado somente quando a condição da instrução for Verdadeira.
#o if serve para colocar mais de uma opção, exemplo: if gosta de goiaba
#if gosta de goiaba e manga ou seja, se gosta de um elemento ou 2 execute tal função 

        if perdeuJogo():
            print('Voce Perdeu!!!')
# break é quebrar, quebra (ou interrompe) o fluxo natural do programa
            break
        if ganhouJogo(palavraSecreta):
            print('  Voce Ganhou  (☞ﾟヮﾟ)☞ !!!')
            break            
        
def perdeuJogo():
# a global serve para informar que a função não está mais disponivel somente para uma comando e sim para o programa inteiro.
    global FORCAIMG
    if len(letrasErradas) == len(FORCAIMG):
#o return encerra a execução da função corrente, voltando exatamente para o ponto onde ela foi chamada.
        return True
#O bloco da instrução else será execultado somente quando a condição da instrução if for Falsa.
#o else é utilizado quando existem 2 opçẽs, ex: existe tal coisa e outra coisa, dando a posibilidade de ser uma verdadeira e outra falsa.
    else:
        return False
    
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True
#for singoifica para, ou seja, para tal função existe tal coisa.
#in significa em, ou seja, para letra em palavraSecreta existem mais alternativas.(está entro de tal coisa)
    for letra in palavraSecreta:
# o not in é a mesma coisa, porem existe o not, que significa não, fazendo com que se caso tal coisa não estiver em tal coisa era tal coisa
        if letra not in letrasCertas:
            ganhou = False 
    return ganhou        
        


def receberPalpite():
# input utilizada para solicidar dados do usuário 
    palpite = input("Adivinhe uma letra: ")
    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
# or significa ou 
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
    else:
        return palpite
    
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
#A função range retorna uma série numérica no intervalo enviado como argumento
#A função len retorna o número de caracteres de uma string
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()

    
principal()
