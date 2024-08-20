import math

def integrando(x):
    return pow((math.sin(2*x)+4*(x**2)+3*x), 2)

def funcao_geral_integracao(a, b, epsilon, tipo):
    delta = 0
    xi = 0
    erro = 0
    resultadoAnterior = 0
    resultado = 0
    interacoes = 0
    N = 2

    while True:
        interacoes += 1
        delta = (b-a)/N
        integral = 0
        for i in range(N):
            xi = a + i*delta
            xf = xi + delta
            if(tipo == "fechada1"):
                integral += formula1_fechada(xi, xf)
            elif(tipo=="fechada2"):
                integral += formula2_fechada(xi, xf)
            elif(tipo=="fechada3"):
                integral += formula3_fechada(xi, xf)
            elif(tipo=="fechada4"):
                integral += formula4_fechada(xi, xf)
            elif(tipo=="aberta1"):
                integral += formula1_aberta(xi, xf)
            elif(tipo=="aberta2"):
                integral += formula2_aberta(xi, xf)
            elif(tipo=="aberta3"):
                integral += formula3_aberta(xi, xf)
            elif(tipo=="aberta4"):
                integral += formula4_aberta(xi, xf)
        N *= 2
        resultadoAnterior = resultado
        resultado = integral
        erro = abs(resultado - resultadoAnterior)
        if(erro < epsilon):
            break
    
    return interacoes, resultado

def formula1_fechada(xi, xf): #GRAU 1
    return (xf-xi)/2*(integrando(xi)+integrando(xf))
    
def formula2_fechada(xi, xf): #GRAU 2
    h = (xf-xi)/2
    return (h)/3*(integrando(xi) + 4*integrando(xi+h) + integrando(xi+2*h))

def formula3_fechada(xi, xf): #GRAU 3
    h = (xf-xi)/3
    return (3*(h)/8)*(integrando(xi) + 3*integrando(xi+h) + 3*integrando(xi+2*h) +integrando(xi+3*h))

def formula4_fechada(xi, xf): #GRAU 4 
    h = (xf-xi)/4
    return (2*(h)/45)*(7*integrando(xi) + 32*integrando(xi+h) + 12*integrando(xi+2*h) +32*integrando(xi+3*h)+7*integrando(xi+4*h))
        
def formula1_aberta(xi, xf): #GRAU 1
    h = (xf-xi)/3
    return (xf-xi)/2*(integrando(xi+h)+integrando(xi+2*h))

def formula2_aberta(xi, xf): #GRAU 2
    h = (xf-xi)/4
    return ((4*h)/3)*(2*integrando(xi+h) - integrando(xi+2*h) + 2*integrando(xi+3*h))   

def formula3_aberta(xi, xf): #GRAU 3
    h = (xf-xi)/5
    return ((5*h)/24)*(11*integrando(xi+h) + integrando(xi+2*h) + integrando(xi+3*h) + 11*integrando(xi+4*h))

def formula4_aberta(xi, xf): #GRAU 4
    h = (xf-xi)/6
    return ((6*h)/20)*(11*integrando(xi+h) - 14*integrando(xi+2*h) + 26*integrando(xi+3*h) - 14*integrando(xi+4*h)+ 11*integrando(xi+5*h))
