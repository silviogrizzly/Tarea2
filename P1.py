#Creacion de ecuacion Catenaria para encontrar ceros
import numpy as np
import matplotlib.pyplot as plt


# Para la funcion catenaria en el enunciado se aplicó condiciones dadas para tener la funcion que entregará los ceros

def f(x):  #funcion 
    y=x*np.cosh(10/x)-x-7.5
    return y

def df(x):      #Derivada de la funcion f(x)
    y=np.cosh(10/x)-((10/x)*np.sinh(10/x))-1
    return y


x = np.linspace(-2,2,100)
plt.figure(num="Newton")
plt.plot(x, f(x))
plt.grid('on')
plt.show()