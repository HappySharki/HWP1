# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ = not
# ⋁ = or
# ⋀ = and
def TruthCheck ():
    result = True
    for n in range(0, 8):
        num = bin(n)
        print(f'{n} =', end=" ") # Нумерация
        print(f'{num} =', end=" ") # Бинарное представление числа
        num = num.replace('b', '0')
        X = int(num[-3])
        Y = int(num[-2])
        Z = int(num[-1])
        print(f'{X}{Y}{Z}', end=" ") # Результат сортировки нужных значений xyz
        result = (not(X or Y or Z)) == ((not X) and (not Y) and (not Z))
        print()
        if result is True:
            result = "Утверждение является истинным"
        else:
            result = "Утверждение является ложным"
    return result
print(TruthCheck())