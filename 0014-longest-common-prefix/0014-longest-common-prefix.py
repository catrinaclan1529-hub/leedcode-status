class Solution:
    def longestCommonPrefix(self, strs):
        ans = strs[0]

        for s in strs[1:]:
            while not s.startswith(ans):
                ans = ans[:-1]

        return ans