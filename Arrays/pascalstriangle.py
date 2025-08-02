"""Problem: Pascal’s Triangle
 Leetcode link : https://leetcode.com/problems/pascals-triangle
📅 Date Solved: 02-08-2025
🧠 Approach: Iterative Construction using Previous Row
📄 Description:
Generate the first numRows of Pascal’s Triangle, where each element is the sum of the two elements above it. The first and last elements of each row are always 1.
📝 Notes:
Initialized each row as a list of 1’s.
For inner elements, updated values by summing the two elements from the previous row.
Built the triangle row by row iteratively.
Time complexity: O(numRows^2)
Space complexity: O(numRows^2)
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[]
        for i in range(numRows):
            row=[1]*(i+1)
            if i>1:
                prevrow=triangle[i-1]
                for j in range(1,i):
                    row[j]=prevrow[j-1]+prevrow[j]
            triangle.append(row)
        return triangle