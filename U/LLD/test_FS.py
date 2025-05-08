class FileSystemNode:
    def __init__(self):
        self.is_file = False
        self.children = {}
        self.content = ''
    
        
class FileSystem:
    def __init__(self):
        self.root = FileSystemNode()
        self.cwd = '/'
    
        
    def _traverse(self, path: str, create=False, make_file=False):
        curr = self.root
        if path == '/':
            return curr
        
        parts = path.strip('/').split('/')
        for i, part in enumerate(parts):
            if part not in curr.children:
                if not create:
                    raise ValueError('Invlaid path')
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
        if curr.is_file:
            return [path.split('/')[-1]]
        return sorted(curr.children.keys())
    
    
    def mkdir(self, path: str):
        self._traverse(path, create=True)
        
    
    def addContentToFile(self, path: str, content: str):
        curr = self._traverse(path, create=True, make_file=True)
        curr.content += content
        
    
    def readContentFromFile(self, path: str):
        curr = self._travers(path)
        if curr is None or not curr.is_file:
            return ''
        return curr.content
    
    
    def cd(self, path):
        if not path.startswith('/'):
            path = self.cwd.rstrip('/') + '/' + path
        
        node = self._traverse(path)
        if node is None or node.is_file:
            raise FileNotFoundError(f"No such directory: {path}")
        
        self.cwd = '/' + '/'.join(path.strip('/').split('/')) if path != '' else '/'
    
            
    def pwd(self):    
        return self.cwd
    
    
    def delete(self, path: str):
        if path == '/':
            raise ValueError("Cannot delete root directory")
        
        parts = path.strip('/').split('/')
        *dirs, target = parts
        
        parent = self._traverse('/' + '/'.join(dirs))
        if parent is None or target not in parent.children:
            raise FileNotFoundError(f"Path '{path}' does not exist")
        
        del parent.children[target]
    

fs = FileSystem()
fs.mkdir('/a/b/c')
fs.cd('a')        # relative → becomes '/a'
print(fs.pwd())   # '/a'
fs.cd('b/c')      # relative → becomes '/a/b/c'
print(fs.pwd())   # '/a/b/c'
fs.cd('/')        # absolute path
print(fs.pwd())   # '/'
