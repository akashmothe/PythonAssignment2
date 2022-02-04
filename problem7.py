
def pascal_triangle(n):
    res = [] # outer main list
    # first getting required output as nested list
    for i in range(n):
        row = [] # inner list
        for j in range(i+1):
            # first and last value is 1
            # so getting it using j value and appending there as 1
            if j == 0 or j == i:
                row.append(1)
            else:                                    
                # accessing privious row by i-1 
                # getting index of column by j value. 
                # i.e by adding j'th index and privious value of j'th index  
                row.append(res[i-1][j-1] + res[i-1][j]) 
        res.append(row)
    return res

# for printing above nested list in required shape
def print_triangle(l):
    for i in l:
        for j in i:
            print(j, end=' ')
        print()

n = int(input("Enter the number: "))
print_triangle(pascal_triangle(n))


# only applicable for n = 5

# for i in range(1,6):
#     print(11**i)
