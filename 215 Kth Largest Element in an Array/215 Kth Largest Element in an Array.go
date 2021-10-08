func left (i int) int {
    return 2*i + 1
}
func right(i int) int {
    return 2*i+2
}
func parent (i int) int {
    return (i-1) / 2
}

func heapyfyMax(i int) {
    l := left(i)
    r := right(i)

    largest := i
    if l < HS && heap[l] > heap[i] {
        largest = l
    }
    if r < HS && heap[r] > heap[largest] {
        largest = r
    }

    if largest != i {
        heap[i], heap[largest] = heap[largest], heap[i]
        heapyfyMax(largest)
    }
}


func extractTop() int {
    e := 999999999
    if HS < 0 {
       return e
    }

    if HS == 1 {
        HS--
        return heap[0]
    }

    e  = heap[0]
    heap[0] = heap[HS - 1]
    HS--
    heapyfyMax(0)
    return e
}

func insert(i int) {

    HS++
    idx := HS - 1
    heap = append(heap, i)
//    fmt.Println(HS, heap)
    for ; idx != 0 && heap[parent(idx)] < heap[idx]; {
        heap[parent(idx)] , heap[idx] = heap[idx], heap[parent(idx)]
        idx = parent(idx)
    }
}
var HS int
var heap []int

func findKthLargest(nums []int, k int) int {
    HS = 0
    heap = make([]int, 0)
    for i := 0; i < len(nums); i++ {
        insert(nums[i])
    }
    ans := 0
    for  i := 0; i < k; i++ {
        //fmt.Println(heap, "-", HS)
        ans  = extractTop()

    }

    return ans
}
