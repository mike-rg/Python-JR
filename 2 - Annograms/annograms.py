def annograms(word):
    dictioinary = {}
    words = [w.rstrip() for w in open('WORD.lst')]
    for w in words:
        key = sorted_word(w)

        if key in dictioinary:
            values = dictioinary.get(key) + " , " + w
            dictioinary[key] = values
        else:
            dictioinary[key] = w

    key = sorted_word(word)
    values = dictioinary.get(key, "NONE")
    return values.split(" , ")


def sorted_word(word):
    chars = [c for c in word]
    chars.sort()
    return "".join(chars)

if __name__ == "__main__":
    print(annograms("train"))
    print('--')
    print(annograms("drive"))
    print('--')
    print(annograms("python"))
    print('--')
