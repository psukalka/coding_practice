struct Solution;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        return Self::approach_2(&nums, target);
    }

    #[warn(dead_code)]
    pub fn approach_1(nums: &Vec<i32>, target: i32) -> Vec<i32> {
        let n = nums.len();
        for i in 0..n {
            for j in (i+1)..n{
                if nums[i] + nums[j] == target {
                    return vec![i as i32, j as i32];
                }
            }
        }
        return vec![];
    }

    pub fn approach_2(nums: &Vec<i32>, target: i32) -> Vec<i32> {
        let n = nums.len();
        let sorted = {
            let mut cloned = nums.to_vec();
            cloned.sort();
            cloned
        };
        let mut ci = 0;
        let mut cj = n-1;
        while ci < cj {
            if sorted[ci] + sorted[cj] > target {
                cj = cj - 1;
            } else if sorted[ci] + sorted[cj] < target {
                ci = ci + 1;
            } else {
                break;
            }
        }
        let mut i: i32 = -1;
        let mut j: i32 = -1;
        for k in 0..n {
            if nums[k] == sorted[ci] && i == -1 {
                i = k as i32;
            }
            else if nums[k] == sorted[cj] && j == -1 {
                j = k as i32;
            }
        }
        return vec![i, j];
    }
}

fn main() {
    let result = Solution::two_sum(vec![2,11,7,15], 9);
    println!("{:?}", result);
    
}