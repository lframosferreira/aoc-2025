from sys import stdin

ranges = []
ans=0;
for line in stdin:
    line=line[:-1]
    if "-" in line:
        ranges.append(list(map(lambda x: int(x), line.split("-"))))
        continue
    if line == "":
        continue
    n = int(line)
    for l, r in ranges:
        if n >= l and n <= r:
            ans+=1
            break
print(ans)

