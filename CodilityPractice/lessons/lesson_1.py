MAX_INT = 2_147_483_647


def binary_gap(n):

    assert isinstance(n, int)
    assert 1 <= n <= MAX_INT, f'Invalid N given: {n} of type {type(n)}. Should be 1 <= int <= {MAX_INT}'

    binary_string = bin(n)[2:]  # removes binary chars 0b from start

    max_gap = 0

    idxs = []
    for idx, char in enumerate(binary_string):
        if char == '1':
            idxs.append(idx)

    for i in range(len(idxs) - 1):
        gap = idxs[i+1] - idxs[i] - 1

        max_gap = gap if gap > max_gap else max_gap

    return max_gap


