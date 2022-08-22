tion for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

    var node1 *ListNode = l1;
    var node2 *ListNode = l2;
    var overflow = 0;
    var currNode *ListNode = nil;
    var res *ListNode;


    for (node1 != nil || node2 != nil || overflow != 0) {

        var v1, v2 int;
        if node1 != nil {
            v1 = node1.Val;
        } else {
            v1 = 0;
        }
        if node2 != nil {
            v2 = node2.Val;
        } else {
            v2 = 0;
        }

        v := v1 + v2 + overflow;
        if v >= 10 {
            overflow = 1;
            v = v - 10;
        } else {
            overflow = 0;
        }

        if currNode == nil {
            currNode = &ListNode{Val: v, Next: nil};
            res = currNode;
        } else {
            currNode.Next = &ListNode{Val: v, Next: nil};
            currNode = currNode.Next;
        }



        if node1 != nil {
            node1 = node1.Next
        }
        if node2 != nil {
            node2 = node2.Next
        }
    }

    return res;
}
