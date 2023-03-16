#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "#" + "#".join(s) + "#"
        r = self.manachar(s)
        print(r)
        center = r.index(max(r))
        max_r = r[center]
        res = s[(center - max_r + 1) : (center + max_r)]
        res = res.replace("#", "")
        return res

    def manachar(self, s: str):
        i = 0
        j = 0
        r = [0 for _ in range(len(s))]
        # 文字列の最初から最後までを探索する
        while i < len(s):
            # j が文字列の範囲内にある間、探索する
            # iを中心とした半径jの回文であればjを伸ばしていく
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                j += 1

            # iを中心とした回文の半径
            r[i] = j

            k = 1
            while i - k >= 0 and k + r[i - k] < j:
                r[i + k] = r[i - k]
                k += 1
            i += k
            j -= k
        return r


# @lc code=end
