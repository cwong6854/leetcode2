class ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

var reorderList = function (head) {
  // slow and fast?
  if (!head) return null;
  let slow = head;
  let fast = head.next;
  // get half of list
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }
  // slow is our half -> reverse
  let second = slow.next;
  slow.next = null;
  // reverse the half
  let reverse = second ? new ListNode(second.val) : null;
  while (second && second.next) {
    reverse = new ListNode(second.next.val, reverse);
    second = second.next;
  }

  let [prev, latter] = [head, reverse];
  while (latter) {
    let tmp1 = head.next;
    let tmp2 = latter.next;
    prev.next = latter;
    latter.next = tmp1;
    prev = tmp1;
    latter = tmp2;
  }
};
let x = ListNode(1, ListNode(2, ListNode(3, ListNode(4))));
reorderList(x);
