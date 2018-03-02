import re


def first_word(text: str) -> str:
    return re.search('[a-zA-Z0-9\']+', text).group(0)


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")
