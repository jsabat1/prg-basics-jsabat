def f(arr2D):
    col_sums = [sum(col) for col in zip(*arr2D)]
    sum_counts = {}

    for s in col_sums:
        if s in sum_counts:
            sum_counts[s] += 1
        else:
            sum_counts[s] = 1

    for count in sum_counts.values():
        if count > 1:
            return True

    return False


print(f([[3, 4, 2], [5, 1, 6]]))
print(f([[3, 4, 2], [5, 1, 7]]))
print(f([[3, 4], [5, 1], [4, 7]]))
print(f([[3, 4], [5, 9], [4, 7]]))
