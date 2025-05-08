""""You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them."""
from collections import defaultdict

def longestPath(parent, s):
    # Build the tree as an adjacency list
    tree = defaultdict(list)
    for child, par in enumerate(parent):
        if par != -1:
            tree[par].append(child)
            
    longest = [0]
    
    def dfs(node):
        max1 = max2 = 0
        
        for child in tree[node]:
            child_len = dfs(child)
            
            if s[child] != s[node]:
                if child_len > max1:
                    max2 = max1
                    max1 = child_len
                elif child_len > max2:
                    max2 = child_len
                    
        longest[0] = max(longest[0], 1 + max1 + max2)
        
        return 1 + max1
    
    dfs(0)
    
    return longest[0]
     

# Example usage
parent = [-1,0,0,1,1,2]
s = "abacbe"
print(longestPath(parent, s))