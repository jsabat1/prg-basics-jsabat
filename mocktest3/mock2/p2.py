def f(x, y, d):
    count = 0
    for i in range(x, y + 1):
        if str(d) in str(i):
            count += 1
    if count > 0:
        return True
    else:
        return False


print(f(10, 15, "14"))  # Expected output: False
print(f(100, 120, "11"))  # Expected output: True
print(f(205, 210, "04"))  # Expected output: False
