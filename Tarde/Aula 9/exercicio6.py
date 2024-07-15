numero = int(input("Digite um número:"))

for n in range(1,numero+1):
    print(f"Tabuada do {n}")
    for i in range(1,11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")
        
    print("------------------")