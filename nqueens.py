import string
mapping = string.digits + string.ascii_lowercase
reverse_mapping = dict.fromkeys(mapping, 0)

for i in range(36):
    key = mapping[i]
    reverse_mapping[key] = i

del i


def base_n(number: int, base):
    if number == 0:
        return '0'
    if number < 0:
        raise ValueError("Negative number not accepted.")
    result = ''
    while number > 0:
        number, digit = divmod(number, base)
        result = mapping[digit] + result
    return result


def digit_list(numeric_string):
    digits = []
    for char in numeric_string:
        digits.append(reverse_mapping[char])
    return digits


def n_solutions(n):
    bound = n ** n

    solutions = 0

    for ordinal in range(bound):
        solutions += test_solution(ordinal, n)

    return solutions


def test_solution(ordinal, n):
    board = []
    for i in range(n):
        board.append([False] * n)

    digits = digit_list(base_n(ordinal, n).zfill(n))

    # Check if two on the same column
    # If there are none on one column, there must be at least two on another
    for i in range(n):
        if digits.count(i) != 1:
            return False

    # Place the queens
    # Check if two are on the same diagonal
    for j in range(n):
        row = j
        column = digits[row]
        board[row][column] = True

        for k in range(j):
            distance = j - k
            upper_column = column - distance
            if upper_column >= 0:
                if board[k][upper_column]:
                    return False
            lower_column = column + distance
            if lower_column < n:
                if board[k][lower_column]:
                    return False
    return True


for i in range(1, 9):
    print(i, n_solutions(i))







