mod z2;

use std::io::Write;

fn main() {
    let data = z2::get_data();
    let cycle = z2::simulated_annealing(data);
    let mut file = std::fs::File::create("z2.txt").unwrap();
    for i in 0..cycle.len() {
        let (x, y) = cycle[i];
        file.write_all(format!("{} {}\n", x, y).as_bytes()).unwrap();
    }
}
