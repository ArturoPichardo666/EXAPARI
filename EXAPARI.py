#pedir al usurio 2 numeros A y B



n=True
suma=0
while n:

print("Dame el numero 1")
num1=int (input())
print("Dame el numero 2")
num2=int (input())
if num1 < 0 and num2 > 0 or num2 > 0 and num1 < 0:
    suma= num1 + num2   
    print("La suma es:",suma)
elif num1 < 0 and num2 < 0:
    multiplicacion = num1 * num2