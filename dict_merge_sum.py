def dict_merge_sum(d1, d2):
    m ={}
    keys = set(d1.keys()).union(set(d2.keys()))
    print(keys)

    for k in keys:
        m[k] = d1.get(k,0)+d2.get(k,0)
    return m
d1={'apple':400, 'banana':20, 'bisuit':39, 'mango':100}
d2={'apple':40, 'banana':20, 'bisuit':39}
result = dict_merge_sum(d1, d2)

print(result)
