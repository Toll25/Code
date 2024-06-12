import numpy as np
from itertools import product

colors = {
    "white": np.array([249, 255, 254]),
    "light_gray": np.array([157, 157, 151]),
    "gray": np.array([71, 79, 82]),
    "black": np.array([29, 29, 33]),
    "brown": np.array([131, 84, 50]),
    "red": np.array([176, 46, 38]),
    "orange": np.array([249, 128, 29]),
    "yellow": np.array([254, 216, 61]),
    "lime": np.array([128, 199, 31]),
    "green": np.array([94, 124, 22]),
    "cyan": np.array([22, 156, 156]),
    "light_blue": np.array([58, 179, 218]),
    "blue": np.array([60, 68, 170]),
    "purple": np.array([137, 50, 184]),
    "magenta": np.array([199, 78, 189]),
    "pink": np.array([243, 139, 170]),
}


def color_distance(c1, c2):
    return np.sqrt(np.sum((np.array(c1) - np.array(c2)) ** 2))


def calculate_color(panes):
    n = len(panes)
    if n == 0:
        return np.array([0, 0, 0], dtype=np.uint8)

    sum_colors = np.zeros(3)

    for i in range(1, n):
        weight = pow(2, i - 1)
        sum_colors += weight * colors[panes[i]]

    sum_colors += colors[panes[0]]

    scaling_factor = (1 / (pow(2, n - 1)))

    final_color = scaling_factor * sum_colors

    return final_color


def approximate_color(color):
    color_keys = list(colors.keys())
    most_similar = None
    smallest_distance = float('inf')

    for num_panes in range(1, 7):
        for combo in product(color_keys, repeat=num_panes):
            dist = color_distance(color, calculate_color(combo))

            if dist < smallest_distance:
                smallest_distance = dist
                most_similar = combo

    return most_similar


def print_for_color(target_color):
    red = (target_color >> 16) & 0xFF
    green = (target_color >> 8) & 0xFF
    blue = target_color & 0xFF

    target_color = np.array([red, green, blue])

    approx_color = approximate_color(target_color)
    calculated_color = calculate_color(approx_color)
    print("Target Color:", target_color)
    print("Calculated Color:", calculated_color)
    print("Final Panes:", approx_color)


print_for_color(0x1DB954)
