class Calculadora:
    
    @staticmethod
    def soma(n1, n2):
        return n1 + n2

    @staticmethod
    def subtracao(n1, n2):
        return n1 - n2

    @staticmethod
    def multiplicacao(n1, n2):
        return n1 * n2

    @staticmethod
    def divisao(n1, n2):
        if n2 == 0:
            return "Erro: Não é possível dividir por zero."
        return n1 / n2

    @staticmethod
    def media(n1, n2):
        return (n1 + n2) / 2

    @staticmethod
    def potenciacao(n1, n2):
        return n1 ** n2

    @staticmethod
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
    8. Mostrar histórico de operações
    9. Limpar histórico de operações""")


def main():
    historico = []

    operacoes = {
        '1': Calculadora.soma,
        '2': Calculadora.subtracao,
        '3': Calculadora.multiplicacao,
        '4': Calculadora.divisao,
        '5': Calculadora.media,
        '6': Calculadora.potenciacao,
        '7': Calculadora.radiciacao,
    }

    while True:
        exibir_menu()
        escolha = input("Digite sua escolha (1/2/3/4/5/6/7/8/9): ")

        if escolha in operacoes:
            try:
                if escolha == '7': 
                    num1 = float(input("Digite o número da raiz: "))
                    resultado = operacoes[escolha](num1)
                    print(f"Raiz de {num1} = {resultado}")
                    historico.append(f"Raiz de {num1} = {resultado}")
                else:
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    resultado = operacoes[escolha](num1, num2)
                    print(f"Resultado: {resultado}")
                    historico.append(f"{num1} e {num2} -> {resultado}")
            except ValueError:
                print("Erro: Entrada inválida. Por favor, insira números válidos.")

        elif escolha == '8':  
            print("Histórico de operações:")
            for operacao in historico:
                print(operacao)

        elif escolha == '9':  
            historico.clear()
            print("Histórico limpo.")

        else:
            print("Escolha uma opção válida.")

        proxima_operacao = input("Nova ação? (s/n): ").lower()
        if proxima_operacao != 's':
            break


if __name__ == "__main__":
    main()