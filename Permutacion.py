print("ESTE PROGRAMA PERMUTA LOS NÚMEROS QUE INGRESES (3 NUM MAX)")
print()
print()
print()

x = int(input("Ingrese un número: "))
y = int(input("Ingrese un número: "))
z = int(input("Ingrese un número: "))
n = int(input("Las permutaciones no deben ser igual a: "))
    
conjunto = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                conjunto.append([i, j, k])
    print(conjunto)