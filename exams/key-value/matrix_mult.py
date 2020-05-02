def hadamard_product(a, b):
    """Return the Hadamard product of matrices a and b"""
    x = []
    # iterate through indices
    for i in range(len(a)):
        x.append([])
        for j in range(len(a[0])):
            # x(i,j) = a(i,j) * b(i,j)
            # but clamp x(i,j) at 255
            x[i].append(min(255, a[i][j] * b[i][j]))
    return x

if __name__ == '__main__':
    a = [
            [1,2,3],
            [2,3,4],
            [3,4,5]
    ]
    b = [
            [0,1,0],
            [1,0,1],
            [0,1,0]
    ]
    b12 = [
            [0,1,0],
            [1,2005,1],
            [0,1,0]
    ]
    print(hadamard_product(a,b))
    print(hadamard_product(a,b12))

