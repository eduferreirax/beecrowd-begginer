coelhos = 0
ratos = 0
sapos = 0
total = 0

n = int(input())

for i in range(n):
    qtd, tipo = input().split()
    qtd = int(qtd)
    
    total += qtd
    
    if tipo == "C":
        coelhos += qtd
    elif tipo == "R":
        ratos += qtd
    elif tipo == "S":
        sapos += qtd
    
    percentual_de_coelhos = (coelhos / total) * 100
    percentual_de_ratos = (ratos / total) * 100
    percentual_de_sapos = (sapos / total) * 100
    
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percentual_de_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_de_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_de_sapos:.2f} %")