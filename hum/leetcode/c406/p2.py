# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


from typing import List, Optional


class Solution:
  def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    s = set(nums)
    res = []
    tmp = head
    while tmp:
      if tmp.val not in s:
        res.append(tmp.val)
      tmp = tmp.next
    h = ListNode(res[0])
    t = h
    for i in range(1, len(res)):
      h.next = ListNode(res[i])
      h = h.next
    return t
