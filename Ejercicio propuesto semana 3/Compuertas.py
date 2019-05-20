class Compuerta:
    def __init__(self,a,b):
        if a == "0" and  b == "0":
            print("0")
        elif a == "1" and  b == "1":
            print("1")

class Or(Compuerta):
    def compuerta_or(self,a,b):
        if a == "0" and  b == "1" or a == "1" and  b == "0":
            print("1")
class And(Compuerta):
    def compuerta_and(self,a,b):
        if a == "0" and  b == "1" or a == "1" and  b == "0":
            print("0")

print("Escribe el valor de A")
A = input()
print("Escribe el valor de B")
B = input()
print("Para la compuerta OR")
X = Or(A,B)
X.compuerta_or(A,B)
print("Para la compuerta AND")
X = And(A,B)
X.compuerta_and(A,B)

