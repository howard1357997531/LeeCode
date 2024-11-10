from typing import List
from copy import deepcopy

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        output = [[1], [1, 1]]
        middle_count = rowIndex - 1 # 中間的數量(不包括頭尾)

        for i in range(1, middle_count + 1):
            start_list = [1, 1]
            last_list = deepcopy(output[-1])
            
            for j in range(i):
                num = last_list[j] + last_list[j + 1]
                start_list.insert(j + 1, num)
            output.append(start_list)

        return output[-1]

rowIndex = 3
# rowIndex = 0
# rowIndex = 1

solution = Solution()
ans = solution.getRow(rowIndex)
print(ans)