"""
# Intuition

Repeatedly replacing a number with the sum of the squares of its digits produces a sequence.

This sequence will eventually do one of two things:

1. Reach `1`, which means the number is happy.
2. Repeat a previously encountered value, which means the sequence has entered a cycle and will never reach `1`.

We can use a set to store previously encountered values and detect when a cycle occurs.

# Approach

1. Initialize a set containing the original number.
2. Calculate the sum of the squares of all digits in the current number.
3. If the calculated sum is `1`, return `True`.
4. If the calculated sum already exists in the set, a cycle has been detected, so return `False`.
5. Otherwise, add the calculated sum to the set.
6. Assign the calculated sum to `n` and repeat the process.

# Complexity

- Time complexity: $$O(k \log n)$$

  Here, `k` is the number of generated values before the sequence reaches `1` or enters a cycle. Calculating the next value requires processing every digit of the current number.

- Space complexity: $$O(k)$$

  The set stores up to `k` distinct values before the process terminates.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}

        while True:
            sum_of_squares = 0

            while n > 0:
                digit = n % 10
                sum_of_squares += digit * digit
                n //= 10

            if sum_of_squares == 1:
                return True

            if sum_of_squares in seen:
                return False

            seen.add(sum_of_squares)
            n = sum_of_squares