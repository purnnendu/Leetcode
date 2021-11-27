func myPow(x float64, n int) float64 {
    var ret float64
	switch {
	case n == 1:
		ret = x
	case n == 0:
		ret = 1.0
	case n >= 2:
		halfPower := myPow(x, n/2)
		ret = halfPower * halfPower
		if (n % 2) == 1 {
			ret *= x
		}
	default:
		ret = 1 / myPow(x, -n)
	}
    return ret
}
