'''bubble sort'''

def bubble_sort_while(lst:list[int]) -> list[int]:
    '''using while loop'''
    go_on = True
    while go_on:
        go_on = False
        for index in range(len(lst)-1):
            if lst[index] > lst[index+1]:
                lst[index], lst[index+1] = lst[index+1], lst[index]
                go_on = True
    return lst

assert bubble_sort_while([1,67,3,7,3,1,34,654,143,6,8,2,9]) == \
    [1, 1, 2, 3, 3, 6, 7, 8, 9, 34, 67, 143, 654]

def bubble_sort_enum(lst:list[int]) -> list[int]:
    '''using enumerate method'''
    go_on = True
    while go_on:
        go_on = False
        for index, number in enumerate(lst[:-1]):
            if lst[index] > lst[index+1]:
                lst[index], lst[index+1] = lst[index+1], lst[index]
                go_on = True
    return lst

assert bubble_sort_enum([1,67,3,7,3,1,34,654,143,6,8,2,9]) == \
    [1, 1, 2, 3, 3, 6, 7, 8, 9, 34, 67, 143, 654]