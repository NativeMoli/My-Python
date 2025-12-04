def Max(a, b):
    return a if a >= b else b


def Min(a, b):
    return a if a <= b else b


def main():

    a = 10
    b = 7

    print("Max:", Max(a, b))
    print("Min:", Min(a, b))

    assert Max(1, 2) == 2
    assert Max(10, -5) == 10
    assert Max(-3, -7) == -3
    assert Max(5, 5) == 5

    assert Min(1, 2) == 1
    assert Min(10, -5) == -5
    assert Min(-3, -7) == -7
    assert Min(5, 5) == 5

if __name__ == "__main__":
    main()
