type Trie struct {
	Value string
	Left  *Trie
	Right *Trie
}

/** Initialize your data structure here. */
func Constructor() Trie {
	return Trie{}
}

/** Inserts a word into the trie. */
func (this *Trie) Insert(word string) {
	if this.Value == "" {
		this.Value = word
		return
	}

	if word == this.Value {
		return
	}

	if word > this.Value {
		if this.Right == nil {
			this.Right = &Trie{
				Value: word,
			}
			return
		}

		this.Right.Insert(word)
		return
	}

	if this.Left == nil {
		this.Left = &Trie{
			Value: word,
		}
		return
	}

	this.Left.Insert(word)
}

/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
	if word == this.Value {
		return true
	}

	if word > this.Value {
		if this.Right == nil {
			return false
		}

		return this.Right.Search(word)
	}

	if this.Left == nil {
		return false
	}

	return this.Left.Search(word)
}

/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
	if strings.Index(this.Value, prefix) == 0 {
		return true
	}

	if prefix > this.Value {
		if this.Right == nil {
			return false
		}

		return this.Right.StartsWith(prefix)
	}

	if this.Left == nil {
		return false
	}

	return this.Left.StartsWith(prefix)
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
