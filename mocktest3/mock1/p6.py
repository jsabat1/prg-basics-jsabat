def f(vname):
    if len(vname) < 1 or len(vname) > 5:
        return False
    if not (vname[0].isalpha() or vname[0] == "_"):
        return False
    for i in vname[1:]:
        if not (i.isalpha() or i.isnumeric() or i == "_"):
            return False
    return True


print(f("abc"))  # True
print(f("Abc"))  # True
print(f("aBC"))  # True
print(f("_ab_c"))  # True
print(f("abcdef"))  # False
print(f("8abc"))  # False
print(f("_aB8_"))  # True
print(f("_4x"))  # True
