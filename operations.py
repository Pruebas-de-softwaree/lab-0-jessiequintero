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
    salida10 = power(1,1)
    salida11 = square_root(9)
    #salida12 = square_root(-1)

    list1 = [3,5,2,5,2]
    salida13 = average(list1)
    #salida14 = average(5)

    list2 = [9,5,7,9,3,4,6]
    salida15 = maximum(list2)

    salida16 = maximum(9)

    print(salida16)

    print("end test")

