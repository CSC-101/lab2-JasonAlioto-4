# 4a
from typing import Optional

def checked_access(L:list[int], idx: int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)        # For the first call, the test does not pass. For the second call, the value is 2.
    if test:                                # The check is making sure that the index number is positive and less than the length of the list.
        return L[idx]
    else:
        return None

first = checked_access([1, 0, 1], 9)
# None
second = checked_access([1, 0, 1], 2)
# 1
print(first, second)


# 4b
def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])  # This statement is evaluated in the call: "first"
    elif len(L) > 1:                                # 4 + 2 + 3 = 9
        result = len(L[0]) + len(L[1])              # This statement is evaluated for the calls: "second" and "third"
    elif len(L) > 0:                                # "second": 6 + 1 + 4, "third": 7 + 4
        result = len(L[0])                          # This statement is not evaluated
    else:
        result = 0
    return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print(first, second, third)


# 4c
def surprising(L:list[str], other: str) -> list[str]:
    L.append(other.upper())
    return L

words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
# words: ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
# first = second = ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
# Each call to the function added two new words (in capital letters) to the list.
print(first, second)
