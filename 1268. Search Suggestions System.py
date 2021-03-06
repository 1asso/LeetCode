Optimized brute force:

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        for i in range(len(searchWord)):
            products = [s for s in products if s.startswith(searchWord[:i+1])]
            res.append(products[:3])
        return res
        
        
Binary search:

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prefix, start, res = '', 0, []
        for c in searchWord:
            prefix += c
            start = bisect.bisect_left(products, prefix, start)
            res.append([w for w in products[start: start+3] if w.startswith(prefix)])
        return res
        
Trie:

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        word_key = '$'
        trie = {}
        for product in products:
            cur = trie
            for c in product:
                cur = cur.setdefault(c, {})
                if word_key not in cur:
                    cur[word_key] = []
                cur[word_key].append(product)
                cur[word_key].sort()
                if len(cur[word_key]) > 3:
                    cur[word_key].pop()
        res = []
        for c in searchWord:
            if trie:
                trie = trie.get(c, None)
            res.append(trie[word_key] if trie else [])
        return res
        

OR:

class Trie:
    def __init__(self):
        self.children = {}
        self.value = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for product in products:
            self._insert(product, root)
        return self._search(searchWord, root)
            
    def _insert(self, product, root):
        for c in product:
            if c not in root.children:
                root.children[c] = Trie()
            root = root.children[c]
            root.value.append(product)
            root.value.sort()
            if len(root.value) > 3:
                root.value.pop()
    
    def _search(self, w, root):
        res = []
        for c in w:
            if root:
                root = root.children.get(c)
            res.append(root.value if root else [])
        return res
