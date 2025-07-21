import unittest
from collections import defaultdict

def number_of_target_sum_subarrays(numbers, target_sum = 0):
    previous_sums = defaultdict(lambda: 0)

    target_sum_count = 0

    current_sum = 0
    for number in numbers:
        current_sum += number
        if current_sum == target_sum:
            target_sum_count += 1
        
        if (current_sum - target_sum) in previous_sums:
            target_sum_count += previous_sums[current_sum - target_sum]
        previous_sums[current_sum] += 1
    
    print(previous_sums)
    return target_sum_count


class TestTargetSumSubarrays(unittest.TestCase):

    def test_find_number_of_subarrays_with_zero_sum(self):
        self.assertEqual(number_of_target_sum_subarrays([1, 2, 3]), 0)
        self.assertEqual(number_of_target_sum_subarrays([1, -1]), 1)
        self.assertEqual(number_of_target_sum_subarrays([1, -1, 1, -1]), 4)
        self.assertEqual(number_of_target_sum_subarrays([2, -2, 3, 0, 4, -7]), 4)


if __name__ == '__main__':
    unittest.main()