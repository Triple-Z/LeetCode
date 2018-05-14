class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a
        # a is always longer
        ci = False
        rst = ""
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0:
            if j >= 0:
                if ci:
                    sum_bin = int(a[i]) + int(b[j]) + 1
                else:
                    sum_bin = int(a[i]) + int(b[j])

                j -= 1
                i -= 1
            else:
                if ci:
                    sum_bin = int(a[i]) + 1
                else:
                    sum_bin = int(a[i])

                i -= 1

            if sum_bin >= 2:
                ci = True
                rst = str(sum_bin%2) + rst
            else:
                ci = False
                rst = str(sum_bin) + rst

            # print(rst)
        
        if ci:
            rst = '1' + rst
        
        return rst

