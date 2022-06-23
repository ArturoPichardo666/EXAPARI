from re import A
A = 270
B = 340
C = 390
bebida = 0
mone1 = 10
mone2 = 50 
mone3 = 100
print("Elige una bebida")
print("1 A = 270")
print("2 B = 340")
print("3 C = 390")
print("Selecciona una opcion:")
opcion = int(input())
if opcion == 1:
    bebida = A
elif opcion == 2:
    bebida = B
else:
    bebida = C
mone = bebida   