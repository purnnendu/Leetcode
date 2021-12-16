func increasingTriplet(nums []int) bool {
  smallBin, mediumBin := math.MaxInt32, math.MaxInt32
	for _, num := range nums {
		if num <= smallBin {
			smallBin = num
		} else if num <= mediumBin {
			mediumBin = num
		} else { // if not using "or equal to" above, must be num > mediumBin
			return true
		}
	}
  return false
}
