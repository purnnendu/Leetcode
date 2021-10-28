func partitionLabels(s string) []int {
    lastSeen := make([]int, 128)
    for i,ch := range s {
        lastSeen[ch-'a'] = i
    }
    result := []int{}

    startingLastseen := -1
    prevlastSeen := 0
    for i := 0; i < len(s); i++ {
        j := lastSeen[s[i]-'a']
        startingLastseen = int(math.Max(float64(startingLastseen), float64(j)))

        if i == startingLastseen {
            result = append(result, (startingLastseen - prevlastSeen) +1)
            prevlastSeen = startingLastseen+1
            startingLastseen = -1
        }

    }

    return result
}
