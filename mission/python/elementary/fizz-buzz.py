def is_division_by_number(number, division_number):
    return number % division_number == 0


def checkio(number):
    if is_division_by_number(number, 3) and is_division_by_number(number, 5):
        return 'Fizz Buzz'
    elif is_division_by_number(number, 3):
        return 'Fizz'
    elif is_division_by_number(number, 5):
        return 'Buzz'
    else:
        return str(number)


if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
