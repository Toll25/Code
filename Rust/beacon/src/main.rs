use ndarray::{array, Array1};
use std::collections::HashMap;

fn main() {
    let colors: HashMap<&str, [u8; 3]> = [
        ("white", [249, 255, 254]),
        ("light_gray", [157, 157, 151]),
        ("gray", [71, 79, 82]),
        ("black", [29, 29, 33]),
        ("brown", [131, 84, 50]),
        ("red", [176, 46, 38]),
        ("orange", [249, 128, 29]),
        ("yellow", [254, 216, 61]),
        ("lime", [128, 199, 31]),
        ("green", [94, 124, 22]),
        ("cyan", [22, 156, 156]),
        ("light_blue", [58, 179, 218]),
        ("blue", [60, 68, 170]),
        ("purple", [137, 50, 184]),
        ("magenta", [199, 78, 189]),
        ("pink", [243, 139, 170]),
    ]
    .iter()
    .cloned()
    .collect();

    let target_color = 0x00ffff;
    print_for_color(target_color, &colors);
}

fn s_rgb_to_linear_rgb(c: &[f64; 3]) -> [f64; 3] {
    let c: Vec<f64> = c.iter().map(|&x| x / 255.0).collect();
    let result: Vec<f64> = c
        .iter()
        .map(|&x| {
            if x <= 0.04045 {
                x / 12.92
            } else {
                ((x + 0.055) / 1.055).powf(2.4)
            }
        })
        .collect();
    [result[0], result[1], result[2]]
}

fn linear_rgb_to_xyz(rgb: &[f64; 3]) -> [f64; 3] {
    let m = array![
        [0.4124564, 0.3575761, 0.1804375],
        [0.2126729, 0.7151522, 0.0721750],
        [0.0193339, 0.1191920, 0.9503041]
    ];
    let rgb = array![rgb[0], rgb[1], rgb[2]];
    let xyz = m.dot(&rgb);
    [xyz[0], xyz[1], xyz[2]]
}

fn xyz_to_lab(xyz: &[f64; 3]) -> [f64; 3] {
    let xyz_ref = array![0.95047, 1.00000, 1.08883];
    let xyz: Array1<f64> = array![xyz[0], xyz[1], xyz[2]] / &xyz_ref;
    let epsilon = 0.008856;
    let kappa = 903.3;

    let f = |t: f64| {
        if t > epsilon {
            t.powf(1.0 / 3.0)
        } else {
            (kappa * t + 16.0) / 116.0
        }
    };
    let f_xyz = xyz.mapv(f);
    let l = 116.0 * f_xyz[1] - 16.0;
    let a = 500.0 * (f_xyz[0] - f_xyz[1]);
    let b = 200.0 * (f_xyz[1] - f_xyz[2]);
    [l, a, b]
}

fn delta_e(lab1: &[f64; 3], lab2: &[f64; 3]) -> f64 {
    ((lab1[0] - lab2[0]).powi(2) + (lab1[1] - lab2[1]).powi(2) + (lab1[2] - lab2[2]).powi(2)).sqrt()
}

fn color_distance(c1: &[f64; 3], c2: &[f64; 3]) -> f64 {
    // Convert sRGB to linear RGB
    let linear_rgb1 = s_rgb_to_linear_rgb(c1);
    let linear_rgb2 = s_rgb_to_linear_rgb(c2);

    // Convert linear RGB to XYZ
    let xyz1 = linear_rgb_to_xyz(&linear_rgb1);
    let xyz2 = linear_rgb_to_xyz(&linear_rgb2);

    // Convert XYZ to L*a*b*
    let lab1 = xyz_to_lab(&xyz1);
    let lab2 = xyz_to_lab(&xyz2);

    // Compute the Delta E distance
    delta_e(&lab1, &lab2)
}

