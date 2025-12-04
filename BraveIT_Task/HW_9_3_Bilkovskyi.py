ROMAN = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

def roman_to_int(s):
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and ROMAN[s[i]] < ROMAN[s[i+1]]:
            total -= ROMAN[s[i]]
        else:
            total += ROMAN[s[i]]
    return total


def int_to_roman(num):
    vals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
        (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"), (1, "I")
    ]
    out = []
    for v, r in vals:
        while num >= v:
            out.append(r)
            num -= v
    return "".join(out)


def main():

    assert roman_to_int("MCMLXXXII") == 1982
    assert roman_to_int("MCMLXXVII") == 1977
    assert roman_to_int("MMXII") == 2012
    assert roman_to_int("MMXXIV") == 2024


    assert int_to_roman(1988) == "MCMLXXXVIII"
    assert int_to_roman(1991) == "MCMXCI"




if __name__ == "__main__":
    main()
