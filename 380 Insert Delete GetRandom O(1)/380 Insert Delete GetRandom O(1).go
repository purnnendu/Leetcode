type RandomizedSet struct {
	numsMap   map[int]int
	numsArray []int
}

/** Initialize your data structure here. */
func Constructor() RandomizedSet {
	return RandomizedSet{numsArray: []int{}, numsMap: make(map[int]int)}
}

/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.numsMap[val]; ok {
		return false
	}

	this.numsMap[val] = len(this.numsArray)
	this.numsArray = append(this.numsArray, val)
	return true
}

/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {
	index, ok := this.numsMap[val];
	if !ok {
		return false;
	}

	last := this.numsArray[len(this.numsArray)-1]
	if val == last { // if we are removing the last element in the array, we don't need to swap and update index in map
		this.numsArray = this.numsArray[:len(this.numsArray)-1]
	} else {
		// swap and remove the last element makes the delete of the element O(1)
		this.numsArray[index] = last
		this.numsArray = this.numsArray[:len(this.numsArray)-1]
		// note: we also need to update the index of the last element in the map
		this.numsMap[this.numsArray[index]] = index
	}
	delete(this.numsMap, val)
	return true
}

/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
	index := rand.Intn(len(this.numsArray))

	return this.numsArray[index]
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
