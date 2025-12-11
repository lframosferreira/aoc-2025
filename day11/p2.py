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
fft=False
dac=False
def dfs(u):
    global ans
    global fft
    global dac
    if u == "out":
        if fft and dac:
            ans+=1
        return
    for v in g[u]:
        if v == "fft":
            fft=True
            dfs(v)
            fft=False
        elif v == "dac":
            dac=True
            dfs(v)
            dac=False
        else:
            dfs(v)
dfs("svr")


print(ans)
