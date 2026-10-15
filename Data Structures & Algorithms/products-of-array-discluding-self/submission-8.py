class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # FINDING:  Taking total product of nums and dividing it by product(i) yields i
        # e.g. 48/12 = 4, 48/8 = 6 --> total_product / product[i] = nums[i]
        #                          --> total_product / nums[i] = product[i]

        output = {}
        total_product = 1
        zero_count = 0

        for i in range(len(nums)):
            if nums[i] != 0: # Calculate total product avoiding ZeroDivisionError
                total_product *= nums[i]
            else:
                zero_count += 1
        
        if zero_count >= 2: # If there's 2+ zeros, then there can be no non-zero products
            return [0 for _ in range(len(nums))]

        product = []

        if zero_count == 0:
            for i in range(len(nums)):
                product.append((nums[i], int(total_product / nums[i])))

        else:
            for i in range(len(nums)):
                if nums[i] == 0:
                    product.append((nums[i], total_product))
                else:
                    product.append((nums[i], 0))

        ans = []
        for l in product:
            ans.append(l[1])
        
        return ans