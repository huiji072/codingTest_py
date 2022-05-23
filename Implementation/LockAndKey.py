def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]

