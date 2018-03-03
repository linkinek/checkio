import re


def checkio(words):
    words_list = words.split(' ')
    count = 0
    for word in words_list:
        if re.match('[a-zA-Z]+', word):
            count = count + 1
            if count == 3:
                return True
        else:
            count = 0
    return False


if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
