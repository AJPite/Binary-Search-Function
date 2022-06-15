def has_duplicates(t):
    if len(t) < 2:
        return False
    t.sort()
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False

def move_divider_right(ls, index):
    if len(ls) == 1:
        return 1
    if len(ls) % 2 == 0:
        del ls[:len(ls)//2]
    else:
        del ls[:len(ls)//2 + 1]
    return len(ls) // 2

def move_divider_left(ls, index):
    if len(ls) == 1:
        return 1
    if len(ls) % 2 == 0:
        del ls[len(ls)//2:]
    else:
        del ls[len(ls)//2 + 1:]
    return len(ls) // 2

def bisect(ls, target):
    copy = ls[:]
    divider_ls = []
    divider = len(ls)//2
    while True:
        if target == ls[divider]:
            return divider
        if target > ls[divider]:
            divider += move_divider_right(copy, divider)
        if target < ls[divider]:
            divider -= move_divider_left(copy, divider)
        divider_ls.append(divider)
        if has_duplicates(divider_ls):
            return None
