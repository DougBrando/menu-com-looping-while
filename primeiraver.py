# Solicita ao usuário que escolha dois números inteiros
n1 = int(input('Escolha um numero: '))
n2 = int(input('Escolha um numero: '))
opt = 0  # Inicializa a variável opt para armazenar a opção escolhida pelo usuário

# Loop que continua até que o usuário escolha a opção 5 (sair do programa)
while opt != 5:
    # Exibe o menu de opções para o usuário
    print('''
    [ 1 ] somar
    [ 2 ] maior
    [ 3 ] multiplicar
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    
    # Solicita ao usuário que escolha uma opção
    opt = int(input('qual sua opção: '))

    # Se a opção escolhida for 1, realiza a soma dos dois números
    if opt == 1:
        print('{}'.format(n1 + n2))  # Exibe o resultado da soma
    # Se a opção escolhida for 2, determina qual número é maior
    elif opt == 2:
        if n1 > n2:
            print('{} é o maior numero!'.format(n1))  # Exibe n1 se for maior
        else:
            print('{} é o maior numero!'.format(n2))  # Exibe n2 se for maior ou se forem iguais
    # Se a opção escolhida for 3, realiza a multiplicação dos dois números
    elif opt == 3:
        print('{}'.format(n1 * n2))  # Exibe o resultado da multiplicação
    # Se a opção escolhida for 4, solicita novos números ao usuário
    elif opt == 4:
        n1 = int(input('Escolha um numero: '))  # Solicita um novo valor para n1
        n2 = int(input('Escolha um numero: '))  # Solicita um novo valor para n2
    # Se a opção escolhida for maior que 5, exibe uma mensagem de erro
    elif opt > 5:
        print('digite um numero valido')  # Informa que a opção é inválida

# Exibe uma mensagem de fim de programa quando o loop é encerrado
print('fim do programa')
