# link to leet code https://leetcode.com/problems/climbing-stairs/solution/

import unittest
from parameterized import parameterized

def climbStairsRecursive(totalSteps: int) -> int:
    def recursiveClimbStairs(currentStep = 0):
        if currentStep > totalSteps:
            return 0
        if currentStep == totalSteps:
            return 1
        return recursiveClimbStairs(currentStep + 1) + recursiveClimbStairs(currentStep + 2)
    return recursiveClimbStairs()


def climbStairsMemoized(totalSteps: int) -> int:
    memo = [None]*(totalSteps+1)
    def recursiveClimbStairs(remainingSteps = totalSteps):
        if remainingSteps < 0:
            return 0
        if remainingSteps == 0:
            return 1
        if memo[remainingSteps]:
            return memo[remainingSteps]
        memo[remainingSteps] = (recursiveClimbStairs(remainingSteps - 1) +
                                recursiveClimbStairs(remainingSteps - 2))
        return memo[remainingSteps]

    return recursiveClimbStairs()


def climbStairsDynamic(totalSteps: int) -> int:
    memo = [None]*(totalSteps+2)
    memo[1] = 1
    memo[2] = 2
    for i in range(3, totalSteps+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[totalSteps]

class ClimbingStairs(unittest.TestCase):

    def create_test_case_parameters(funcList, parametersForFunc):
        finalParameters = []
        for func in funcList:
            for parameters in parametersForFunc:
                finalParameters.append((func,) + parameters)
        return finalParameters

    @parameterized.expand(create_test_case_parameters(
        [
            climbStairsRecursive,
            climbStairsMemoized,
            climbStairsDynamic
        ],
        [
            (1, 1),
            (2, 2),
            (3, 3),
            (7, 21)
        ]
    ))
    def test_climb_stairs_functions(self, climbStairsFunc,  totalSteps, expectedWaysToClimb):
        self.assertEqual(climbStairsFunc(totalSteps), expectedWaysToClimb)


if __name__ == '__main__':
    unittest.main()
