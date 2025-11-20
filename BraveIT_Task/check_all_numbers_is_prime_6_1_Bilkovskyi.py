"""
Напишіть програму на Python, щоб перевірити, чи кожне число є простим
у заданому списку чисел.
Повертає True, якщо всі числа прості, інакше False
"""

def is_prime(number):
    # look for solution in previous topics
    if number < 2 :
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def check_numbers_prime(nums: list):

    # code implementation
    for n in nums:
        if not is_prime(n):
            return False
    return True


def test():
    cases = [ 
    [False, [0, 3, 4, 7, 9]],
    [True, [3, 5, 41, 7, 13]],
    [False, [1, 5, 3, 23]]
    ]

    for case in cases:
        expected, inputs = case
        result = check_numbers_prime(inputs)
        assert expected == result, 'Wrong result.\nExpected: {}\nActual: {}'.format(expected, result)


if __name__ == '__main__':
    test()

