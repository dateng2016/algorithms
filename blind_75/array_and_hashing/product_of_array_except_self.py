from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # This has a runtime and space complexity of O(n)
        pre_prod = [0] * (len(nums) + 1)
        post_prod = [0] * (len(nums) + 1)

        pre_prod[0] = 1
        post_prod[-1] = 1

        cur = 1
        for i in range(len(nums)):
            cur *= nums[i]
            pre_prod[i + 1] = cur
            if cur == 0:
                break

        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            cur *= nums[i]
            post_prod[i] = cur
            if cur == 0:
                break

        res = [0] * len(nums)
        for i in range(len(nums)):

            res[i] = pre_prod[i] * post_prod[i + 1]

            if nums[i] == 0:
                break

        return res
        # Brute force. R: O(n**2)
        res = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            res.append(prod)
        return res

        pass


