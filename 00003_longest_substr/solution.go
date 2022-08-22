import (
    "strings"
)

func lengthOfLongestSubstring(s string) int {
    i, j := 0, 0
    h := make(map[string]int)
    buffer := ""
    winner := ""
    
    for j < len(s) {
        c := string(s[j])
        if !strings.Contains(buffer, c) {
            buffer += c
            h[c] = j
            j += 1
        } else {
            i = h[c] + 1
            if len(buffer) > len(winner) {
                winner = buffer
            }
            buffer = s[i:j]
            h[c] = j
        }
    }
    
    if len(buffer) > len(winner) {
        winner = buffer
    }
    
    return len(winner)
}
