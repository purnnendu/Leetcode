func dailyTemperatures(T []int) []int {
    type Tuple struct {
    Temp int
    Index int
}

    // initialize slice to store result
    res := make( []int, len(T))
    // stack to store tuple of {Temp, Index}
    var stack [] Tuple

    // iterating in reverse order
    for i:= len(T)-1;  i>=0 ; i-- {
        // initialize the value at current index of res to be 0
        res[i] = 0

        // current temp
        temp:=T[i]
        for (len(stack)>0) && (temp>= stack[len(stack)-1].Temp){
            //pop from stack, if the top of stack has a temperature lower than the current
            stack= stack[:len(stack)-1]
        }

        if len(stack)>0{
            // set value to be the difference between the
            // current index and the index of the temperature we found to be higher
            res[i]=stack[len(stack)-1].Index - i
        }
        // push current temp and index to stack
        stack=append(stack, Tuple{Temp: temp, Index: i })
    }
    return res

}
