'''
dwed
'''
# properties of a node: data, left, right
def pre_order(node):
    '''
    Returns the tree traversal in preorder
    '''
    lyst = []

    def recurse(node):
        if node is not None:
            lyst.append(node.data)
            recurse(node.left)
            recurse(node.right)

    recurse(node)
    return lyst


# In-order traversal
def in_order(node):
    '''
    Returns the tree traversal in inorder
    '''
    lyst = []

    def recurse(node):
        if node is not None:
            recurse(node.left) # does nothing when there is no left son
            lyst.append(node.data) # appends "on the way back"
            recurse(node.right)

    recurse(node)
    return lyst

# Post-order traversal
def post_order(node):
    '''
    Returns the tree traversal in postorder
    '''
    lyst = []

    def recurse(node):
        if node is not None:
            recurse(node.left)
            recurse(node.right)
            lyst.append(node.data)

    recurse(node)
    return lyst
