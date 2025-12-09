from sys import stdin

lines = []
for line in stdin:
    line=line[:-1]
    line = line.split()
    lines.append(list(map(lambda x: x.strip(), line)))
op = lines[-1]
acc = list(map(lambda x: int(x) ,lines[0]))
lines=lines[1:len(lines)-1]
for j in range(len(lines[0])):
    for i in range(len(lines)):
        if op[j]=="+":
            acc[j]+=int(lines[i][j])
        else:
            acc[j] *= int(lines[i][j])

print(sum(acc))
