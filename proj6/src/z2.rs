use rand::prelude::*;
use std::cmp::*;
use std::fs::File;
use std::io::prelude::*;

pub const MAX_ITER: usize = 1000000;
pub const TStart: f64 = 0.1;

pub type Point = (i32, i32);
pub type Cycle = Vec<Point>;

fn get_starting_cycle(V: &Cycle) -> Cycle {
    let mut rng = rand::thread_rng();
    let mut P = vec![(0, 0); V.len() as usize];
    let mut used = [false; 150];
    let mut i = 0;
    while i < 150 {
        let j = rng.gen_range(0..(V.len() as usize));
        if !used[j] {
            P[i] = V[j];
            used[j] = true;
            i += 1;
        }
    }
    P
}

fn change_edges(P: &Cycle) -> Cycle {
    // let mut Pnew = P.clone();
    let mut rng = rand::thread_rng();

    let i = rng.gen_range(0..(P.len() as usize - 1));
    let j = rng.gen_range(0..(P.len() as usize - 1));

    let a = min(i, j);
    let b = a + 1;
    let c = max(i, j);
    let d = c + 1;

    if a == c || a == d || b == c {
        return change_edges(&P);
    }

    let mut Pnew = vec![(0, 0); P.len() as usize];
    for k in 0..=a {
        Pnew[k] = P[k];
    }
    for k in (b..=c).rev() {
        Pnew[k] = P[k];
    }
    for k in d..(P.len() as usize) {
        Pnew[k] = P[k];
    }
    Pnew
}

fn get_cycle_length(P: &Cycle) -> f64 {
    let mut length = 0 as f64;
    for i in 0..149 {
        let (x1, y1) = P[i];
        let (x2, y2) = P[i + 1];
        length += (((x1 - x2).pow(2) + (y1 - y2).pow(2)) as f64).sqrt();
    }
    let (x1, y1) = P[149];
    let (x2, y2) = P[0];
    length += (((x1 - x2).pow(2) + (y1 - y2).pow(2)) as f64).sqrt();
    length
}

pub fn simulated_annealing(V: Cycle) -> Cycle {
    let mut P = get_starting_cycle(&V);
    for i in (1..=100).rev() {
        let T = TStart * f64::powi(i as f64, 2);
        for _ in 0..MAX_ITER {
            let Pnew = change_edges(&P);
            let delta = get_cycle_length(&Pnew) - get_cycle_length(&P);
            if delta < 0. {
                P = Pnew;
            } else {
                let p = (-delta as f64 / T).exp();
                let r = rand::thread_rng().gen_range(0.0..1.0);
                if r < p {
                    P = Pnew;
                }
            }
        }
    }
    P
}

pub fn get_data() -> Cycle {
    let mut f = File::open("input_150.dat").expect("File not found");
    let mut contents = String::new();
    f.read_to_string(&mut contents)
        .expect("Something went wrong reading the file");
    let mut lines = contents.lines();
    let mut data = Vec::new();
    for i in 0..150 {
        let line = lines.next().unwrap();
        let mut nums = line.split_whitespace();
        let x = nums.next().unwrap().parse::<i32>().unwrap();
        let y = nums.next().unwrap().parse::<i32>().unwrap();
        data.push((x, y));
    }
    data
}
