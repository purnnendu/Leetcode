func jump(nums []int) int {
    curJump, farthestJump, jumps := 0, 0, 0
	for i := 0; i < len(nums)-1; i++ {
	    // push index of furthest jump during current iteration
		if i+nums[i] > farthestJump {
			farthestJump = i + nums[i]
		}

		// if current iteration is ended - setup the next one
		if i == curJump {
			jumps, curJump = jumps+1, farthestJump

			if curJump >= len(nums)-1 {
				return jumps
			}
		}
	}

	// it's guaranteed to never hit it
    return 0
}
