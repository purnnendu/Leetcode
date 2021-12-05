func canCompleteCircuit(gas []int, cost []int) int {
	n := len(gas)
	sub := 0
	min := 0
	ans := 0
	for i := 0; i < n; i++ {
		sub += gas[i] - cost[i]
		if sub < min {
			ans = i + 1
			min = sub
		}
	}
	if sub >= 0 {
		return ans
	} else {
		return -1
	}
}
