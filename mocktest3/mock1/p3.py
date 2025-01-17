def f(uid):
    set1 = set(uid)
    if len(set1) == len(uid):
        return True
    else:
        return False


print(f(["john5", "ann123", "JOHN5", "xxx", "abc333", "a10"]))
print(f(["abc123", "ann", "abc123", "a10"]))
