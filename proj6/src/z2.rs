use rand::prelude::*;
use std::cmp::{max, min};
use std::fs::File;
use std::io::prelude::*;

pub const MAX_ITER: usize = 10000;
pub const TSTART: f64 = 0.001;

pub type Point = (i32, i32);
pub type Cycle = Vec<Point>;

fn get_starting_cycle(points: &Cycle) -> Cycle {
    let mut rng = rand::thread_rng();
    let mut cycle = vec![(0, 0); points.len() as usize];
    let mut used = [false; 150];
    let mut i = 0;
    while i < 150 {
        let j = rng.gen_range(0..(points.len() as usize));
        if !used[j] {
            cycle[i] = points[j];
            used[j] = true;
            i += 1;
        }
    }
    cycle
}

fn change_points(cycle: &Cycle) -> Cycle {
    // let mut new_cycle = P.clone();
    let mut rng = rand::thread_rng();

    let i = rng.gen_range(0..(cycle.len() as usize - 1));
    let j = rng.gen_range(0..(cycle.len() as usize - 1));

    let a = min(i, j);
    let b = a + 1;
    let c = max(i, j);
    let d = c + 1;

    if a == c || a == d || b == c {
        return change_points(&cycle);
    }

    let mut i = 0;
    let mut new_cycle = vec![(0, 0); cycle.len() as usize];

    for k in 0..=a {
        new_cycle[i] = cycle[k];
        i += 1;
    }
    for k in (b..=c).rev() {
        new_cycle[i] = cycle[k];
        i += 1;
    }
    for k in d..(cycle.len() - 1 as usize) {
        new_cycle[i] = cycle[k];
        i += 1;
    }
    new_cycle
}

fn get_cycle_length(cycle: &Cycle) -> f64 {
    let mut length = 0 as f64;
    for i in 0..149 {
        let (x1, y1) = cycle[i];
        let (x2, y2) = cycle[i + 1];
        length += (((x1 - x2).pow(2) + (y1 - y2).pow(2)) as f64).sqrt();
    }
    let (x1, y1) = cycle[149];
    let (x2, y2) = cycle[0];
    length += (((x1 - x2).pow(2) + (y1 - y2).pow(2)) as f64).sqrt();
    length
}

pub fn simulated_annealing(points: Cycle) -> Cycle {
    let mut cycle = get_starting_cycle(&points);
    for i in (1..=100).rev() {
        let temperature = TSTART * f64::powi(i as f64, 2);
        for _ in 0..MAX_ITER {
            let new_cycle = change_points(&cycle);
            let delta = get_cycle_length(&new_cycle) - get_cycle_length(&cycle);
            if delta < 0. {
                cycle = new_cycle;
            } else {
                let p = (-delta as f64 / temperature).exp();
                let r = rand::thread_rng().gen_range(0.0..1.0);
                if r < p {
                    cycle = new_cycle;
                }
            }
        }
    }
    print!("{}\n", get_cycle_length(&cycle)); // 1875.8931705675216
    cycle
}

pub fn get_data() -> Cycle {
    // let mut f = File::open("input_150.dat").expect("File not found");
    let mut f = File::open("z2.txt").expect("File not found");
    let mut contents = String::new();
    f.read_to_string(&mut contents)
        .expect("Something went wrong reading the file");
    let mut lines = contents.lines();
    let mut data = Vec::new();
    for _ in 0..150 {
        let line = lines.next().unwrap();
        let mut nums = line.split_whitespace();
        let x = nums.next().unwrap().parse::<i32>().unwrap();
        let y = nums.next().unwrap().parse::<i32>().unwrap();
        data.push((x, y));
    }
    data
}
