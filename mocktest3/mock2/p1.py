def f(n):
    n = [int(i) for i in str(n)]

    for i in n:
        if i % 2 != 1:
            return -1
        break

    biggest = None
    smallest = None

    for i in n:
        if i % 2 != 0:
            if biggest is None or i > biggest:
                biggest = i
            if smallest is None or i <= smallest:
                smallest = i

    if biggest is not None and smallest is not None:
        return biggest - smallest
    return -1


print(f(10852))  # 4
print(f(723597))  # 6
print(f(4388))  # 0
print(f(846206))  # -1

## nie dziala
