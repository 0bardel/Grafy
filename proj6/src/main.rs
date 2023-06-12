mod z2;

use std::io::Write;

fn main() {
    let data = z2::get_data();
    let P = z2::simulated_annealing(data);
    let mut file = std::fs::File::create("z2.txt").unwrap();
    for i in 0..P.len() {
        let (x, y) = P[i];
        file.write_all(format!("{} {}\n", x, y).as_bytes()).unwrap();
    }
}
