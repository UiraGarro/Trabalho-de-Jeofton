class Calculadora:
    def soma(n1, n2):
        soma = n1 + n2
        return soma
    
    def subtração(n1, n2):
        subtração = n1 - n2
        return subtração
    
    def multiplicação(n1, n2):
        multiplicação = n1 * n2
        return multiplicação
    
    def divisão(n1, n2):
        if n2 == 0:
            return "Erro: Nõo é possível dividir por zero."
        divisão = n1 / n2
        return divisão
    def média(n1, n2):
        média = (n1 + n2) / 2
        return média
    
    def potenciação(n1, n2):
        potenciação = n1 ** n2
        return potenciação
    
    def radiciação(n1):
        raiz = n1 ** (1/2)
        return raiz
    
while True:
    print("Bem-vindo(a) à Calculadora!")
    print("""Selecione uma operação:
    1. Soma
    2. Subtração
    3. Multiplicação
    4. Divisão
    5. Média
    6. Potenciação
    7. Radiciação"
    8. Mostrar histórico de operações
    9. Limpar histórico de operações""")
    histórico = []