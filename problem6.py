
def List_to_Dict(l,r):
    res = {}
    for key in r:
        # converting string values to list of integers
        rng_tup = list(map(int, key.split("-")))
        # appending the values from list l to dict which are in range of key from list r
        res[key] = [val for val in l if val in range(rng_tup[0],rng_tup[-1])]
    return res
            
lst = [15, 16, 20, 35, 25, 45, 41]
rng = ['0-10','10-20','20-30','30-40','40-50']

print(List_to_Dict(lst,rng))