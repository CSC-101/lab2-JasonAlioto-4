# 3a
def smallest(n:float, m:float) -> float:
    if n < m:
        return n
        # This statement is never evaluated because n is never less than m.
    else:
        return m

first = smallest(3, 2)
# First is 2.
second = smallest(2, 2)
# Second is 2. This is not a reasonable result because 2 cannot be less than 2. This function does not consider if n and m are equal.
print(first, second)

# 3b
def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b
        # This statement is only evaluated when the call's values are in descending order.
    elif b > c:
        return b + c
        # This statement is evaluated whenever the call's middle value is bigger than the last value.
    else:
        return 2 * c
        # This statement is evaluated for any case that is not the first two.

answer1 = function2(3, 2, 1)
# 1
answer2 = function2(2, 3, 1)
# 4
answer3 = function2(2, 1, 3)
# 6
print(answer1, answer2, answer3)