import random

print('---------------jogo da senha---------------')

digitosenha1 = random.randint(0,9)
digitosenha2 = random.randint(0,9)
digitosenha3 = random.randint(0,9)
digitosenha4 = random.randint(0,9)

print()
print('tente advinhar a senha')
resposta0=int(input('digite 4 digitos entre'))
if resposta0 == digitosenha1:
    print(digitosenha1, end='')
else:
    print('*', end='')

print('tente advinhar a senha')
resposta1=int(input('digite o segundo digito:'))
if resposta1 == digitosenha1:
    print(digitosenha1, end='')
else:
    print('*', end='')

print('tente advinhar a senha')
resposta2=int(input('digite o terceiro digito:'))
if resposta2 == digitosenha1:
    print(digitosenha1, end='')
else:
    print('*', end='')

print('tente advinhar a senha')
resposta3=int(input('digite o quarto digito:'))
if resposta3 == digitosenha1:
    print(digitosenha1, end='')
else:
    print('*', end='')