soma = 0
positivos = 0

for i in range(6):
    n = float(input())
    if n > 0:
        positivos +=1
        soma += n

media = soma / positivos 

print(f"{positivos} valores positivos")
print(f"{media:.1f}")