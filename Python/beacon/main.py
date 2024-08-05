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


def sRGB_to_linear_rgb(c):
    c = c / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)

def linear_rgb_to_xyz(rgb):
    M = np.array([[0.4124564, 0.3575761, 0.1804375],
                  [0.2126729, 0.7151522, 0.0721750],
                  [0.0193339, 0.1191920, 0.9503041]])
    return np.dot(M, rgb)

def xyz_to_lab(xyz):
    xyz_ref = np.array([0.95047, 1.00000, 1.08883])  # Reference white D65
    xyz = xyz / xyz_ref
    epsilon = 0.008856
    kappa = 903.3

    def f(t):
        return np.where(t > epsilon, t ** (1/3), (kappa * t + 16) / 116)

    f_xyz = f(xyz)
    L = 116 * f_xyz[1] - 16
    a = 500 * (f_xyz[0] - f_xyz[1])
    b = 200 * (f_xyz[1] - f_xyz[2])
    return np.array([L, a, b])

def deltaE(lab1, lab2):
    return np.sqrt(np.sum((lab1 - lab2) ** 2))

def color_distance(c1, c2):
    # Convert sRGB to linear RGB
    linear_rgb1 = sRGB_to_linear_rgb(np.array(c1))
    linear_rgb2 = sRGB_to_linear_rgb(np.array(c2))

    # Convert linear RGB to XYZ
    xyz1 = linear_rgb_to_xyz(linear_rgb1)
    xyz2 = linear_rgb_to_xyz(linear_rgb2)

    # Convert XYZ to L*a*b*
    lab1 = xyz_to_lab(xyz1)
    lab2 = xyz_to_lab(xyz2)

    # Compute the Delta E distance
    return deltaE(lab1, lab2)


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

    for num_panes in range(1, 6):
        print(num_panes)
        for combo in product(color_keys, repeat=num_panes):
            dist = color_distance(color, calculate_color(combo))

            if dist < smallest_distance:
                smallest_distance = dist
                most_similar = combo

    return most_similar, smallest_distance


def print_for_color(target_color):
    red = (target_color >> 16) & 0xFF
    green = (target_color >> 8) & 0xFF
    blue = target_color & 0xFF

    target_color = np.array([red, green, blue])

    approx_color, distance = approximate_color(target_color)
    calculated_color = calculate_color(approx_color)
    print("Target Color:", target_color)
    print("Calculated Color:", calculated_color)
    print("Distance:", distance)
    print("Final Panes:", approx_color)


print_for_color(0x810081)
