n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}


def identify(node1, node2, node3):
    union = n1.keys() | n2.keys() | n3.keys()
    intersections = n1.keys() & n2.keys() & n3.keys()
    relevant = union - intersections
    res = {
        key: (node1.get(key, 0), node2.get(key, 0), node3.get(key, 0))
        for key in relevant
    }
    return res


print(identify(n1, n2, n3))
