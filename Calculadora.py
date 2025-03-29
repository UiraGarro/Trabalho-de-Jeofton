def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        return "Erro: Não é possível dividir por zero."
    return n1 / n2

def media(n1, n2):
    return (n1 + n2) / 2

def potenciacao(n1, n2):
    return n1 ** n2

def radiciacao(n1):
    return n1 ** 0.5

def exibir_menu():
    print("""Bem-vindo(a) à Calculadora!
Selecione uma operação:
    1. Soma
    2. Subtração
    3. Multiplicação
    4. Divisão
    5. Média
    6. Potenciação
    7. Radiciação
    8. Sair""")

def main():
    while True:
        exibir_menu()
        escolha = input("Digite sua escolha (1/2/3/4/5/6/7/8): ")

        if escolha in ['1', '2', '3', '4', '5', '6', '7']:
            try:
                if escolha == '7': 
                    num1 = float(input("Digite o número da raiz: "))
                    resultado = radiciacao(num1)
                    print(f"Raiz de {num1} = {resultado}")
                else:
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    if escolha == '1':
                        resultado = soma(num1, num2)
                    elif escolha == '2':
                        resultado = subtracao(num1, num2)
                    elif escolha == '3':
                        resultado = multiplicacao(num1, num2)
                    elif escolha == '4':
                        resultado = divisao(num1, num2)
                    elif escolha == '5':
                        resultado = media(num1, num2)
                    elif escolha == '6':
                        resultado = potenciacao(num1, num2)
                    print(f"Resultado: {resultado}")
            except ValueError:
                print("Erro: Entrada inválida. Por favor, insira números válidos.")

        elif escolha == '8':
            print("Saindo da calculadora.")
            break

        else:
            print("Escolha uma opção válida.")

if __name__ == "__main__":
    main()