def f(x, y, digit):
    how_many = 0
    for i in range(x, y + 1):
        how_many += str(i).count(str(digit))
    return how_many


print(f(10, 15, 1))  # 7
print(f(28, 32, 2))  # 3
