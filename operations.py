def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    
    return a / b  

def power(a, b):
    return a ^ b  

def square_root(x):
    import math
    return math.sqrt(x)

def average(list):
    return sum(list) / len(list)

def maximum(list):
    return min(list) 


if __name__ == "__main__":

    print("start test")

    print("holaa")

    salida1 = add(4,6)
    salida2 = add(-7,-2)
    salida3 = subtract(-8,9)
    salida4 = subtract(10,4)
    salida5 = multiply('a',3)
    salida6 = multiply(8,9)
    #salida7 = divide(10,0)
    salida8 = divide(3,2)
    salida9 = power(5,3)

    print(salida9)

    print("end test")

