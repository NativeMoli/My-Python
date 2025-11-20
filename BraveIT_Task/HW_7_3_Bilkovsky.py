def check_brackets(s: str) -> bool:

    stack = []
    opening = "([{<"
    closing = ")]}>"
    pairs = {')':'(', ']':'[', '}':'{', '>':'<'}

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0


def test_check_brackets():
    cases = [
        ("(((a * x) + [b] * y) + c", False),
        ("auf(zlo)men [gy<psy>] four{s}", True),
        ("(a+[b*c] - {d/3})", True),
        ("(a+[b*c) - 17]", False),
        ("{[()]}", True),
        ("{[(])}", False),
        ("<({[]})>", True),
        ("<({[}])>", False),
        ("", True),
    ]

    for s, expected in cases:
        result = check_brackets(s)
        assert result == expected, f"Fail: check_brackets({s!r}) = {result}, expected {expected}"



if __name__ == "__main__":
    test_check_brackets()
