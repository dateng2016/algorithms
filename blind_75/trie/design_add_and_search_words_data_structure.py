# R ->    Worst case assume everything is dot
# S -> the entire trie


class Node:
    def __init__(self) -> None:
        self.children = dict()
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def helper(node: Node, word: str) -> bool:
            if not word:
                return node.is_end
            cur = node
            for i in range(len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children:
                        if helper(cur.children[child], word[i + 1 :]):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.is_end

        return helper(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

