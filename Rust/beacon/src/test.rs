fn generate_combinations(
    current_depth: usize,
    max_depth: usize,
    current_combination: &mut Vec<usize>,
    possibilities: &[usize],
) {
    if current_depth == max_depth {
        // Print or process the current combination
        //println!("{:?}", current_combination);
        return;
    }

    for &possibility in possibilities {
        // Append the current possibility to the combination
        current_combination.push(possibility);

        // Recursive call to generate combinations at the next depth
        generate_combinations(
            current_depth + 1,
            max_depth,
            current_combination,
            possibilities,
        );

        // Backtrack: Remove the last added possibility to try the next one
        current_combination.pop();
    }
}

fn generate_all_combinations(max_depth: usize, possibilities: &[usize]) {
    let mut initial_combination = Vec::new();
    generate_combinations(0, max_depth, &mut initial_combination, possibilities);
}

fn main() {
    let possibilities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14];
    let max_depth = 7; // Set the depth of combinations you want to generate

    generate_all_combinations(max_depth, &possibilities);
}
