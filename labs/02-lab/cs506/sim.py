def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])**1
    return res

def jaccard_dist(x, y):
    intersection = []
    union = []
    for i in range(len(x)):
        if x[i] == y[i]:
            intersection.append(x[i])
        if x[i] not in union:
            union.append(x[i])
        if y[i] not in union:
            union.append(y[i])

    if union == []:
        return 0

    return 1 - len(intersection) / len(union)

def cosine_sim(x, y):
    dot_product = 0
    x_length = 0
    y_length = 0
    for i in range(len(x)):
        dot_product += x[i] * y[i]
        x_length += x[i] ** 2
        y_length += y[i] ** 2
    
    x_length = x_length ** (1/2)
    y_length = y_length ** (1/2)

    if x_length == 0 or y_length == 0:
        return 0
    
    return dot_product / (x_length * y_length)
    

# Feel free to add more
