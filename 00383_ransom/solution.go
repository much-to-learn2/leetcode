func canConstruct(ransomNote string, magazine string) bool {
    hm :=  make(map[rune]int)
    for _, d := range magazine {
        if count, ok := hm[d]; ok {
            hm[d] = count + 1
        } else {
            hm[d] = 0
        }
    }

    for _, d := range ransomNote {
        count, ok := hm[d]
        if ! ok || count == -1 {
            return false
        } else {
            hm[d] = count - 1
        }
    }

    return true
}
