#ejercicio 1: Llenar una lista
#llenar una lista con los nros del 1 al 50, luego mostrar
#la lista con el buvle for, los elementos deben mostrarse
#de la siguiente forma:
#1-2-3-4-5-..50

lista = []
i = 1
while i <= 50:
    lista.append(i)
    i += 1
for i in lista:
   print(i, end='-')
#algoritmo eficaz
lista = list(range(1,51))# algoritmo eficaz de menos lineas
for i in lista:
    print(i, end='-')

