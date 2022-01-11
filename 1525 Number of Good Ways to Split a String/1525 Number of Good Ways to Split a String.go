type CharSet struct {
    chars []int
    size int
}

func NewCharSet() *CharSet {
    return &CharSet{
        chars: make([]int, 26),
        size: 0,
    }
}

func (s *CharSet) Add(char byte) {
    index := char - 'a'

    if s.chars[index] == 0 {
        s.size++
    }

    s.chars[index]++
}

func (s *CharSet) Remove(char byte) {
    index := char - 'a'

    if s.chars[index] == 0 {
        return
    }

    if s.chars[index] == 1 {
        s.size--
    }

    s.chars[index]--
}

func (s *CharSet) Size() int {
    return s.size
}


func numSplits(s string) int {
    n := len(s)
    leftSet, rightSet := NewCharSet(), NewCharSet()

    for i := 0; i < n; i++ {
        rightSet.Add(s[i])
    }

    count := 0
    for i := 0; i < n; i++ {
        rightSet.Remove(s[i])
        leftSet.Add(s[i])

        if leftSet.Size() == rightSet.Size() {
            count++
        }
    }

    return count
}
