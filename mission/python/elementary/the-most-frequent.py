def most_frequent(data):
    count_array = {}
    for string in data:
        count_array[data.count(string)] = string
    return count_array[max(count_array)]


if __name__ == '__main__':
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
