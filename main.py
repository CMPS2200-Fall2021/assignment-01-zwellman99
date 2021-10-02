"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        (ra,rb) = (foo(x-1)), (foo(x-2))
            rc = ra + rb
        return rc

def longest_run(mylist, key):
    streak = 0
    longest = 0
    for i in mylist:
        if i == key:
            streak += 1
        else:
            if (streak > longest):
                longest = streak
                streak = 0
            else:
                streak = 0
    return max(longest, streak)


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key

    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))

def combine_results(left_result, right_result):
    result = Result(0,0,0,False)

    if (left_result.is_entire_range == False and right_result.is_entire_range == False):

        result = Result(left_result.left_size, right_result.right_size, max(left_result.longest_size,
        right_result.longest_size, (left_result.right_size + right_result.left_size)), False)

        return result

    elif (left_result.is_entire_range == True and right_result.is_entire_range == True):

        longest = left_result.longest_size + right_result.longest_size

        result = Result(longest, longest, longest, True)

        return result

    elif (left_result.is_entire_range == True and right_result.is_entire_range == False):

        result = Result((left_result.longest_size + right_result.right_size), right_result.right_size,
                max(left_result.longest_size, right_result.longest_size,
                    (left_result.right_size + right_result.left_size)), False)

        return result

    elif (left_result.is_entire_range == False and right_result.is_entire_range == True):

        result = Result(left_result.left_size, (right_result.longest_size + left_result.right_size),
                    max(left_result.longest_size, right_result.longest_size,
                    (left_result.right_size + right_result.left_size)), False)

        return result

def longest_run_recursive(mylist, key):
    ### TODO
    if len(mylist == 1):
        if mylist[0] == key:
            result1 = Result(1, 1, 1, True)
            return result1
        else:
            result2 = Result(0, 0, 0, False)
            return result2

    left_result = longest_run_recursive(mylist[:len(mylist) // 2], key)
    right_result = longest_run_recursive(mylist[len(mylist) // 2:], key)

    return combine_results(left_result, right_result)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
