stack = []

def reverse_order(r):
    visited = [False] * len(nodes)
    stack.append(r)

    while stack:
        node = stack[-1]
        if left[node] != -1 and not visited[left[node]]:
            stack.append(left[node])
        elif right[node] != -1 and not visited[right[node]]:
            stack.append(right[node])
        else:
            print(nodes[node])
            stack.pop()
            visited[node] = True

nodes = list(map(int, open(0).read().split()))

'''
nodes = []
for _ in range(9):
    nodes.append(int(input()))
'''

root = 0
left = [-1] * len(nodes)
right = [-1] * len(nodes)
parent = [-1] * len(nodes)

prev = 0
for i in range(1, len(nodes)):
    if nodes[prev] > nodes[i]:
        left[prev] = i
        parent[i] = prev
    else:
        while parent[prev] != -1 and nodes[parent[prev]] < nodes[i]:
            prev = parent[prev]

        while right[prev] != -1:
            prev = right[prev]

        right[prev] = i
        parent[i] = prev

    prev = i

# print(left)
# print(right)
# print(parent)
reverse_order(root)