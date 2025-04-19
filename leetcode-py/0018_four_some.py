"""
Link: https://leetcode.com/problems/4sum/description/
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.approach_1(nums, target)
    
    def approach_1(self, nums, target):
        import math
        """
        Let's go by brute force
        Main time will go in finding unique set. 
        Let's find out first n prime numbers
        Use them to find out a unique number to store ith four-some 
        """
        n = len(nums)
        # primes = [2,3,5]
        # for i in range(6, 10000):
        #     is_prime = True
        #     for j in range(2, int(math.sqrt(i))+1):
        #         if i%j == 0:
        #             is_prime = False
        #             break
        #     if is_prime:
        #         primes.append(i)
        #     if len(primes) > 200:
        #         break

        fsl = dict()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            tl = [nums[i], nums[j], nums[k], nums[l]]
                            unique_id = "_".join(str(num) for num in sorted(tl))
                            if unique_id not in fsl:
                                fsl.update({unique_id: tl})
        return list(fsl.values())
        
    def test_solution(self):
        print(self.fourSum([1,0,-1,0,-2,2], 0))

s = Solution()
s.test_solution()