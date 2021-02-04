#!/usr/bin/env python3
"""
EJERCICIO 1: Implemente en lenguaje Python una función que aproxime mediante un Polinomio de Taylor de tercer orden centrado en x=1 para predecir f(2), siendo f(x) = 25x**3 – 6x**2 + 7x – 88. Calcule luego el error relativo de la aproximación.

EJERCICIO 2: Implemente en lenguaje Python el método de Newton-Raphson para aproximar la solución de f(x) = 0, siendo f(x) = exp(-x)-ln(x).

Escriba aqui los nombres de los integrantes del grupo:
- Lusandre Marcano. CI:28349644
- José Gómez. CI:27547101
"""
'''
    Ejercicio 1: Polinomio de Taylor
'''

# Librerias
from math import * # Para funciones matematicas
from sympy import * # Para funciones en forma simbólica

# Funciones 
def Ptaylor(fx,x0,n): #Funcion que calcula el polinomio de Taylor
    k = 0 
    poli = 0 
    while (k <= n): 
        
        poli += fx.diff(x,k).subs(x,x0)/factorial(k)*(x-x0)**k # Calcula el polinomio Taylor aumentando el orden en cada iteracion
        k += 1 
    
    return poli # Devuelve el error relativo polinomio de Taylor

def Erelativo(fx,x0,n,c):
 
    Em =  fx.diff(x,n+1).subs(x,c) / factorial(n+1)*(x-x0)**(n+1) # Error maximo relativo
    Er = Em.subs(x,c)/fx.subs(x,c)                                # Error relativo
    
    return Er # Devuelve el error relativo


# Definicion de parametros    
x = Symbol('x')  # Variable x es simbólica
fx = 25*x**3-6*x**2+7*x-88 # se define la funcion a evaluar

x0 = 1 #Punto entorno al cual se calcula el polinomio de Taylor
xi = 2 #Donde se evalua el polinomio 
n = 3  #Orden para calcular el polinomio

# Inicio 
fxi = fx.subs(x,xi)           # Polinomio evaluado en xi 
Poli = Ptaylor(fx,x0,n)       # Aproximado con Taylor
pxi = Poli.subs(x,xi)         # Aprox evaluada en xi
Ereal = fxi - pxi             # Error real 
Erela = Erelativo(fx,x0,n,xi) # Error relativo

# Impresiones en pantalla
print('Polinomio de Taylor')
print(' Funcion original:',fx)
print(' Polinomio de Taylor:', Poli) 
print(' Valor de evaluacion:', xi) 
print(' Solucion aproximada:', pxi) 
print(' Solucion real:', fxi) 
print(' Error real:', Ereal)
print(' Error relativo:', Erela)




'''
    Ejercicio 2: Metodo de Newton-Raphson
'''

from math import *
 
def newton(f,df,xi,Es):    
    """
    #Aplica el Metodo de Newton Raphson a los valores ingresados por parametros:
        f  = funcion 
        df = derivada de la funcion
        xi = valor de inicio
        Es = error inicial
    """
    x  = xi 
    Ea = 100    #Error Aproximado
    n  = 1      #Numero de Iteracion
    xa = 0
    print("Aproximacion Inicial:",x)
    while Ea > Es:
        xa = x
        x  = x-f(x)/df(x)      #Formula iterativa de Newton-Raphson para calcular la siguiente aproximacion
        Ea = abs((x-xa)/x*100) #calculo del error aproximado
        n += 1
        print("[Aprox. a la raiz:",x,"]","[Error aprox.: {:.2f},%]".format(Ea))
    print(x,"-->Es una buena aproximacion para la solucion de f(x)=0")
    print("Numero de iteraciones realizadas: ",n)

f  = lambda x : e**-x-log(x)     #Funcion
df = lambda x : -(1/exp(x))-1/x  #Derivada de la funcion
print('Metodo de Newton Raphson')
newton(f,df,1,1)