# Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

# You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

# Here are the specific rules:

# The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
# The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
# If less than 3 hot sentences exist, return as many as you can.
# When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
# Implement the AutocompleteSystem class:

# AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
# List<String> input(char c) This indicates that the user typed the character c.
# Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
# Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than 3 matches, return them all.
 

# Example 1:

# Input
# ["AutocompleteSystem", "input", "input", "input", "input"]
# [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
# Output
# [null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

# Explanation
# AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
# obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
# obj.input(" "); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
# obj.input("a"); // return []. There are no sentences that have prefix "i a".
# obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.



class Trie:
    def __init__(self):
        self.children = {}
        self.value = []
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Trie()
        self.count = {}
        self.keyword = ''
        self.cur_node = self.root
        for i in range(len(sentences)):
            self._insert(sentences[i])
            self.count[sentences[i]] = -times[i]
    
    def _insert(self, s):
        cur = self.root
        for c in s:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
            cur.value.append(s)

    def input(self, c: str) -> List[str]:
        if c == '#':
            if self.keyword in self.count:
                self.count[self.keyword] -= 1
            else:
                self.count[self.keyword] = -1
                self._insert(self.keyword)
            self.keyword = ''
            self.cur_node = self.root
            return []
        self.keyword += c
        if self.cur_node:
            self.cur_node = self.cur_node.children.get(c)
        if not self.cur_node:
            return []
        res = sorted([[w, self.count[w]] for w in self.cur_node.value], \
                     key=lambda x: (x[1], x[0]))
        res = [k for k, v in res][:3]
        return res
        

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
