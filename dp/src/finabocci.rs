const MAX_NUM: usize = 100000;

struct Fibonacci {
    dp: [i32; MAX_NUM],
}

impl Fibonacci {
    fn new() -> Self {
        Fibonacci { dp: [-1; MAX_NUM] }
    }

    fn calc(&mut self, n: i32) -> i32 {
        if self.dp[n as usize] != -1 {
            return self.dp[n as usize];
        } else {
            self.dp[n as usize] = self.calc(n - 1) + self.calc(n - 2);
            return self.dp[n as usize];
        }
    }

    fn fib(&mut self, n: i32) -> i32 {
        self.dp[0] = 0;
        self.dp[1] = 1;
        let ans = self.calc(n);
        return ans;
        }
    }



fn main() {
    let mut n: Vec<i32> = Vec::new();
    println!("Hello, world!");
}

#[test]
fn test_fibonacci() {
    let mut f = Fibonacci::new();
    assert_eq!(f.fib(0), 0);
    assert_eq!(f.fib(1), 1);
    assert_eq!(f.calc(2), 1);
    assert_eq!(f.calc(3), 2);
    assert_eq!(f.calc(4), 3);
    assert_eq!(f.calc(10), 55);
}
