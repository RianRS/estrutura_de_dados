nodeChildren = {
    1: [2, 3],
    2: [4, 5],
    5: [8, 9],
    3: [6, 7]
}
elements = []
levels = []

def traverseNode(node, level = 0):
    elements.append(node)
    levels.append(level)
    if node in nodeChildren:
        for child in nodeChildren[node]:
            traverseNode(child, level + 1)
            elements.append(node)
            levels.append(level)
traverseNode(1)
print(f'node elements: {elements}')
print(f'levels: {levels}')