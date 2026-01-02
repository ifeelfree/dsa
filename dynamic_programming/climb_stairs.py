class SolutionNative:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class SolutionMemo:
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        if n <= 2:
            return n

        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = result
        return result


class SolutionIterative:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        two_steps_back = 1
        one_step_back = 2

        for i in range(3, n + 1):
            current_ways = one_step_back + two_steps_back
            two_steps_back = one_step_back
            one_step_back = current_ways

        return one_step_back

from functools import lru_cache

class SolutionLRUCache:
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)