fn calculate_color(panes: Vec<&str>, colors: &HashMap<&str, [u8; 3]>) -> [f64; 3] {
    let n = panes.len();
    if n == 0 {
        return [0.0, 0.0, 0.0];
    }

    let mut sum_colors = [0.0, 0.0, 0.0];

    for (i, pane) in panes.iter().enumerate().skip(1) {
        let weight = 2u32.pow((i - 1) as u32) as f64;
        let color = colors.get(*pane).unwrap();
        sum_colors[0] += weight * color[0] as f64;
        sum_colors[1] += weight * color[1] as f64;
        sum_colors[2] += weight * color[2] as f64;
    }

    let first_color = colors.get(panes[0]).unwrap();
    sum_colors[0] += first_color[0] as f64;
    sum_colors[1] += first_color[1] as f64;
    sum_colors[2] += first_color[2] as f64;

    let scaling_factor = 1.0 / (2u32.pow((n - 1) as u32) as f64);

    [
        scaling_factor * sum_colors[0],
        scaling_factor * sum_colors[1],
        scaling_factor * sum_colors[2],
    ]
}

fn generate_combinations<'a>(
    current_depth: usize,
    max_depth: usize,
    current_combination: &mut Vec<&'a str>, // Change to Vec<&'a str>
    possibilities: &'a HashMap<&'a str, [u8; 3]>,
    distance: &mut f64,
    most_similar: &mut Vec<&'a str>,
    target_color_u8: [u8; 3],
) -> (f64, Vec<&'a str>) {
    if current_depth == max_depth {
        let target_color: [f64; 3] = [
            target_color_u8[0] as f64,
            target_color_u8[1] as f64,
            target_color_u8[2] as f64,
        ];

        // Calculate current color and its distance from target
        let current_color = calculate_color(current_combination.clone(), possibilities);
        let dist = color_distance(&target_color, &current_color);

        // Update most_similar and distance if current combination is closer
        if dist < *distance {
            *distance = dist;
            *most_similar = current_combination.clone();
        }

        // Return the current distance for comparison
        return (dist, most_similar.to_vec());
    }

    let mut min_distance = std::f64::INFINITY;

    for (key, _) in possibilities.iter() {
        // Append the current possibility to the combination
        current_combination.push(key);

        // Recursive call to generate combinations at the next depth
        let (dist, _) = generate_combinations(
            current_depth + 1,
            max_depth,
            current_combination,
            possibilities,
            distance,
            most_similar,
            target_color_u8,
        );

        // Track the minimum distance found in the recursive calls
        if dist < min_distance {
            min_distance = dist;
        }

        // Backtrack: Remove the last added possibility to try the next one
        current_combination.pop();
    }

    (min_distance, most_similar.to_vec()) // Return the minimum distance found in this depth level
}

fn generate_all_combinations<'a>(
    max_depth: usize,
    possibilities: &'a HashMap<&'a str, [u8; 3]>,
    target_color: [u8; 3],
) -> (f64, Vec<&'a str>) {
    let mut initial_combination = Vec::new();
    let (most_similar, smallest_distance) = generate_combinations(
        0,
        max_depth,
        &mut initial_combination,
        possibilities,
        &mut f64::INFINITY,
        &mut vec![],
        target_color,
    );

    (most_similar, smallest_distance)
}

fn print_for_color(target_color: u32, colors: &HashMap<&str, [u8; 3]>) {
    let red = ((target_color >> 16) & 0xFF) as u8;
    let green = ((target_color >> 8) & 0xFF) as u8;
    let blue = (target_color & 0xFF) as u8;

    let target_color = [red, green, blue];

    let (distance, approx_color) = generate_all_combinations(5, colors, target_color);
    let calculated_color = calculate_color(approx_color.clone(), colors);

    println!("Target Color: {:?}", target_color);
    println!("Calculated Color: {:?}", calculated_color);
    println!("Distance: {}", distance);
    println!("Final Panes: {:?}", approx_color);
}
