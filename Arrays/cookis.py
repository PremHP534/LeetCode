class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        count = 0
        child = 0

        for cookie in s:
            if child < len(g) and cookie >= g[child]:
                count += 1
                child += 1

        return count
