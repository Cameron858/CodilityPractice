

def cycle_array(array: list, n: int):

    assert isinstance(array, list)
    assert isinstance(n, int)

    array_length = len(array)
    shifted_array = array.copy()

    for shifts in range(n):
        new = [shifted_array[-1]]

        for i in range(array_length - 1):
            new.append(shifted_array[i])

        shifted_array = new.copy()

    return shifted_array
