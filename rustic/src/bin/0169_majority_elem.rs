use std::collections::HashMap;
struct Solution;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        return Solution::approach_2(&nums);
    }

    #[allow(dead_code)]
    fn approach_1(nums: &Vec<i32>) -> i32 {
        /*
        Use Hash Map. Count frequency of each value. Return value with highest frequency.
         */
        let n = nums.len();
        let mut counter: HashMap<i32, i32> = HashMap::new();
        for i in 0..n {
            let k = nums[i];
            match counter.get(&k) {
                Some(value) => {
                    counter.insert(k, *value+1);
                },
                None => {counter.insert(k, 1);}
            }
        }
        let max_key = Solution::get_key_with_max_val(&counter);
        return max_key;
    }

    #[allow(dead_code)]
    fn get_key_with_max_val(counter: &HashMap<i32, i32>) -> i32 {
        /*
        We know that the majority number occurs more than n/2 times. 
        So, instead of hashmap, we can just maintain a single value. 
        Increase its frequency if we encounter it again. 
        Decrease its frequency if we encounter some other value. 
        If counter goes below 0, reset current number as new result.
         */
        let mut max_key = 0;
        let mut max_val = 0;
        for (k, v) in counter.iter() {
            if *v > max_val {
                max_val = *v;
                max_key = *k;
            }
        }
        max_key
    }

    fn approach_2(nums: &Vec<i32>) -> i32 {
        let mut res = nums[0];
        let mut count = 1;
        let n = nums.len();
        for i in 1..n {
            if nums[i] == res {
                count += 1;
            } else {
                if count > 0 {
                    count -= 1;
                } else {
                    res = nums[i] as i32; 
                    count = 1;
                }
            }
        }
        return res;
    }
}


pub fn main() {
    println!("Majority elem: {}", Solution::majority_element(vec![3,2,3]));
    println!("Majority elem: {}", Solution::majority_element(vec![2,2,1,1,1,2,2]));
}