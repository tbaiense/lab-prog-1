while True:
    fib_n = int(input("Termos calculados: "))
     
    if fib_n < 1:
        print("Número de termos inválido. Tente novamente...")
    else:
        break

a = 0
b = 1

for _ in range(fib_n):
    print(a, end='  ')

    prox = a + b
    a = b
    b = prox
