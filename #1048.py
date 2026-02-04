salary = float(input())

if salary >= 0 and salary <= 400.01:
    reajuste = 0.15 * salary
    soma = reajuste + salary
    percentual = ("15 %")
    print(f"Novo salario: {soma:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual}")
    
elif salary >= 400.01 and salary <= 800.00:
    reajuste = 0.12 * salary
    soma = reajuste + salary
    percentual = ("12 %")
    print(f"Novo salario: {soma:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual}")
    
elif salary >= 800.01 and salary <= 1200.00:
    reajuste = 0.10 * salary
    soma = reajuste + salary
    percentual = ("10 %")
    print(f"Novo salario: {soma:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual}")

elif salary >= 1200.01 and salary <= 2000.00:
    reajuste = 0.07 * salary
    soma = reajuste + salary
    percentual = ("7 %")
    print(f"Novo salario: {soma:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual}")

elif salary > 2000.01:
    reajuste = 0.04 * salary
    soma = reajuste + salary
    percentual = ("4 %")
    print(f"Novo salario: {soma:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual}")
