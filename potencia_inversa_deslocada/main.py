from potencia_inversa import Potencia_inversa
from potencia_deslocamento import Potencia_deslocamento

def metodo_potencia_inversa(): 
    print("----------------------------------------------------")
    print("            Método da potência inversa")
    print("---------------------------------------------------\n")
    v0_a = [1, 0, 0]
    v0_a3 = [1, 0, 0, 0, 0]
    matriz_a1 = [[5,2,1],[2,3,1],[1,1,2]]
    matriz_a2 = [[-14,1,-2],[1,-1,1],[-2,1,-11]]
    matriz_a3 = [[40,8,4,2,1], [8,30,12,6,2], [4,12,20,1,2],[2,6,1,25,4], [1,2,2,4,5]]
    [novo_autovalor_a1, novo_autovetor_a1] = Potencia_inversa(matriz_a1, v0_a, 0.00001)
    [novo_autovalor_a2, novo_autovetor_a2] = Potencia_inversa(matriz_a2, v0_a, 0.00001)
    [novo_autovalor_a3, novo_autovetor_a3] = Potencia_inversa(matriz_a3, v0_a3, 0.00001)
    print("Respostas da matriz A1")
    print("----------------------------------------------------------------")
    print("          Autovalor:", novo_autovalor_a1,"Autovetor:",  novo_autovetor_a1)
    print("----------------------------------------------------------------")
    print("Respostas da matriz A2")
    print("----------------------------------------------------------------")
    print("          Autovalor:", novo_autovalor_a2,"Autovetor:",  novo_autovetor_a2)
    print("----------------------------------------------------------------")
    print("Respostas da matriz A3")
    print("----------------------------------------------------------------")
    print("          Autovalor:", novo_autovalor_a3,"Autovetor:",  novo_autovetor_a3)
    print("----------------------------------------------------------------")
 
def metodo_potencia_deslocamento(): 
    print("----------------------------------------------------")
    print("            Método da potência com deslocamento")
    print("---------------------------------------------------\n")
    v0_a = [1, 0, 0]
    v0_a3 = [1, 0, 0, 0, 0]
    matriz_a1 = [[5,2,1],[2,3,1],[1,1,2]]
    matriz_a2 = [[-14,1,-2],[1,-1,1],[-2,1,-11]]
    matriz_a3 = [[40,8,4,2,1], [8,30,12,6,2], [4,12,20,1,2],[2,6,1,25,4], [1,2,2,4,5]]    
    [novo_autovalor_a1, novo_autovetor_a1] = Potencia_deslocamento(matriz_a1, v0_a, 0.00001, 3)
    [novo_autovalor_a2, novo_autovetor_a2] = Potencia_deslocamento(matriz_a2, v0_a, 0.00001, -10)
    [novo_autovalor_a3, novo_autovetor_a3] = Potencia_deslocamento(matriz_a3, v0_a3, 0.00001, 10)
    print("Respostas da matriz A1")
    print("----------------------------------------------------------------")
    print("          Autovalor:", novo_autovalor_a1,"Autovetor:",  novo_autovetor_a1)
    print("----------------------------------------------------------------")
    print("Respostas da matriz A2")
    print("----------------------------------------------------------------")
    print("          Autovalor:", novo_autovalor_a2,"Autovetor:",  novo_autovetor_a2)
    print("----------------------------------------------------------------")
    print("Respostas da matriz A3")
    print("----------------------------------------------------------------")
    print("          Autovalor:", novo_autovalor_a3,"Autovetor:",  novo_autovetor_a3)
    print("----------------------------------------------------------------")

print("-------------- BEM VINDO AO PROGRAMA --------------")
result = input('Deseja saber os resultados de qual método? 1 - potencia inversa  2 - potencia com deslocamento ')
result= int(result)
if(result==1):
    metodo_potencia_inversa()
else:
    metodo_potencia_deslocamento()