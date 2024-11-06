def obter_numero_inteiro(prompt):
    """Função para obter um número inteiro do usuário com tratamento de exceção."""
    while True:
        try:
            return int(input(prompt))  # Solicita um número inteiro ao usuário
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")  # Mensagem de erro para entradas inválidas

def exibir_menu():
    """Função para exibir o menu de opções."""
    print('''
    [ 1 ] Somar
    [ 2 ] Maior
    [ 3 ] Multiplicar
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')

def main():
    # Solicita ao usuário que escolha dois números inteiros
    n1 = obter_numero_inteiro('Escolha um número: ')
    n2 = obter_numero_inteiro('Escolha outro número: ')
    opt = 0  # Inicializa a variável opt para armazenar a opção escolhida pelo usuário

    # Loop que continua até que o usuário escolha a opção 5 (sair do programa)
    while opt != 5:
        exibir_menu()  # Exibe o menu de opções
        opt = obter_numero_inteiro('Qual sua opção: ')  # Solicita ao usuário que escolha uma opção

        # Se a opção escolhida for 1, realiza a soma dos dois números
        if opt == 1:
            print('Resultado da soma: {}'.format(n1 + n2))  # Exibe o resultado da soma
        # Se a opção escolhida for 2, determina qual número é maior
        elif opt == 2:
            maior = n1 if n1 > n2 else n2  # Usa uma expressão condicional para determinar o maior
            print('{} é o maior número!'.format(maior))  # Exibe o maior número
        # Se a opção escolhida for 3, realiza a multiplicação dos dois números
        elif opt == 3:
            print('Resultado da multiplicação: {}'.format(n1 * n2))  # Exibe o resultado da multiplicação
        # Se a opção escolhida for 4, solicita novos números ao usuário
        elif opt == 4:
            n1 = obter_numero_inteiro('Escolha um número: ')  # Solicita um novo valor para n1
            n2 = obter_numero_inteiro('Escolha outro número: ')  # Solicita um novo valor para n2
        # Se a opção escolhida for inválida
        elif opt < 1 or opt > 5:
            print('Digite um número válido entre 1 e 5.')  # Informa que a opção é inválida

    # Exibe uma mensagem de fim de programa quando o loop é encerrado
    print('Fim do programa')

# Chama a função principal para executar o programa
if __name__ == "__main__":
    main()
