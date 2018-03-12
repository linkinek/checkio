import re


def is_stressful(subj):
    return len(
        re.findall('(h+.?e+.?l+.?p+)|(a+.?s+.?a+.?p)|(u+.?r+.?g+.?e+.?n+.?t)|(!!!)$', subj, re.IGNORECASE)) > 0 or subj.isupper()


if __name__ == '__main__':
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("something is gona happen") == False
    print('Done! Go Check it!')
