from newton_cotes import funcao_geral_integracao

running = True
print("-------------- BEM VINDO AO PROGRAMA --------------")
print("   fórmula base: f(x)=(sen(2x) + 4x^2 + 3x)^2")
print("---------------------------------------------------\n")
while running:
    
    a = input('Qual será o intervalo [a]? ')
    a = int(a)
    b = input('Qual será o intervalo [b]? ')
    b = int(b)
    epsilon = input('Qual será o erro aproximado?\n')
    epsilon = float(epsilon)
    print("              FÓRMULAS DE NEWTON-COTES")
    print("1 - Abordagem aberta")
    print("2 - Abordagem fechada")
    print("0 - Sair do programa")
    approach = input('Qual abordagem você deseja? ')
    approach = int(approach)
    if(approach==1):
        print("\n              Abordagem aberta")
        print("1 - Polinômio de substituição de grau 1")
        print("2 - Polinômio de substituição de grau 2")
        print("3 - Polinômio de substituição de grau 3")
        print("4 - Polinômio de substituição de grau 4")
        print("0 - Sair do programa")
        methodIntegration = input('Com qual polinômio você deseja integrar? ')
        methodIntegration = int(methodIntegration)
        if(methodIntegration == 1):
            grau1 = funcao_geral_integracao(a, b, epsilon, "fechada1")
            print("\n     --------------------------------")
            print("      Resultado: " , grau1[1])
            print("      Interações: " , grau1[0])
            print("     --------------------------------")
        elif(methodIntegration == 2):
            grau2 = funcao_geral_integracao(a, b, epsilon, "fechada2")
            print("\n     --------------------------------")
            print("      Resultado: " , grau2[1])
            print("      Interações: " , grau2[0])
            print("     --------------------------------")
        elif(methodIntegration == 3):
            grau3 = funcao_geral_integracao(a, b, epsilon, "fechada3")
            print("\n     --------------------------------")
            print("      Resultado: " , grau3[1])
            print("      Interações: " , grau3[0])
            print("     --------------------------------")
        elif(methodIntegration == 4):
            grau4 = funcao_geral_integracao(a, b, epsilon, "fechada4")
            print("\n     --------------------------------")
            print("      Resultado: " , grau4[1])
            print("      Interações: " , grau4[0])
            print("     --------------------------------")
    elif(approach==2):
        print("\n              Abordagem fechada")
        print("1 - Polinômio de substituição de grau 1")
        print("2 - Polinômio de substituição de grau 2")
        print("3 - Polinômio de substituição de grau 3")
        print("4 - Polinômio de substituição de grau 4")
        print("0 - Sair do programa")
        methodIntegration = input('Com qual polinômio você deseja integrar? ')
        methodIntegration = int(methodIntegration)
        if(methodIntegration == 1):
            grauAberta1 = funcao_geral_integracao(a, b, epsilon, "aberta1")
            print("\n     --------------------------------")
            print("      Resultado: " , grauAberta1[1])
            print("      Interações: " , grauAberta1[0])
            print("     --------------------------------")
        elif(methodIntegration == 2):
            grauAberta2 = funcao_geral_integracao(a, b, epsilon, "aberta2")
            print("\n     --------------------------------")
            print("      Resultado: " , grauAberta2[1])
            print("      Interações: " , grauAberta2[0])
            print("     --------------------------------")
        elif(methodIntegration == 3):
            grauAberta3 = funcao_geral_integracao(a, b, epsilon, "aberta3")
            print("\n     --------------------------------")
            print("      Resultado: " , grauAberta3[1])
            print("      Interações: " , grauAberta3[0])
            print("     --------------------------------")
        elif(methodIntegration == 4):
            grauAberta4 = funcao_geral_integracao(a, b, epsilon, "aberta4")
            print("\n     --------------------------------")
            print("      Resultado: " , grauAberta4[1])
            print("      Interações: " , grauAberta4[0])
            print("     --------------------------------")
    if(approach==0):
        running = False
    print("1 - Calcular novamente")
    print("0 - Sair do programa")
    choice = input('O que deseja fazer? ')
    choice = int(choice)
    if(choice==1):
        print("---------------------------------------------------")
        print("   fórmula base: f(x)=(sen(2x) + 4x^2 + 3x)^2")
        print("---------------------------------------------------\n")
    else:
        running = False


    