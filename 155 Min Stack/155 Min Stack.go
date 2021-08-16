type MinStack struct {
    elements []*MinStackElement
}


type MinStackElement struct {
    Val int
    Minimum int
}

/** initialize your data structure here. */
func Constructor() MinStack {
    return MinStack{elements: make([]*MinStackElement, 0, 50 )}
}


func (this *MinStack) Push(val int)  {
    newElem := &MinStackElement{Val: val}


    if len(this.elements) > 0 {
        prevMin := this.elements[len(this.elements)-1].Minimum
        if val < prevMin {
            newElem.Minimum = val
        } else {
            newElem.Minimum = prevMin
        }
    } else {
        newElem.Minimum = val
    }


    this.elements = append(this.elements, newElem)


    return
}


func (this *MinStack) Pop()  {
    this.elements = this.elements[0:len(this.elements)-1]
}


func (this *MinStack) Top() int {
    return this.elements[len(this.elements)-1].Val
}


func (this *MinStack) GetMin() int {
    return this.elements[len(this.elements)-1].Minimum
}
