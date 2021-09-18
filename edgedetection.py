import numpy as np


COLOR_DIFFERENCE_THRESHOLD = 60


def calc_surrounding_coords(x, y, width, height):
    coords = []

    if y - 1 >= 0:
        coords.append([x, y - 1])
        if x - 1 >= 0:
            coords.append([x - 1, y - 1])
        if x + 1 < width:
            coords.append([x + 1, y - 1])

    if y + 1 < height:
        coords.append([x, y + 1])
        if x - 1 >= 0:
            coords.append([x - 1, y + 1])
        if x + 1 < width:
            coords.append([x + 1, y + 1])

    if x - 1 >= 0:
        coords.append([x - 1, y])
    if x + 1 < width:
        coords.append([x + 1, y])

    return coords


def edge_detection(arr: np.array):
    width = len(arr[0])
    height = len(arr)

    newarr = np.zeros((height, width), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            coords = calc_surrounding_coords(x, y, width, height)
            for i in coords:
                if abs(int(arr[i[1]][i[0]]) - int(arr[y][x])) > COLOR_DIFFERENCE_THRESHOLD:
                    newarr[y][x] = 255
    return newarr
