type Solution struct {
    base []int
    r *rand.Rand
}

func Constructor(nums []int) Solution {
    return Solution{
        base: nums,
        r: rand.New(rand.NewSource(time.Now().UnixNano())),
    }
}

func (this *Solution) Reset() []int {
    return this.base
}

func (this *Solution) Shuffle() []int {
    var index int
    shuffled := make([]int, len(this.base))
    copy(shuffled, this.base)
    for i := len(this.base); i > 0; i-- {
        index = this.r.Intn(i)
        shuffled[index], shuffled[i-1] = shuffled[i-1], shuffled[index]
    }
    return shuffled
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.Reset();
 * param_2 := obj.Shuffle();
 */
