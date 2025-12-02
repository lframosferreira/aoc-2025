def invalid(id):
    if len(id)%2==1:
        return False
    sz=len(id)/2
    x=int(id)%(10**sz)
    y=int(id)//(10**sz)
    if x==y:
        return True
    return False



inp = input()
ranges = map(lambda x: x.split("-"), inp.split(","))
cnt=0
for id1, id2 in ranges:
    for id in range(int(id1), int(id2)+1):
        if invalid(str(id)):
            cnt+=id
print(cnt)
