limite_peso = float(input("Limite de peso diário (kg): "))

peso_total = 0.0

while True:
    peso_peixe = float(input("Peso do peixe (kg): "))

    if peso_peixe == 0:
        break

    peso_total += peso_peixe

    print(f"\nPeso total: {peso_total:.2f} kg")

    if peso_total > limite_peso:
        print("ALERTA: Limite de peso diário excedido!")
        break