from typing import List

# ord('a') = 97 英轉字
# chr(97) = 'a' 字轉英
# letters_dicts = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], 
# '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], 
# '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = [chr(i) for i in range(97, 123)]
        letters_dict = {}
        for i in range(1, 9):
            if i < 6:
                letters_dict[str(i+1)] = letters[3*i-3:3*i]
            elif i == 6:
                letters_dict[str(i+1)] = letters[-11:-7]
            elif i == 7:
                letters_dict[str(i+1)] = letters[-7:-4]
            else:
                letters_dict[str(i+1)] = letters[-4:]
        
        digits_list = []
        for i in [i for i in digits]:
            digits_list.append(letters_dict[i])

        output = []

        if len(digits_list) == 0:
            output = []
        elif len(digits_list) == 1:
            output = digits_list[0]
        elif len(digits_list) == 2:
            for i in digits_list[0]:
                for j in digits_list[1]:
                    output.append(i+j)
        elif len(digits_list) == 3:
            for i in digits_list[0]:
                for j in digits_list[1]:
                    for k in digits_list[2]:
                        output.append(i+j+k)
        else:
            for i in digits_list[0]:
                for j in digits_list[1]:
                    for k in digits_list[2]:
                        for l in digits_list[3]:
                            output.append(i+j+k+l)
        
        return output

digits = "23"
# digits = ""
# digits = "2"
digits = "234"
digits = "5678"

solution = Solution()
ans = solution.letterCombinations(digits)
print(ans)


'''
def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(idx, comb):
            if idx == len(digits):
                res.append(comb[:])
                return
            
            for letter in digit_to_letters[digits[idx]]:
                backtrack(idx + 1, comb + letter)

        res = []
        backtrack(0, "")

        return res
'''