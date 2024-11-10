from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_index = 0
        prefix = ""
        flag = True
        
        while flag:
            if prefix_index == len(strs[0]): break
        
            for i, text in enumerate(strs):
                if len(strs) == 1 or text == "":
                    prefix = text
                    flag = False
                    break

                if text.startswith(strs[0][0:prefix_index+1]):
                    if i+1 == len(strs):
                        prefix = strs[0][0:prefix_index+1]
                        prefix_index += 1
                else:
                    flag = False
                    break
        
        return prefix
    
strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
strs = [""]
strs = ["a"]
strs = ["",""]
strs = ["flower","flower","flower","flower"]
strs = ["abab","aba",""]

solution = Solution()
ans = solution.longestCommonPrefix(strs)
print(ans)