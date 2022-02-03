from collections import Counter

def SeparateElements(l):
    unique = set(l)
    # for freuency of elements
    ele_counts = Counter(l)
    # getting the only elements whoes frequency is more than 1
    duplicates = list([item for item in ele_counts if ele_counts[item]>1])
    return f"Unique: {list(unique)}\nDuplicates: {duplicates}"


lst = [1, 2, 3, 4, 3, 2, 1 ,5]
print(SeparateElements(lst))

