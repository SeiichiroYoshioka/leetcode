#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        t = [[] for _ in range(numRows)]
        reverse = True
        j = 0
        for i in range(len(s)):
            t[j].append(s[i])
            print(j)
            if j == 0 or j == numRows - 1:
                reverse = not reverse

            if numRows != 1:
                if reverse == True:
                    j -= 1
                else:
                    j += 1
        res = ""
        for ss in t:
            res += "".join(ss)
        return res


# @lc code=end
