"""Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return 
its content in string format."""
"""We model the file system using a tree structure:

Each node is either a file (has content) or a directory (has children).

Use a FileSystemNode class to represent files/directories.

Use a FileSystem class to implement the required methods."""

class FileSystemNode:
    def __init__(self):
        self.is_file = False
        self.children = {}
        self.content = ''

        
class FileSystem:
    def __init__(self):
        self.root = FileSystemNode()
        self.cwd = '/'
        
    # Create a core internal helper to navigate through a path like /a/b/c and optionally creating missing files or directories during traversal
    def _traverse(self, path, create=False, make_file=False):
        curr = self.root
        if path == '/':
            return curr
        
        # Remove trailing and leading slashes and split the part by /
        parts = path.strip('/').split('/')
        for i, part in enumerate(parts):
            if part not in curr.children:
                if not create:
                    raise ValueError(f'Path {path} does not exist')               
                curr.children[part] = FileSystemNode()            
            curr = curr.children[part]
        
        if make_file:
            curr.is_file = True
        
        return curr
        
    def ls(self, path=None):
        if path is None:
            return self.cwd
        
        curr = self._traverse(path)
        if curr is None:
            return []
        
        # If the path is a file, return its name
        if curr.is_file:
            return [path.split('/')[-1]]
        
        # If it is a directory, return sorted lit of names
        return sorted(curr.children.keys())
    
    def mkdir(self, path):
        self._traverse(path, create=True)
        
    def addContentToFile(self, filePath, content):
        curr = self._traverse(filePath, create=True, make_file=True)
        curr.content += content
        
    def readContentFromFile(self, filePath):
        curr = self._traverse(filePath)
        if not curr.is_file:
            raise ValueError(f'{filePath} is not a file')
        return curr.content
    
    # How would you support deleting a file or directory?
    # Ans: At the parent directory, remove the child from its children dict

    def delete(self, path):
        if path == '/':
            raise ValueError('Cannot delete the root directory')
        
        parts = path.strip('/').split('/')
        *dirs, target = parts
        
        parent = self._traverse('/' + '/'.join(dirs))
        if parent is None or target not in parent.children:
            raise FileNotFoundError(f"Path '{path}' does not exist")
        
        del parent.children[target]

    
fs = FileSystem()
fs.mkdir("/a/b/c")
fs.addContentToFile("/a/b/c/d", "hello")
print(fs.ls("/"))           # ['a']
print(fs.ls("/a/b/c"))      # ['d']
print(fs.readContentFromFile("/a/b/c/d"))  # 'hello'
# fs.delete('/')