def rotate_string(s: str, k: int) -> str:

    n = len(s)
    if n == 0 or k == 0:
        return s

    if k > 0:
        k = k % n
        return s[k:] + s[:k]
    else:
        k = (-k) % n
        return s[-k:] + s[:-k]

def test_rotate_string():
    cases = [

        ('forwhomthebelltolls', 3, 'whomthebelltollsfor'),
        ('verycomplexnumber', -6, 'numberverycomplex'),
        ('abcdef', 2, 'cdefab'),
        ('abcdef', -2, 'efabcd'),
        ('abcdef', 0, 'abcdef'),
        ('a', 1, 'a'),
        ('', 3, ''),
        ('rotation', 8, 'rotation'),
        ('rotation', -8, 'rotation')
    ]

    for s, k, expected in cases:
        result = rotate_string(s, k)
        assert result == expected, f"Fail: rotate_string({s!r}, {k}) = {result!r}, expected {expected!r}"



if __name__ == "__main__":
    test_rotate_string()
