func lengthOfLongestSubstring(s string) int {
    i, j := 0, 0
    rs := []rune(s)
    
    h := make(map[rune]int)
    buffer := []rune("")
    winner := []rune("")
    
    for j < len(rs) {
        c := rs[j]
        if !containsRune(buffer, c) {
            buffer = append(buffer, c)
            h[c] = j
            j += 1
        } else {
            i = h[c] + 1
            if len(buffer) > len(winner) {
                winner = buffer
            }
            buffer = rs[i:j]
            h[c] = j
        }
    }
    
    if len(buffer) > len(winner) {
        winner = buffer
    }
    
    return len(winner)
}

func containsRune(rs []rune, r rune) bool {
    for i := 0; i < len(rs); i++ {
        if r == rs[i] {
            return true
        }
    }
    return false
}
