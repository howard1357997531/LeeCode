class Solution:
    def isValid(self, s: str) -> bool:
        left_brackets = ["(", "[", "{"]
        right_brackets = [")", "]", "}"]
        check_dict = {"(": ")", "[": "]", "{": "}"}
        check_list = []

        for i, bracket in enumerate(s):
            if len(s) == 1: return False

            if i == 0:
                if bracket in right_brackets: 
                    return False
                else:
                    check_list.append(bracket)

            if i > 0:
                if bracket in left_brackets:
                    check_list.append(bracket)
                else:
                    if len(check_list) == 0: return False

                    check = check_list[-1]
                    check = check_dict[check]
                    if bracket == check:
                        check_list.pop()
                    else:
                        return False
        
        return True if len(check_list) == 0 else False
            
s = "()"
s = "()[]{}"
s = "(]"
s = "([])"
s = "(){}}{"
s = "(])"

solution = Solution()
ans = solution.isValid(s)
print(ans)