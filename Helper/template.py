from typing import List
import time


class Solution:
    """
        >>> Solution().twoSum([3, 2, 4],6)
        [1, 2]
        >>> Solution().twoSum([2, 7, 11, 15],9)
        [0, 1]
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, i in enumerate(nums):
            for idx2, j in enumerate(nums):
                if i + j == target and idx1 != idx2:
                    return [idx1, idx2]


if __name__ == "__main__":
    import doctest

    start = time.time()
    doctest.testmod()
    end = time.time()
    print(end - start)
