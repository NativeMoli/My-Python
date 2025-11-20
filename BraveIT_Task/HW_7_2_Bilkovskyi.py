

def is_palindrome(phrase: str) -> bool:
    cleaned = ''.join(c.lower() for c in phrase if c.isalnum())
    return cleaned == cleaned[::-1]

def test_is_palindrome():
    cases = [
        ("Was it a cat I saw", True),
        ("No 'x' in Nixon", True),
        ("А роза упала на лапу Азора", True),
        ("Три психи пили Пилипихи спирт", True),
        ("Вор Азаров", True),
        ("Hello, world!", False),
        ("Palindrome", False),
        ("", True),
        ("A", True),
    ]

    for phrase, expected in cases:
        result = is_palindrome(phrase)
        assert result == expected, f"Fail: is_palindrome({phrase!r}) = {result}, expected {expected}"


if __name__ == "__main__":
    test_is_palindrome()
