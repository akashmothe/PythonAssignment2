# only applicable for n = 5
# for i in range(1,6):
#     print(11**i)


def pascal_triangle(n):
    res = [[1], [1,1]] 
    for i in range(n):
        tmp = [1]
        for j in range(len(res[-1])):
            tmp.append(res[-1][j]+res[-1][j+1])
        tmp.append(1)

        res.append(tmp)
    return res


print(pascal_triangle(3))


# Tried but not getting required output
