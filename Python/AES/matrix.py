def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i + 4]) for i in range(0, len(text), 4)]


def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    new_string = ""
    for array in matrix:
        for element in array:
            print(chr(element))
            new_string += (chr(element))
    return new_string


state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    r = []
    for (a, b) in zip(s, k):
        x = []
        for (c, d) in zip(a, b):
            x.append(c ^ d)
        r.append(x)
    return r

#print(matrix2bytes(add_round_key(state, round_key)))


matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

# print(matrix2bytes(matrix))
