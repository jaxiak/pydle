#I completed today's pydle in 5 tries, my time was 00:20:15, here is my solution:

def coding_problem_07(budget, choices):
    """
    There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a
    function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
    For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
    integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
    Example:

    >>> coding_problem_07(budget=4, choices=[1, 2])
    5
    """
    memoization = {}
    memoization[0] = 1
    for i in range(1, budget + 1):
        t = 0
        for ii in choices:
            if i - ii in memoization:
                t += memoization[i-ii]
        memoization[i] = t
    return memoization[budget]
