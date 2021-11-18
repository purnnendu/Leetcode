func firstUniqChar(s string) int {
  counter := make([]int, 26)

  for _, r := range s {
    charIdx := r - 'a'
    counter[charIdx] += 1
  }

  for idx, r := range s {
    charIdx := r - 'a'
    count := counter[charIdx]
    if count == 1 {
      return idx
    }
  }

    return -1
}
