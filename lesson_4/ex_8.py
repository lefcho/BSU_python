def check_average(list1, list2):
    if not list1 or not list2:
        return False
    avg1 = sum(list1) / len(list1)
    avg2 = sum(list2) / len(list2)
    return avg1 == avg2


print(check_average([1, 2, 3], [2, 2, 2]))
print(check_average([1, 2], [3, 4]))