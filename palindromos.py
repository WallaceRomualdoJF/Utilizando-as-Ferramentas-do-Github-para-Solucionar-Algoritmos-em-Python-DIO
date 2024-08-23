palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

palavra = palavra.lower()

palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")



