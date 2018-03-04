def checkio(number):
    result = 1
    numbers = [int(num) for num in str(number) if num != '0']
    for digit in numbers:
        result = result * digit
    return result


if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
