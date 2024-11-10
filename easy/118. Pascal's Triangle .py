from typing import List
from copy import deepcopy

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        output = [[1], [1, 1]]
        middle_count = numRows - 2 # 中間的數量(不包括頭尾)

        for i in range(1, middle_count + 1):
            start_list = [1, 1]
            last_list = deepcopy(output[-1])
            
            for j in range(i):
                num = last_list[j] + last_list[j + 1]
                start_list.insert(j + 1, num)
            output.append(start_list)

        return output
            
numRows = 5
numRows = 1

solution = Solution()
ans = solution.generate(numRows)
print(ans)