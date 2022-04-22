class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a = 0
        b = len(height)-1
        out = 0
        while(a != b):
            if height[a] >= height[b]:
                 c = abs(a-b)*height[b]
                 if(c >= out):
                     out = c
                 b -= 1
            if height[a] < height[b]:
                 c = abs(a - b) * height[a]
                 if (c >= out):
                     out = c
                 a += 1

        return out


if __name__ == '__main__':
    list =  [1, 8, 6, 2, 5, 4, 8, 3, 7]
    S = Solution()
    out = S.maxArea(list)
    print(out)