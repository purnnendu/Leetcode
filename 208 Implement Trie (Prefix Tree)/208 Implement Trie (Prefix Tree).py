"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
"""
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        def helper( char, table ):

            if char not in table:
                table[char] = {}


            return table[char]

        # -----------------------

        # update new word into trie
        table = self.trie
        for char in word:
            table = helper( char, table)

        # use '@' as ending symbol
        table['@'] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        def helper( char, table):

            if char in table:
                return table[char]
            else:
                return None

        # -----------------------

        # search word in trie
        table = self.trie

        for char in word:
            table = helper( char, table)

            if table is None:
                return False

        # use ending symbol to judge whether current word exist in our trie or not
        return ( '@' in table )
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        def helper( char, table):

            if char in table:
                return table[char]
            else:
                return None

        # -----------------------

        # check the prefix exist in trie or not
        table = self.trie

        for char in prefix:
            table = helper( char, table)

            if table is None:
                return False

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
