def checkio(text):
    low_text = text.lower()
    words = []
    for word in low_text:
        if word.isalpha():
            words.append([low_text.count(word), word])
    maximum_value = max(words)[0]
    maximum_values = []
    for value in words:
        if value[0] == maximum_value:
            maximum_values.append(value[1])
    return min(maximum_values)


if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
