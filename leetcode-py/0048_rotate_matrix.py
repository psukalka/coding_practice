"""
https://leetcode.com/problems/rotate-image/description/
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # matrix = self.approach_1(matrix)
        self.approach_2(matrix)

    def approach_1(self, matrix):
        """
        By using extra space and creating a new matrix 
        """
        mat_len = len(matrix)
        rotated_matrix = list()
        for row in matrix:
            # Insert row vertically, meaning n-ith column
            for idx, r in enumerate(row):
                if len(rotated_matrix) <= idx:
                    rotated_matrix.append([r])
                else:
                    rotated_matrix[idx].insert(0, r)
        matrix = rotated_matrix
        return matrix
    
    def approach_2(self, matrix):
        """
        With in-place replacement.
        We will have to go box by box since rotating just one row will override the other value.
        
        How do I find a box ? 
        For a 3x3 matrix 
        0,0 --> 0,2 --> 2,2 --> 2,0
        0,1 --> 1,2 --> 2,1 --> 1,0

        
        For a 4x4 matrix
        i,j --> j,n-i -->n-i,n-j --> n-j,i 
        0,0 --> 0,3 --> 3,3 --> 3,0
        0,1 --> 1,3 --> 3,2 --> 2,0
        We will have to go till i = n/2 and j = n-i-1
        """
        n = len(matrix)
        m = n-1
        for i in range(int(n / 2)):
            for j in range(i, m-i):
                temp = matrix[m-j][i]
                matrix[m-j][i] = matrix[m-i][m-j]
                matrix[m-i][m-j] = matrix[j][m-i]
                matrix[j][m-i] = matrix[i][j]
                matrix[i][j] = temp
        return matrix
        

    def test_solution(self):
        # output = self.rotate([[1,2,3],[4,5,6],[7,8,9]])
        output = self.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
        for row in output:
            print(row)

s = Solution()
s.test_solution()