dividir = lambda a, b: 0 if a < b else dividir(a - b, b) + 1
factorial = lambda x: 1 if x == 1 else x * factorial (x-1)
sumar_lista = lambda lista: lista[0] if len(lista) == 1 else sumar_lista(lista[1:]) + lista[0]
potencia = lambda x, e: x if e == 1 else x * potencia(x, e - 1) 


print(dividir(30,3))
print(factorial(3))
print(sumar_lista(range(10)))
print(potencia(3,5))

