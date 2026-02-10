x, y, z = map(int, input().split())

original = [x, y, z]

ordenada = sorted(original)

for v in ordenada:
    print(v)

print()

for v in original:
    print(v)