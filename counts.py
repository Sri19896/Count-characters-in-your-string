def count(str):
    s = {}
    for i in set(str):
        s.update({i: str.count(i)})
    return(s)


print(count("aabb"))
