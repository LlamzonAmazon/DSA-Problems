class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # 1. Sort – Allows us to dismiss certain values using 2-Pointer if left is not large enough
        nums.sort()
        print(nums)

        # 2. Reduce to 2Sum
        ans = []
        for a in range(len(nums)-1):

            if a > 0 and nums[a] == nums[a-1]: # Iterate a until last duplicate
                continue

            b = a+1
            c = len(nums)-1

            while b < c:
                if nums[b] + nums[c] == -nums[a]:
                    ans.append([nums[a], nums[b], nums[c]])
                    b += 1

                    while b < c and nums[b] == nums[b-1]: # Iterate b until last duplicate
                        b += 1

                elif nums[b] + nums[c] > -nums[a]:
                    c -= 1
                else:
                    b += 1


        return ans