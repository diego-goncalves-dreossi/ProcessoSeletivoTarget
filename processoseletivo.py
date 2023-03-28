def questao1():
    # While Indice K
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K = K + 1
        SOMA += K

    print(SOMA)

def questao2(numero):
    #Fibonacci
    fibonacci = [0,1,1]
    pronto = False
    
    while not pronto:
        n = fibonacci[-2] + fibonacci[-1]
        if n > numero:
            pronto = True
        else:
            fibonacci.append(n)


    

    if numero in fibonacci:
        print(f'Número {numero} pertence a sequência de Fibonacci')
    else:
        print(f'Número {numero} não pertence a sequência de Fibonacci')

def questao3():
    print('a) ... 9')
    print('b) ... 128')
    print('c) ... 49')
    print('d) ... 100')
    print('e) ... 13')
    print('f) ... 200')

def questao4(distancia, vcarro, vcaminhao, pausacarro, pausacaminhao):
    # 
    # Pausa em minutos
    """
    Para chegar ao resultado eu calculei a distancia percorrida por cada veículo, o ponto em que se encontram é o ponto em que a soma dos percursos é mais ou menos igual a distancia entre RP e Franca.
    Troquei km/hr por km/min para poder incluir as pausas do pedágio.
    Os percursos foram calculados em um loop, cada interação é um minuto e vai se somando ao valor total, que é iniciado subtraindo o que se andaria nas pausas do pedágio.
    """
    percurso_carro = -pausacarro * vcarro
    percurso_caminhao = -pausacaminhao * vcaminhao
    pronto = False
    i = 1
    

    while not pronto:
        percurso_carro += vcarro
        percurso_caminhao += vcaminhao
      
        i += 1
        if (percurso_caminhao + percurso_carro) >= distancia:
            pronto = True
        
    print('Percurso do carro:',percurso_carro,'Percurso do caminhão:',percurso_caminhao)
    print('O caminhão está mais perto de RP, já que ele não precisa seguir para Franca para chegar em RP.')

    
def questao5(palavra):
    palavra = str(palavra).strip()
    nova = ''
    if palavra == '':
        print('String vazia inserida')
    else:
        tam = len(palavra)
        i = 1

        while i <= tam:
            nova += palavra[-i]
            i += 1
        print(palavra,nova)

print('-- Questão 1')
questao1() #91
print('-- Questão 2')
questao2(34)
print('-- Questão 3')
questao3()
print('-- Questão 4')
questao4(100,1.83,1.3,0,5)
print('-- Questão 5')
questao5('ola')