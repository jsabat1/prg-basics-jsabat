def f(fnc, res):
    filtered_res = list(filter(fnc, res))
    if not filtered_res:
        return 0
    return max(filtered_res) - min(filtered_res)

res = [95, 90, 20, 50, 70]
fnc1 = lambda x: x > 50
print(f(fnc1, res))  # Output: 25

fnc2 = lambda x: x > 30 and x < 90
print(f(fnc2, res))  # Output: 20
