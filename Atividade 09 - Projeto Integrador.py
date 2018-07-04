
"""
Ester Pereira Martins
Atividade 09 - Projeto Integrador

"""
# Olá. Neste exercício do projeto integrador, vamos praticar algumas habilidades básicas em Python. 
# 1) Crie uma lista com 100 números gerados aleatoriamente. Use o módulo numpy para criar os dados que você precisa. Atribua a lista a um objeto nomeado.
import numpy as np
import pandas as pd
numeros = np.random.normal(size=100)

# 2) Apresente o maior número, o menor número, a média do vetor, o desvio padrão e a variância.
numeros.max()
2.5299553763512552
numeros.min()
-2.231004767326251
numeros.mean()
0.1675606937975938
numeros.std()
0.955661691351401
numeros.var()
0.9132892683166205

# 3) Apresente os mesmos resultados só que agora, construa uma frase que será apresentada no console.
print(f'A média do vetor numérico é {round(numeros.mean(), 2)}')
0.17
print(f'O valor máximo do vetor numérico é {round(numeros.max(), 2)}')
2.53
print(f'O valor mínimo do vetor numérico é {round(numeros.min(), 2)}')
-2.23
print(f'O desvio padrão do vetor numérico é {round(numeros.mean(), 2)}')
0.17
print(f'A variância do vetor numérico é {round(numeros.var(), 2)}')
0.91

# 4) Construa um for loop para iterar entre todos os números do vetor. Exiba o número no console se ele for maior do que 0.
print(numeros[[i for i in numeros > 0]])
[0.25728436 0.8427339  0.24494973 0.54387602 0.19677132 1.28233389
 0.58905193 0.40109755 0.22537827 1.40163116 1.01015078 1.71446014
 1.70535708 1.37696236 0.18300297 1.6244282  0.81719013 0.30692953
 2.52995538 0.98859614 0.4402601  0.55448146 1.7328954  0.27323913
 0.7903621  0.28971998 0.46207991 1.26332744 0.63259385 2.50382265
 0.11260387 0.77885376 1.15830006 0.47326571 0.28054843 0.83590286
 0.52004921 0.30831558 0.02609702 0.16345189 0.82090759 0.35292882
 1.06533466 0.32514104 2.27495371 0.89425992 0.08616184 1.24845658
 2.03030251 0.89296824 0.06734217 1.22730754 0.86501505 0.41597239
 0.62292337 0.24031642 0.47053146 0.22664752 0.20221807 0.37450451
 0.67506565]

# 5) Faça a mesma coisa usando um loop while.
j = 0
while j < len(numeros):
    if numeros[j] > 0:
        print(numeros[j])
        j += 1
0.25728436 
0.8427339  
0.24494973
0.54387602 
0.19677132 
1.28233389
0.58905193 
0.40109755 
0.22537827 
1.40163116 
1.01015078 
1.71446014
1.70535708 
1.37696236 
0.18300297 
1.6244282  
0.81719013 
0.30692953
2.52995538 
0.98859614 
0.4402601
0.55448146
1.7328954  
0.27323913
0.7903621  
0.28971998 
0.46207991 
1.26332744 
0.63259385 
2.50382265
0.11260387 
0.77885376 
1.15830006 
0.47326571 
0.28054843 
0.83590286
0.52004921 
0.30831558 
0.02609702 
0.16345189 
0.82090759 
0.35292882
1.06533466 
0.32514104 
2.27495371 
0.89425992 
0.08616184 
1.24845658
2.03030251 
0.89296824 
0.06734217 
1.22730754 
0.86501505 
0.41597239
0.62292337 
0.24031642 
0.47053146 
0.22664752 
0.20221807 
0.37450451
0.67506565]
        
# 6) Usando um comando, crie uma lista com números de 0 a 80. Usando um for loop e um loop while, se o número 
# estiver entre 0 e 20, imprima pequeno. Se estiver entre 21 e 40, imprima médio. Se estiver entre 41 e 60, imprima grande. 
# Se estiver entre 61 e 80, imprima "Que isso, meu?". Se o número for igual à sua idade, imprima na tela "Te peguei!".
lista = list(range(81))

for i in lista:
    if i <= 20:
        print('Pequeno')
    elif i > 20 and i <= 40:
        print('Médio')
    elif i > 40 and i <= 60:
        print('Grande')
    elif i > 60:
        print('Que isso, meu?')
    if i == 25:
        print('Te peguei!')
        
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Pequeno
Médio
Médio
Médio
Médio
Médio
Te peguei!
Médio
Médio
Médio
Médio
Médio
Médio
Médio
Médio
Médio
Médio
Médio
Médio
Médio
Médio
Médio
Grande
Grande
Grande
Grande
Grande
Grande
Grande
Grande
Grande
Grande
Grande
Grande
Grande
Grande
Grande
Grande
Grande
Grande
Grande
Grande
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?
Que isso, meu?       
        

i = 0
while i < len(lista):
    if i <= 20:
        print('Pequeno')
    elif i > 20 and i <= 40:
        print('Médio')
    elif i > 40 and i <= 60:
        print('Grande')
    elif i > 60:
        print('Que isso, meu?')
    if i == 25:
        print('Te peguei!')
    i += 1
    
    
# 7) Crie um dicionário. As chaves serão os nomes de 5 pessoas e os valores, suas idades. Usando um for loop, imprima os pares chave, valor.
dict = {'Ester': 19,
      'Ana': 25,
      'Sarah': 26,
      'Joao': 16,
      'Miguel': 41}
for x, y in dict.items():
    print(x, y)
    
Ester 19
Ana 25
Sarah 26
Joao 16
Miguel 41
    
# 8) Usando um for loop, mostre quem é a pessoa mais velha e a pessoa mais nova no dicionário.
for x, y in dict.items():
    if y == max(dict.values()):
        print(f'{x} é a pessoa mais velha, essa pessoa tem {y} anos.')
    if y == min(dict.values()):
        print(f'{x} é a pessoa mais nova, essa pessoa tem {y} anos.')    
    
Joao é a pessoa mais nova, essa pessoa tem 16 anos.
Miguel é a pessoa mais velha, essa pessoa tem 41 anos.   
    
    
    
    
    
    