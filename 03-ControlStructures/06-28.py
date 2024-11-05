fibonacci1 = 1
fibonacci2 = 1
fib3 = 0
print(fibonacci1)
print(fibonacci2)
for i in range(2, 21):
    fib3 = fibonacci1 + fibonacci2
    print(fib3)
    fibonacci1 = fibonacci2
    fibonacci2 = fib3
