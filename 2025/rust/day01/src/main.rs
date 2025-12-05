static DATA: &str = include_str!("../../../day01.txt");

fn main() {
    let mut dial = 50;
    let mut code1 = 0;
    let mut code2 = 0;

    for line in DATA.lines() {
        let amount: i32 = (if &line[..1] == "L" { -1 } else { 1 }) * &line[1..].parse().unwrap();
        let end = dial + amount;
        let mut zeroes = (end / 100).abs();

        if dial != 0 && end <= 0 {
            zeroes += 1;
        }

        dial = end.rem_euclid(100);

        if dial == 0 {
            code1 += 1;
        }

        code2 += zeroes;
    }

    println!("{}\n{}", code1, code2);
}
