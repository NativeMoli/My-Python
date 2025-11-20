'''
Напишіть реалізацію функції closest_mod_5, яка приймає один цілочисельний аргумент
та повертає найменше число y, яке:
y >= x
y % 5 == 0
'''

def closest_mod_5(x):
    while  x % 5 != 0:
        x += 1
    return x



cases = [
    # expected, input
    [5, 5],
    [15, 13],
    [0, 0],
    [0, -1],
    [-15, -16]
]

for i in cases:
    expected, inp = i
    res = closest_mod_5(inp)
    assert expected == res, 'Fail. Expected: {}\nActual: {}'.format(expected, res)

