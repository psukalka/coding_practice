"""
Link: https://www.interviewbit.com/problems/repeat-and-missing-number-array/
"""
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        return self.approach_1(A)
    
    def approach_1(self, A):
        """
        A simple approach can be to sort the array and then find the missing number by traversing it.
        This would take minimum O(log(n)) time

        A second approach can be to use an array of size n. Insert each number in that array. 
        If the number is already present, then we've found the duplicate number. 
        This would take an extra space of O(n)

        Suppose I find sum of all numbers in the array and then compare it with sum of 1 to n numbers. 
        The difference between these two sums would give me the difference between repeated number (R) and missing number (M)
        sum(1_to_n) - sum(arr) == M-R

        If I again repeat it like that with sum of squares, it should give me another equation
        sum(1_to_n_squares) - sum(arr_squares) == M^2 - R^2

        And two equations are enough to solve two variables.
        """
        sum_arr = 0
        sum_arr_sqr = 0 

        sum_n = 0 
        sum_n_sqr = 0 

        for i in A:
            sum_arr += i 
            sum_arr_sqr += i*i 

        for i in range(1, len(A)+1):
            sum_n += i 
            sum_n_sqr += i*i 

        mr_diff = sum_n - sum_arr
        mr_sqr_diff = sum_n_sqr - sum_arr_sqr
        mr_sum = mr_sqr_diff / mr_diff
        m = (mr_sum + mr_diff) / 2
        r = (mr_sum - m)

        return [int(r), int(m)]
    
    def test_solution(self):
        output = self.repeatedNumber([3,1,2,5,3])
        assert output[0] == 3
        assert output[1] == 4
        print("Tests passed")

s = Solution()
s.test_solution()