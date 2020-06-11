from operaciones import suma, nombres as q
from calculo import calcula, nombres

def mainfn():
    print("hola",suma(4,5,6,7))
    print(calcula(2,4,6))
    print(nombres)
    print(q)

    print(__name__)

#import numpy as np -> np.asarray
#from numpy import * -> asarray

if __name__ == "__main__":
    mainfn()

