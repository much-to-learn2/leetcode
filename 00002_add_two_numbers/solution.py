# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        overflow = 0
        currNode = None
        
        while (node1 is not None or node2 is not None or overflow != 0):
            v1 = node1.val if node1 else 0
            v2 = node2.val if node2 else 0
            v = v1 + v2 + overflow
            overflow = 1 if v >= 10 else 0
            v = v - 10 if overflow == 1 else v

            if currNode is None:
                currNode = ListNode(v)
                res = currNode
            else:
                currNode.next = ListNode(v)
                currNode = currNode.next
                
            
            
            # go next
            node1 = node1 and node1.next
            node2 = node2 and node2.next
            
        return res
