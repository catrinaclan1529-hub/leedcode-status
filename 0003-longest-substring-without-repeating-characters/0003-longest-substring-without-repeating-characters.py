class Solution:
    def lengthOfLongestSubstring(self, s):
        d = {}
        left = ans = 0

        for right in range(len(s)):
            if s[right] in d and d[s[right]] >= left:
                left = d[s[right]] + 1

            d[s[right]] = right
            ans = max(ans, right - left + 1)

        return ans