def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

numero = int(input("Digite um número inteiro: "))

resultado = verificar_par_impar(numero)
print(f"O número {numero} é {resultado}.")