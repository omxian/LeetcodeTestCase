class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# [1,None,2,None,3,None,4,None,None]
def gen_tree_by_arr(arr):
    root = TreeNode(arr[0])
    roots = [root]
    is_finish = False
    for i in range(1, len(arr)):
        if is_finish:
            roots.pop(0)
        insert_root = roots[0]
        is_right = i % 2 == 0
        if is_right:
            if arr[i]:
                insert_root.right = TreeNode(arr[i])
                roots.append(insert_root.right)
        else:
            if arr[i]:
                insert_root.left = TreeNode(arr[i])
                roots.append(insert_root.left)

        is_finish = is_right

    return root


def tree_equal(tree1, tree2):
    if tree1 and tree2:
        if tree1.val != tree2.val:
            return False
        else:
            return tree_equal(tree1.left, tree2.left) and tree_equal(tree1.right, tree2.right)
    elif tree1 or tree2:
        return False
    else:
        return True
