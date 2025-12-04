ONES_F = ["", "одна", "дві", "три", "чотири", "п’ять", "шість", "сім", "вісім", "дев’ять"]
ONES_M = ["", "один", "два", "три", "чотири", "п’ять", "шість", "сім", "вісім", "дев’ять"]
TEENS = ["десять", "одинадцять", "дванадцять", "тринадцять", "чотирнадцять",
         "п’ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять", "дев’ятнадцять"]
TENS = ["", "", "двадцять", "тридцять", "сорок", "п’ятдесят",
        "шістдесят", "сімдесят", "вісімдесят", "дев’яносто"]
HUND = ["", "сто", "двісті", "триста", "чотириста",
        "п’ятсот", "шістсот", "сімсот", "вісімсот", "дев’ятсот"]


def words_0_999(n, fem=True):
    if n == 0:
        return ""
    h, r = n // 100, n % 100
    t, o = r // 10, r % 10
    out = []
    if h:
        out.append(HUND[h])
    if t == 1:
        out.append(TEENS[o])
    else:
        if t >= 2:
            out.append(TENS[t])
        if o:
            out.append((ONES_F if fem else ONES_M)[o])
    return " ".join(out)


def suf(n, one, few, many):
    if 11 <= n % 100 <= 14:
        return many
    return one if n % 10 == 1 else few if n % 10 in (2, 3, 4) else many


def money_to_words(x):
    g = int(x)
    k = int(round((x - g) * 100))
    t = g // 1000
    r = g % 1000
    parts = []
    if t:
        parts.append(words_0_999(t))
        parts.append(suf(t, "тисяча", "тисячі", "тисяч"))
    parts.append(words_0_999(r))
    parts.append(suf(g, "гривня", "гривні", "гривень"))
    parts.append(f"{k:02d}")
    parts.append(suf(k, "копійка", "копійки", "копійок"))
    return " ".join(filter(None, parts)).capitalize()


def main():
    assert money_to_words(1) == "Одна гривня 00 копійок"
    assert money_to_words(21.45) == "Двадцять одна гривня 45 копійок"
    assert money_to_words(1234.56) == "Одна тисяча двісті тридцять чотири гривні 56 копійок"
    assert money_to_words(999999.99) == "Дев’ятсот дев’яносто дев’ять тисяч дев’ятсот дев’яносто дев’ять гривень 99 копійок"


if __name__ == "__main__":
    main()
