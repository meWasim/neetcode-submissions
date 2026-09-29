class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            left = i + 1
            right = len(numbers) - 1

            while left <= right:
                mid = (left + right) // 2
                total = numbers[i] + numbers[mid]

                if total == target:
                    return [i + 1, mid + 1]

                elif total < target:
                    left = mid + 1

                else:
                    right = mid - 1