"""
Link: https://www.naukri.com/code360/problems/count-inversions_615
"""
class Solution:
    def getInversions(self, arr, n):
        # write your code here !!
        return self.approach_1(arr, n)
    
    def approach_1(self, arr, n):
        """
        Inversion is when number on the right side is less than that number. 
        So, basically we want to find sum of all numbers lesser than ith number to its right.
        
        In this case, I will have to iterate through all the numbers to the right and find out which is smaller than arr[i]
        This would take O(n^2) time
        """
        inversions = 0
        for idx, i in enumerate(arr):
            for j in arr[idx+1:]:
                if j < i:
                    inversions += 1
        return inversions

    def test_solution(self):
        assert 3 == self.getInversions([3,2,1], 3)
        assert 4 == self.getInversions([2,5,1,3,4], 5)
        print("Tests passed")
        

s = Solution()
s.test_solution()