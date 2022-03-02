/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
      ListNode dummy = new ListNode();
      ListNode temp = dummy;
      int carry = 0;  
      while(l1 != null || l2 != null){
          int l1val = (l1 != null) ? l1.val : 0;
          int l2val = (l2 != null) ? l2.val : 0;
          int sum = l1val + l2val + carry;
          temp.next = new ListNode(sum%10);
          l1 = (l1 != null ) ? l1.next : null;
          l2 = (l2 != null ) ? l2.next : null;
          temp = temp.next;
          carry = sum/10;
      }
      if(carry != 0) temp.next = new ListNode(carry);
      return dummy.next;
        
    }
    
    
}
/*
st: 10:17
    
    2 -> 4 -> 3
    5 -> 6 -> 4 
    
    7 -> 0 -> 8 
    
    (342)
   +(465)
     807 
            


*/