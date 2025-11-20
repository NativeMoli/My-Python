

def simple_cipher(text: str) -> str:
    result = []

    for c in text:
        if 'a' <= c <= 'z':

            result.append(chr((ord(c) - ord('a') + 1) % 26 + ord('a')))
        elif 'A' <= c <= 'Z':
            result.append(chr((ord(c) - ord('A') + 1) % 26 + ord('A')))
        else:
            result.append(c)

    return ''.join(result)


def test_simple_cipher():
    cases = [
        ("vasia", "wbtjb"),
        ("abcxyz", "bcdyza"),
        ("Hello World!", "Ifmmp Xpsme!"),
        ("Python3.8", "Qzuipo3.8"),
        ("Zz", "Aa"),
        ("", ""),
    ]

    for text, expected in cases:
        result = simple_cipher(text)
        assert result == expected, f"Fail: simple_cipher({text!r}) = {result!r}, expected {expected!r}"


if __name__ == "__main__":
    test_simple_cipher()
