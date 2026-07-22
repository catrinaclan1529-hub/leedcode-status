class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        i = 0
        d = 1

        for c in s:
            rows[i] += c
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
            i += d

        return "".join(rows)
        