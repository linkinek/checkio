def second_index(text: str, symbol: str):
    count = 0
    for index, letter in enumerate(text):
        if letter == symbol:
            if count == 1:
                return index
            else:
                count = count + 1
    return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
