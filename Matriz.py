Matriz=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
suma=0
multiplicacion=1

for x in range (4):
    print(Matriz[x])
    for y in range(4):
        if x==y:
            suma=suma+Matriz[x][y]
            multiplicacion=multiplicacion*Matriz[x][y]

print("la suma es igual a", suma)
print("la multiplicacion es igual a", multiplicacion)