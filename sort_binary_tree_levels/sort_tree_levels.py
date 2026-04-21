'''
Module with function for the sorting of a tree by levels
'''

def tree_by_levels(node):
    '''
    Function for the sorting of a tree by levels
    '''
    if node is None:
        return []
    lyst = [node]

    def add_children(node):
        if node is None:
            pass
        if node.left is not None:
            lyst.append(node.left)
        if node.right is not None:
            lyst.append(node.right)

    i = 0
    while i < len(lyst):
        add_children(lyst[i])
        i += 1

    return [node.value for node in lyst]
