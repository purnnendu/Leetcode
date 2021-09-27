type Node struct {
    Key int
    Val int
    Prev *Node
    Next *Node
}

type LRUCache struct {
    Capacity int
    Length int
    Head *Node
    Tail *Node
    Lookup map[int]*Node
}


func Constructor(capacity int) LRUCache {
    return LRUCache {
        Capacity: capacity,
        Lookup: make(map[int]*Node),
    }
}


func (this *LRUCache) Get(key int) int {
    /*
    - key doesn't exist
    - key exist
        - bring node to head
    */

    node, ok := this.Lookup[key]
    if !ok {
        return -1
    }

    this.bringNodeToHead(node)

    return node.Val
}

func (this *LRUCache) bringNodeToHead(node *Node) {
    /*
    - node is already head
    - node is tail
    - node is somewhere else in the list
    */

    if node == this.Head {
        // do nothing
    } else if node == this.Tail {
        this.Tail = node.Prev
        node.Prev.Next = nil
        node.Next = this.Head
        node.Prev = nil
        this.Head.Prev = node
        this.Head = node
    } else {
        node.Prev.Next = node.Next
        node.Next.Prev = node.Prev
        node.Next = this.Head
        node.Prev = nil
        this.Head.Prev = node
        this.Head = node
    }
}


func (this *LRUCache) Put(key int, value int)  {
    /*
    - key exist
        - update
        - bring node to head
    - key doesn't exist
        - create a new node
        - add to the head
        - add to lookup
        - length++

        - length > capacity
            - decrement length
            - delete tail
            - remove from lookup
    */
    node, ok := this.Lookup[key]
    if ok {
        node.Val = value
        this.bringNodeToHead(node)
        return
    }

    node = &Node {
        Key: key,
        Val: value,
    }

    if this.Head == nil {
        this.Head = node
        this.Tail = node
    } else {
        node.Next = this.Head
        this.Head.Prev = node
        this.Head = node
    }

    this.Lookup[key] = node
    this.Length++

    if this.Length > this.Capacity {
        this.Length--
        delete(this.Lookup, this.Tail.Key)

        this.Tail = this.Tail.Prev
        this.Tail.Next = nil
    }
}
