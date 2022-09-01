# Quanto tempo você leva para escrever seu nome.

import time

def cont_tempo():
    inicio = time.perf_counter()
    input('Escreva seu nome: ')
    fim = time.perf_counter()
    tempo = round(fim - inicio, 1)
    print('Você levou ' + str(tempo) + ' segundos para escrever seu nome')

cont_tempo()