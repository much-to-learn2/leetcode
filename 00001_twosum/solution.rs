impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        use std::collections::HashMap;
        
        let mut h: HashMap<i32, i32> = HashMap::new();
        for (i, d) in nums.iter().enumerate() {
            let complement: i32 = target - d;
            if h.contains_key(&complement) {
                return [i as i32, h[&complement]].to_vec();
            }
            
            h.insert(*d, i as i32);
        }
        
        return Vec::new();
        
    }
}
