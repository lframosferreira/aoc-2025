from sys import stdin
g = dict()
nodes = set()

for line in stdin:
    line=line[:-1].split()
    u = line[0][:-1]
    if u not in g.keys():
        g[u]=[]
    nodes.add(u)
    for v in line[1:]:
        g[u].append(v)
        nodes.add(v)

ans=0
def dfs(u):
    global ans
    if u == "out":
        ans+=1
        return
    for v in g[u]:
        dfs(v)

dfs("you")


print(ans)
