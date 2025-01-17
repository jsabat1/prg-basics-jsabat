def f(word):
    if not word:
        return ""
    wave = []
    for i in range(len(word)):
        wave.append(word[:i].lower() + word[i].upper() + word[i + 1 :].lower())
    return "-".join(wave)


print(f("hello"))
print(f("world"))


# f("book") à "Book-bOok-boOk-booK"
# f("water") à "Water-wAter-waTer-watEr-wateR"
# f("ok") à "Ok-oK"
# f("a") à "A"
# f("") à ""
