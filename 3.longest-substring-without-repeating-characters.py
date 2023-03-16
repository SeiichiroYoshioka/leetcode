#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        resu = [0]
        for i in range(len(s)):
            temp = []
            for st in s[i:]:
                if st not in temp:
                    temp.append(st)
                else:
                    break

            resu.append(len(temp))

        print(max(resu))
        return max(resu)


# @lc code=end
