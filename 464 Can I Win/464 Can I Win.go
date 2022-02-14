func canIWin(maxChoosableInteger int, desiredTotal int) bool {
	var sum int
	for val := 1; val <= maxChoosableInteger; val++ {
		sum += val
	}
	if sum < desiredTotal {
		return false
	}
	if desiredTotal <= maxChoosableInteger {
		return true
	}
	mem := make([]byte, (1<<(maxChoosableInteger+1))-1)
	res := findWinner(mem, 0, maxChoosableInteger, 0, desiredTotal, 0) == 0
	return res
}

// findWinner finds the winner. Returns 0 if the first player wins, otherwise 1.
func findWinner(mem []byte, bm, max, sum, desiredTotal int, player byte) byte {
	if sum >= desiredTotal {
		return (player + 1) & 1
	}
	if mem[bm] != 0 {
		return mem[bm] - 1
	}
	// If any move is guaranteed to win, then this round is a win
	for i := 1; i <= max; i++ {
		if bm&(1<<i) > 0 {
			continue
		}
		winner := findWinner(mem, bm|(1<<i), max, sum+i, desiredTotal, (player+1)&1)
		if winner == player {
			mem[bm] = player + 1
			return player
		}
	}
	// No move could make this player win - return a loss
	mem[bm] = (player+1)&1 + 1
	return mem[bm] - 1
}
