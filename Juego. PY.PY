import random

op = ["piedra", "papel", "tijeras"]

while True:
    user = input ("Elije: piedra, papel o tijeras: ").lower ()
    if user not in op:
        print ("\nMovimiento no valido")
        continue
    pc = random.choice (op)
    print (f"\nLa PC ha seleccionado {pc}")
    if user == pc:
        print(f"\nEmpate!, ambos eligieron {user}")
    elif user == "piedra" and pc == "tijeras":
         print (f"Ganaste!, {user} ganas en contra de {pc}")
    elif user == "papel" and pc == "piedra":
         print (f"Ganaste!, {user} ganas en contra de {pc}")
    elif user == "tijeras" and pc == "papel":
         print (f"Ganaste!, {user} ganas en contra de {pc}")
    else:
         print(f"\nPerdiste, {user}pierde en contra de {pc}")


    