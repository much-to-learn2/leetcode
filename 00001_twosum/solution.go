func twoSum(nums []int, target int) []int {
    var m = make(map[int]int);

    for i, d := range nums {
        var complement = target - d;
        complement_idx, ok := m[complement];
        if ok {
            return []int{i, complement_idx}
        }

        m[d] = i;
    }

    return []int{}
}
