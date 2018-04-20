def find_sequence(row_index, column_index, len_index, matrix):
    row_index_etalon = row_index
    column_index_etalon = column_index
    count = 0
    search_number = matrix[row_index][column_index]
    if row_index + 4 <= len_index:
        for index in range(4):
            row_index = row_index + 1
            found_number = matrix[row_index][column_index]
            if found_number is not search_number:
                break
            else:
                count = count + 1
                if count == 3:
                    return True
    row_index = row_index_etalon
    column_index = column_index_etalon
    count = 0
    if column_index + 4 <= len_index:
        for index in range(4):
            column_index = column_index + 1
            found_number = matrix[row_index][column_index]
            if found_number is not search_number:
                break
            else:
                count = count + 1
                if count == 3:
                    return True
    row_index = row_index_etalon
    column_index = column_index_etalon
    count = 0
    if row_index + 4 <= len_index and column_index + 4 <= len_index:
        for index in range(4):
            column_index = column_index + 1
            row_index = row_index + 1
            found_number = matrix[row_index][column_index]
            if found_number is not search_number:
                break
            else:
                count = count + 1
                if count == 3:
                    return True
    row_index = row_index_etalon
    column_index = column_index_etalon
    count = 0
    if row_index + 4 < len_index and column_index - 4 < 0:
        for index in range(4):
            column_index = column_index - 1
            row_index = row_index + 1
            found_number = matrix[row_index][column_index]
            if found_number is not search_number:
                return False
            else:
                count = count + 1
                if count == 3:
                    return True
    return False


def checkio(matrix):
    len_matrix = len(matrix[0])
    for row_index in range(len_matrix):
        for column_index in range(len_matrix):
            if find_sequence(row_index, column_index, len_matrix, matrix):
                return True
    return False


if __name__ == '__main__':
    assert checkio([[2, 6, 2, 2, 7, 6, 5],
                    [3, 4, 8, 7, 7, 3, 6],
                    [6, 7, 3, 1, 2, 4, 1],
                    [2, 5, 7, 6, 3, 2, 2],
                    [3, 4, 3, 2, 7, 5, 6],
                    [8, 4, 6, 5, 2, 9, 7],
                    [5, 8, 3, 1, 3, 7, 8]]) == True, "Test blat"
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
