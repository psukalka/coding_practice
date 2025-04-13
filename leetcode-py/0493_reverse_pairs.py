"""
Link: https://leetcode.com/problems/reverse-pairs/
"""
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.approach_2(nums)

    def approach_1(self, nums):
        """
        I can't think of any optimisation as of now, let's proceed with brute force first
        """
        reverse_pairs = 0
        for idx, i in enumerate(nums):
            for j in nums[idx+1:]:
                if i > 2*j:
                    reverse_pairs += 1
        return reverse_pairs
    
    def approach_2(self, nums):
        # This solution is incorrect
        """
        You can sense that there is some sort of repeated calculation happening. 
        Let's find out the repetition 

        we know that the right most number will always have 0 reverse pair. 
        The number to its left will have 0 or 1 depending on nums[-2] > 2*nums[-1]
        If we store the reverse pairs from right side, that might help us in avoiding repeated calculations. 

        rp[-1] = 0
        rp[-2] = 1 if nums[-2] > 2*nums[-1] else 0
        rp[-3] = rp[-2] + 1 if nums[-3] > 2*nums[-2] else 
        """
        dp_rp = list() # dp of reverse pairs
        n = len(nums) 
        for c, i in enumerate(reversed(nums)):
            if c == 0:
                dp_rp.append(0)
            else:
                # count dp for i
                ic = c
                idp = 0
                while ic >= 0:
                    if i > 2*nums[n-ic-1]:
                        idp = dp_rp[ic] + 1
                        break
                    ic -= 1
                dp_rp.append(idp)
        print(dp_rp)
        return sum(dp_rp)

        
    def test_solution(self):
        assert 2 == self.reversePairs([1,3,2,3,1])
        assert 3 == self.reversePairs([2,4,3,5,1])
        assert 4 == self.reversePairs([5,4,3,2,1])
        print("Tests passed")

s = Solution()
s.test_solution()