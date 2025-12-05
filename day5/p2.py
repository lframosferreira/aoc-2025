from sys import stdin

ranges = []
ans=0;
for line in stdin:
    line=line[:-1]
    if "-" in line:
        ranges.append(list(map(lambda x: int(x), line.split("-"))))

ranges.sort()
cl, cr = ranges[0]
for l, r in ranges[1:]:
    if l <= cr and r <= cr:
        continue
    if l <= cr:
        cr = r
        continue
    ans+=cr-cl+1
    cl=l
    cr=r
ans+=cr-cl+1
print(ans)

