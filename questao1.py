# Informações estão no Readme.

numeros = []
i = 0

while i < 4:
    numeros.append(int(input("Digite um número inteiro:")))
    i += 1

alvo = int(input("Digite o alvo da soma:"))


def somando_numeros(numeros, alvo):
    i = 0
    j = len(numeros) - 1

    while i < j:
        if numeros[i] + numeros[j] == alvo:
            print("A Soma de ", numeros[i], numeros[j], " resulta em", alvo,)
            return True
        elif numeros[i] + numeros[j] < alvo:
            i += 1
        else:
            j -= 1
    return False

print(somando_numeros(numeros, alvo))
