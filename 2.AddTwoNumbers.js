/**
 * LeetCode 2. Add Two Numbers (A)
 * 
 * Runtime: 100 ms
 * Memory: 38.9 MB
 * 
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  let s = 0
  let c = 0
  let hook = {val: null, next: null}
  let l = hook
  
  while (l1 != null && l2 != null) {
      s = l1.val + l2.val + c
      
      c = s > 9 ? 1 : 0
      l.next = {val: s > 9 ? s - 10 : s, next: null}
      l = l.next
      
      l1 = l1.next
      l2 = l2.next
  }
  
  let tmp = (l1 != null) ? l1 : l2
  while (tmp) {
      s = tmp.val + c
      
      c = s > 9 ? 1 : 0
      l.next = {val: s > 9 ? s - 10 : s, next: null}
      l = l.next
      
      tmp = tmp.next
  }
  
  if (c) {
      l.next = {val: c, next: null}
      l = l.next
  }
  
  return hook.next
};


/**
 * LeetCode 2. Add Two Numbers (B)
 * 
 * Runtime: 128 ms
 * Memory: 39.1 MB
 * 
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  let s = 0
  let c = 0
  let acc = []
  
  while (l1 != null && l2 != null) {
      s = l1.val + l2.val + c
      c = s > 9 ? 1 : 0
      acc.push(s > 9 ? s - 10 : s)
      
      l1 = l1.next
      l2 = l2.next
  }
  
  let tmp = (l1 != null) ? l1 : l2
  while (tmp != null) {
      s = tmp.val + c
      c = s > 9 ? 1 : 0
      acc.push(s > 9 ? s - 10 : s)
      
      tmp = tmp.next
  }

  let l = c ? {val: c, next: null} : null
  for (let i = acc.length-1; i >= 0; i--) {
      l = {val: acc[i], next: l}
  }
  
  return l
};


/**
 * LeetCode 2. Add Two Numbers (C)
 * 
 * Runtime: 164 ms
 * Memory: 39 MB
 * 
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  let s = 0
  let c = 0
  let hook = {val: null, next: null}
  let l = hook
  
  while (l1 || l2) {
      let a = l1 ? l1.val : 0
      let b = l2 ? l2.val : 0
      s = a + b + c
      
      c = s > 9 ? 1 : 0
      l.next = {val: s > 9 ? s - 10 : s, next: null}
      l = l.next
      
      l1 = l1 && l1.next
      l2 = l2 && l2.next;
  }
  
  if (c) {
      l.next = {val: 1, next: null}
      l = l.next
  }
  
  return hook.next
};