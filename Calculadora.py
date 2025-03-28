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
    
    try:
        escolha = input("Digite sua escolha (1/2/3/4/5/6/7/8): ")
    
        if escolha in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if escolha == '7':
                num1 = float(input("Digite seu número: "))
                num2 = 0
                print(f"Raiz de {num1} = {Calculadora.radiciação(num1)}")
                histórico.append(Calculadora.radiciação(num1))
                
            if escolha == '8':
                print(histórico)
                
            elif escolha == '9': histórico.clear()
            else:
                num1 = float(input("Digite seu primeiro número: "))
                num2 = float(input("Digite seu segundo número: "))
                
            
                if escolha == '1':
                    print(f"{num1} + {num2} = {Calculadora.soma(num1, num2)}")   
                    histórico.append(Calculadora.soma(num1, num2))
                elif escolha == '2':
                    print(f"{num1} - {num2} = {Calculadora.subtração(num1, num2)}")
                    histórico.append(Calculadora.subtração(num1, num2))
                
                elif escolha == '3':
                    print(f"{num1} * {num2} = {Calculadora.multiplicação(num1, num2)}")
                    histórico.append(Calculadora.multiplicação(num1, num2))
                
                elif escolha == '4':
                    print(f"{num1} / {num2} = {Calculadora.divisão(num1, num2)}")
                    histórico.append(Calculadora.divisão(num1, num2))
                
                elif escolha == '5':
                    print(f"Média de {num1} e {num2} = {Calculadora.media(num1, num2)}")
                    histórico.append(Calculadora.media(num1, num2))
                    
                elif escolha == '6':
                    print(f"{num1} ^ {num2} = {Calculadora.potencia(num1, num2)}")
                    histórico.append(Calculadora.potencia(num1, num2))    
            
        else:
            print("Escolha uma opção válida")
            
    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira números válidos.")    
        
    proxima_operação = input("Tentar Novamente? (s/n): ")
    if proxima_operação.lower() != 's':
            break