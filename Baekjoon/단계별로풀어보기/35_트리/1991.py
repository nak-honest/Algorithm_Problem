import sys

N = int(input())

tree = dict()

root_node, l, r = sys.stdin.readline().split()
tree[root_node] = [l, r]

for _ in range(N-1):
    p, l, r = sys.stdin.readline().split()
    tree[p] = [l, r]


def preorder(root):
    if root == '.':
        return
    print(root, end='')
    preorder(tree[root][0])
    preorder(tree[root][1])


def inorder(root):
    if root == '.':
        return
    inorder(tree[root][0])
    print(root, end='')
    inorder(tree[root][1])


def postorder(root):
    if root == '.':
        return
    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root, end='')


preorder(root_node)
print()
inorder(root_node)
print()
postorder(root_node)