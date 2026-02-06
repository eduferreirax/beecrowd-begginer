x = float(input())
tax = 0

if x > 4500:
    tax += (x - 4500) * 0.28
    x = 4500
if x > 3000:
    tax += (x - 3000) * 0.18
    x = 3000
if x > 2000:
    tax += (x - 2000) * 0.08

if tax == 0:
    print("Isento")
else:
    print(f"R$ {tax:.2f}")