class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x < y:
            x, y = y, x

        bin_x = bin(x)
        bin_y = bin(y)

        dist = 0
        i, j = len(bin_x)-1, len(bin_y)-1

        while i >= 0:
            if j <= 1 or bin_y[j] == 'b':
                if bin_x[i] == '1':
                    dist += 1
                    # print("if")
                i -= 1
            else:
                if bin_x[i] != bin_y[j]:
                    dist += 1
                    # print("else")
                i -= 1
                j -= 1

        return dist
