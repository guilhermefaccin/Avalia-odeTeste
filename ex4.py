import random

numero_secreto = random.randint(1,100)
palpite = 0
tentativas = 0 
while palpite != numero_secreto:
    palpite = int(input('tente adivinhar o numero secreto: '))
    tentativas = tentativas + 1
    if palpite > numero_secreto:
        print ("muito alto!")
    elif palpite < numero_secreto:
        print ('muito baixo!')
print (f'Parabens!! voce acertou em {tentativas} tentativas')
