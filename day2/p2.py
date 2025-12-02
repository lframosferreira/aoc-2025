def invalid(id):
    d = 1
    while d <= len(id)//2:
        if len(id)%d !=0:
            d+=1
            continue
        s = [id[i:i+d] for i in range(0, len(id), d)]
        
        if len(set(s))==1:
             return True
        d+=1
    return False



inp = input()
ranges = map(lambda x: x.split("-"), inp.split(","))
cnt=0
for id1, id2 in ranges:
    for id in range(int(id1), int(id2)+1):
        if invalid(str(id)):
            cnt+=id
print(cnt)
