import sys
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())

graph = {}

for _ in range(N):
    p, c1, c2 = input().split()
    graph[p] = [c1, c2]

def preorder(node):
    if node != ".":
        output(node)
        preorder(graph[node][0])
        preorder(graph[node][1])

def inorder(node):
    if node != ".":
        inorder(graph[node][0])
        output(node)
        inorder(graph[node][1])

def postorder(node):
    if node != ".":
        postorder(graph[node][0])
        postorder(graph[node][1])
        output(node)

preorder('A')
output('\n')
inorder('A')
output('\n')
postorder('A')