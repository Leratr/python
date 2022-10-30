def Sort(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if dist(lst[i]) > dist(lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
    return lst

def dist(point):
    return (point[0]**2+point[1]**2)**0.5

def kClosest(points, k):
    Sort(points)
    return points[:k]


print(kClosest([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]], 3))



