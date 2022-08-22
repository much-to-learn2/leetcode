// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut overflow: i32 = 0;
        let mut res: Option<Box<ListNode>> = Some(Box::new(ListNode::new(-1)));
        let mut currNode: &mut Option<Box<ListNode>> = &mut res;
        let mut n1 = l1.clone();
        let mut n2 = l2.clone();
        
        
        loop {
            let v1 = match n1 {
                Some(ref v) => v.val,
                None => 0
            };
            let v2 = match n2 {
                Some(ref v) => v.val,
                None => 0
            };
            let mut v = v1 + v2 + overflow;
            
            if (v >= 10) {
                v = v - 10;
                overflow = 1;
            } else {
                overflow = 0;
            }
            
            // these two lines I had to look up,
            // since Rust was pretty annoying here about ownership
            currNode.as_mut().unwrap().next = Some(Box::new(ListNode::new(v)));
            currNode = &mut currNode.as_mut().unwrap().next;
            
            n1 = match n1 {
                Some(v) => v.next,
                None => None
            };
            n2 = match n2 {
                Some(v) => v.next,
                None => None
            };
            
            if (n1 == None && n2 == None && overflow == 0) {
                break;
            }
        }
        
        res.unwrap().next
        // return l1;
    }
}
