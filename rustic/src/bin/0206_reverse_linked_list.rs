/*
L1 -> L2 -> L3 -> L4 -> L5

L5 -> L4 -> L3 -> L2 -> L1


If I start from last, how would I iterate through previous numbers ? 
Link is unidirectional 

So, I will have to start from start and then rearrange it somehow 

prev = None 
current = head 
while current is not None {
    temp = current.next; L2
    current.next = prev; L1 -> None  
    prev = current; L1 
    current = temp; L2    
}
*/

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}
struct Solution;
impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev: Option<Box<ListNode>> = None;
        let mut current = head;
        while let Some(mut node) = current {
            let temp = node.next.take();
            node.next = prev;
            prev = Some(node);
            current = temp;
        }
        return prev;
    }
}

fn main() {
}