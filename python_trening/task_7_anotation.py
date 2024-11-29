# a: int = 5
# b: str = 'строка'
# c: list = [1, 2]
#
# def ident(s: str, width: int) -> str:
#     return ' ' * (max(0, width-len(s))) + s
#
# print(ident('123', 123))
#
# def long_str (s: str) -> int:
#     return len(s)
#
# print(long_str('qwerty'))
#
# def two_lists (a: list, b: list) -> int:
#     return max(len(a), len(b))
#
# print(two_lists([1, 2, 3, 4], ['a','f', 5, 6, 'w']))

def task_three (a: list, b) -> list:
    a.append(b)
    return a

print(task_three([1, 4, 'mother',2], 'willow'))

def task_four(a: list[int]):
    return sum(a)

print(task_four([1,2, 3, 4]))