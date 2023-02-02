def reverseList(lst):
    """
    Reverse the order of a list.
    """
    res = []
    for i in range(len(lst)-1, -1, -1):
        res.append(lst[i])
    return res


x = [1, 2, 3, 4, 5]
print(reverseList(x))
