class TrieNode:
    
    def __init__(self):
        self.content = ''
        self.children = defaultdict(TrieNode)
        self.isfile = False

class FileSystem:

    def __init__(self):
        self.trie = TrieNode()

    def ls(self, path: str) -> List[str]:
        node, p = self._traverse(path, False)
        if node.isfile:
            return [p]
        return sorted([d for d in node.children.keys()]) if node else []

    def mkdir(self, path: str) -> None:
        self._traverse(path, True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node, _ = self._traverse(filePath, True)
        node.content += content
        node.isfile = True

    def readContentFromFile(self, filePath: str) -> str:
        node, _ = self._traverse(filePath, True)
        return node.content
    
    def _traverse(self, path, create_path):
        path = path.split('/')
        node = self.trie
        for p in path:
            if not p:
                continue
            if not node:
                return None, None
            if create_path:
                node = node.children[p]
            else:
                node = node.children.get(p)
        return node, p


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)


Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.
List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.
The answer should in lexicographic order.
void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing given content.
If filePath already exists, appends the given content to original content.
String readContentFromFile(String filePath) Returns the content in the file at filePath.
 

Example 1:


Input
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output
[null, [], null, null, ["a"], "hello"]

Explanation
FileSystem fileSystem = new FileSystem();
fileSystem.ls("/");                         // return []
fileSystem.mkdir("/a/b/c");
fileSystem.addContentToFile("/a/b/c/d", "hello");
fileSystem.ls("/");                         // return ["a"]
fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"