'''1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);



Ao final do processamento, qual será o valor da variável SOMA?


'''
print('EXERCICIO 1')

k: int = 0
indice: int = 13
soma: int = 0
while(k < indice):
    k = k + 1
    soma = soma + k
print(soma)

# SOMA = 91

'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

'''

print('-----------------------')
print('EXERCICIO 2')

def fibo(n):
    if (n < 2):
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def pertence(num):
    for i in range(num):
        if (num == fibo(i)):
            print('Pertence')
            break
        else:
            if (i == num):
                print('Não Pertence')

numRecebido = int(input('Digite um número: '))
pertence(numRecebido)

# ENTRADA = 4
# SAIDA = 'Não Pertence'

'''
3) Descubra a lógica e complete o próximo elemento:



a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____
'''

# RESPOSTAS

#  a) 9
#  b) 128
#  c) 49
#  d) 100
#  e) 13
#  f) 200

'''4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. 
O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e 
o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. 
Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?

IMPORTANTE:

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)

c) Explique como chegou no resultado.
'''
# Partindo do ponto de referência sendo o cruzamento, ambos estarão na mesma distância.
'''

5) Escreva um programa que inverta os caracteres de um string.



IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;'''

palavra = input('Digite uma palavra: ')

arrayPalavra = list(palavra)
print(arrayPalavra[::-1])

# ENTRADA : 'OITO'
# SAIDA : 'OTIO'