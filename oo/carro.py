"""Voce deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:

1) Motor
2) Direcao

O Motor tera a responsabilidade de contralar a velocidade
Ele oferece os seguints atributos:
1) Atributo de dado velocidade
2) Metodo acelerar, que devera incrementar a velocidade de uma unidade
3) Metodo frear que devera decrementar a velocidade em duas unidades

A Direcao tera a responsabilidade de controlar a direcao
Ela oferece os seguintes atributos:
1) Valor da direcao com valores possiveis: Norte, Sul, Leste, Oeste
2) Metodo girar_a_direita
3) Metodo girar_a_esquerda

    N
O       L
    S

Exemplo:
>>>#testando motor
>>>motor = Motor()
>>>motor.velocidade
0
>>>motor.acelerar()
>>>motor.velocidade
1
>>>motor.acelerar()
>>>motor.velocidade
2
>>>motor.acelerar()
>>>motor.velocidade
3
>>>motor.frear()
>>>motor.velocidade
1
>>>motor.frear()
>>>motor.velocidade
0

>>>#testando direcao
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Norte'
>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
'Leste'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Oeste'

"""