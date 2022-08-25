impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        // hashmap to hold counts of chars in magazine
        use std::collections::HashMap;
        
        let mut h = HashMap::new();
        
        for c in magazine.chars() {
            let c_count = h.entry(c).or_insert(0);
            *c_count += 1;
        }
        
        // now pass through ransom_note
        for c in ransom_note.chars() {
            let c_count = h.entry(c).and_modify(|x| *x -= 1).or_insert(-1);
            if *c_count == -1 {
                return false;
            }
        }
        return true;
    }
}
