'''
Написати функцію, яка приймає ціле число його двійкове представлення
'''
from math import remainder


def binary(number):
    if number == 0:
        return '0'

    result = ''
    while number > 0:
        remainder = number % 2
        result = str(remainder) + result
        number //= 2
    return result

cases = [
        ['0', 0],
        ['1', 1],
        ['101', 5],
        ['110', 6],
        ['1011', 11],
        ['1100101', 101],
        ['100100101001', 2345],
    ]

for i in cases:
    expected, number = i
    result = binary(number)
    assert expected == result, 'Wrong convertation.\nExpected: {}\nActual: {}'.format(expected, result)
