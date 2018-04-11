import re


def is_start_round(symbol):
    return symbol == '('


def is_finish_round(symbol):
    return symbol == ')'


def is_start_square(symbol):
    return symbol == '['


def is_finish_square(symbol):
    return symbol == ']'


def is_start_curly(symbol):
    return symbol == '{'


def is_finish_curly(symbol):
    return symbol == '}'


def get_first_close_bracket(text):
    return re.search('\)|\}|\]', text).group()


def get_first_close_bracket(text, start_index):
    return re.search('\)|\}|\]', text[start_index:len(text)]).group()


def get_last_open_bracket(text):
    return re.findall('\(|\{|\[', text)[-1]


def get_only_open_brackets(text):
    return ''.join(
        symbol for symbol in text if (
                is_start_curly(symbol) or is_start_square(symbol) or is_start_round(symbol)))


def get_only_close_brackets(text):
    return ''.join(
        symbol for symbol in text if (
                is_finish_curly(symbol) or is_finish_square(symbol) or is_finish_round(symbol)))


def get_only_brackets(text):
    return ''.join(
        symbol for symbol in text if (
                is_start_curly(symbol) or is_start_square(symbol) or is_start_round(symbol) or
                is_finish_curly(symbol) or is_finish_square(symbol) or is_finish_round(symbol)))


def get_bracket_name(symbol):
    if symbol == '(' or symbol == ')':
        return 'round'
    if symbol == '[' or symbol == ']':
        return 'square'
    if symbol == '[' or symbol == ']':
        return 'curly'


def checkio(expression):
    only_brackets = get_only_brackets(expression)

    if len(get_only_open_brackets(only_brackets)) != len(get_only_close_brackets(only_brackets)):
        return False

    for index in range(len(only_brackets) // 2):
        last_open_bracket = get_last_open_bracket(only_brackets)
        index_last_open_bracket = len(only_brackets) - only_brackets[::-1].index(last_open_bracket)
        first_close_bracket = get_first_close_bracket(only_brackets, index_last_open_bracket)
        if get_bracket_name(last_open_bracket) is not get_bracket_name(first_close_bracket):
            return False
        else:
            buffer_start_brackets = only_brackets[0:index_last_open_bracket]
            buffer_end_brackets = only_brackets[index_last_open_bracket:len(only_brackets)]
            buffer_end_brackets = buffer_end_brackets.replace(first_close_bracket, '', 1)
            buffer_start_brackets = buffer_start_brackets[::-1]
            buffer_start_brackets = buffer_start_brackets.replace(last_open_bracket, '', 1)
            buffer_start_brackets = buffer_start_brackets[::-1]
            only_brackets = buffer_start_brackets + buffer_end_brackets

    return True


if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
