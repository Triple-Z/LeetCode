func reversePrint(head *ListNode) []int {
    s := list.New()

    p := head
    for p != nil {
        s.PushBack(p.Val)
        p = p.Next
    }da

    ans := []int{}
    for s.Len() != 0 {
        ans = append(ans, s.Remove(s.Back()).(int))
    }

    return ans
}