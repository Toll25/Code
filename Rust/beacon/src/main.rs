use itertools::Itertools;
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

    let target_color = 0x1DB954;
    print_for_color(target_color, &colors);

    let rainbow_colors = generate_rainbow_pattern(&colors, 100);
    for (target_color, panes, final_color) in rainbow_colors {
        println!(
            "Target Color: {:?}, Approximated Panes: {:?}, Calculated Color: {:?}",
            target_color, panes, final_color
        );
    }
}

fn color_distance(c1: &[u8; 3], c2: &[f64; 3]) -> f64 {
    ((c1[0] as f64 - c2[0] as f64).powi(2)
        + (c1[1] as f64 - c2[1] as f64).powi(2)
        + (c1[2] as f64 - c2[2] as f64).powi(2))
    .sqrt()
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

fn approximate_color<'a>(
    target_color: [u8; 3],
    colors: &'a HashMap<&'a str, [u8; 3]>,
    max_panes: usize,
) -> Vec<&'a str> {
    let color_keys: Vec<&str> = colors.keys().cloned().collect();
    let mut most_similar = vec![];
    let mut smallest_distance = f64::INFINITY;

    for num_panes in 1..=max_panes {
        for combo in color_keys.iter().combinations(num_panes) {
            let result: Vec<&str> = combo.into_iter().cloned().collect();

            if result.len() > 1 && result.iter().all_equal() {
                continue;
            }

            let dist = color_distance(&target_color, &calculate_color(result.clone(), colors));

            if dist < smallest_distance {
                smallest_distance = dist;
                most_similar = result;
            }
        }
    }

    most_similar
}

fn print_for_color(target_color: u32, colors: &HashMap<&str, [u8; 3]>) {
    let red = ((target_color >> 16) & 0xFF) as u8;
    let green = ((target_color >> 8) & 0xFF) as u8;
    let blue = (target_color & 0xFF) as u8;

    let target_color = [red, green, blue];

    let approx_color = approximate_color(target_color, colors, 12);
    let calculated_color = calculate_color(approx_color.clone(), colors);

    println!("Target Color: {:?}", target_color);
    println!("Calculated Color: {:?}", calculated_color);
    println!("Final Panes: {:?}", approx_color);
}

fn generate_rainbow_pattern<'a>(
    colors: &'a HashMap<&'a str, [u8; 3]>,
    granularity: usize,
) -> Vec<([u8; 3], Vec<&'a str>, [f64; 3])> {
    let mut pattern = vec![];
    let step = 1.0 / granularity as f64;

    for i in 0..granularity {
        let ratio = i as f64 * step;
        let r = (ratio * 255.0) as u8;
        let g = ((1.0 - ratio) * 255.0) as u8;
        let b = 127;

        let target_color = [r, g, b];
        let panes = approximate_color(target_color, colors, 12);
        let final_color = calculate_color(panes.clone(), colors);

        pattern.push((target_color, panes, final_color));
    }

    pattern
}
