from typing import List, Set


class TrieNode:
    def __init__(self) -> None:
        self.is_end = False
        self.children = {}


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """Build a Trie first -> Check all possibilities"""
        self.trie = TrieNode()

        def add_word(word: str):
            cur = self.trie
            for ch in word:
                if ch in cur.children:
                    cur = cur.children[ch]
                else:
                    new_child = TrieNode()
                    cur.children[ch] = new_child
                    cur = new_child
            cur.is_end = True

        for w in words:
            add_word(w)

        res = set()
        dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        def helper(node: TrieNode, i, j, cur_word):
            # * (i, j) are being used, node's char represents board[i][j]
            if node.is_end:
                res.add(cur_word)
            # * Visit the current point
            temp = board[i][j]
            board[i][j] = "*"
            for di, dj in dirs:
                ii, jj = i + di, j + dj
                if ii < 0 or jj < 0 or ii >= len(board) or jj >= len(board[0]):
                    continue
                next_char = board[ii][jj]
                if next_char in node.children:
                    nxt_node = node.children[next_char]
                    helper(nxt_node, ii, jj, cur_word + board[ii][jj])
            board[i][j] = temp

        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in self.trie.children:
                    helper(self.trie.children[board[i][j]], i, j, board[i][j])
        return list(res)
