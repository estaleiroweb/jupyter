import pandas as pd
import numpy as np
import pickle


a2D = np.random.randint(1,101,(3,9))
b2D = np.random.randint(1,101,(5,9))
c2D = np.random.randint(1,101,(5,4))

A = np.concatenate((a2D, b2D), axis = 0) # Concatenando pelo eixo das colunas (eixo 0) (empilhamento vertical) 
print("a2D")
print(a2D)
print("")
print("b2D")
print(b2D)
print("")
print("Concatenação")
print(A)

print("-"*50)

B = np.vstack((a2D, b2D)) # Concatenando pelo eixo das colunas (eixo 0) (empilhamento vertical) 
print("a2D")
print(a2D)
print("")
print("b2D")
print(b2D)
print("")
print("Concatenação")
print(B)

print("-"*50)

C = np.concatenate((b2D, c2D), axis = 1) # Concatenando pelo eixo das linhas (eixo 1) (empilhamento horizontal) 
print("b2D")
print(b2D)
print("")
print("c2D")
print(c2D)
print("")
print("Concatenação")
print(C)

print("-"*50)

D = np.hstack((b2D, c2D)) # Concatenando pelo eixo das linhas (eixo 1) (empilhamento horizontal) 
print("b2D")
print(b2D)
print("")
print("c2D")
print(c2D)
print("")
print("Concatenação")
print(D)

print("-"*50)

x = np.random.randint(1,101,(3,9))
y = np.random.randint(1,101,(3,9))

CC = np.stack((x, y)) # Concatenando pelo eixo das linhas (eixo 1) (empilhamento horizontal) 
print("x")
print(x)
print("")
print("y")
print(y)
print("")
print("Concatenação")
print(CC)



livros = pd.Series(["Introdução à programação com Python",
                    "Curso Intensivo de Python",
                    "Python para análise de dados"])

x=livros.str.lower()
print(x)
