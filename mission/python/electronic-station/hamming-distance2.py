def checkio(n, m):
    bin_n = str(bin(n))[2:][::-1]
    bin_m = str(bin(m))[2:][::-1]

    len_diff = len(bin_n) - len(bin_m)

    if len_diff < 0:
        bin_n = bin_n + '0' * (len_diff * -1)
    elif len_diff > 0:
        bin_m = bin_m + '0' * len_diff

    sum = 0
    for x, y in zip(bin_n, bin_m):
        if x != y:
            sum = sum + 1
    return sum


if __name__ == '__main__':
    assert checkio(255, 1) == 7, "First example"
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
