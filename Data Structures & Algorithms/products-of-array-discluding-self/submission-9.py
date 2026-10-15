class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # nums[:i] x nums[i:] = product[nums[i]]
        ans = [1] * len(nums)

        # Build products from previous products
        product = 1
        for i in range(len(nums)):
            ans[i] = product
            product *= nums[i]

        # Update products from products after nums[i]
        product = 1
        for i in range(len(nums)-1, -1, -1): # From last index to nums[0]
            ans[i] *= product
            product *= nums[i]
        
        return ans