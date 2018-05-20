class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ht = dict()  # Hash table
        result = list()

        for char in p:
            if ht.get(char):
                ht[char] += 1
            else:
                ht[char] = 1

        w_start, w_end, diff = -1, -1, len(p)

        while w_end < len(s)-1:
            # print(w_start, w_end, diff)
            # print(ht)
            if ht.get(s[w_end+1]) is not None:
                if ht[s[w_end+1]] > 0:
                    # extend window
                    w_end += 1
                    diff -= 1
                    ht[s[w_end]] -= 1

                    if w_end - w_start == len(p) and diff == 0:
                        result.append(w_start+1)
                        # print(result)
                else:
                    # narrow window
                    if ht.get(s[w_start+1]) is not None:
                        ht[s[w_start+1]] += 1
                        diff += 1
                    w_start += 1
            else:
                if w_start == w_end:
                    w_end += 1
                # narrow window
                if ht.get(s[w_start+1]) is not None:
                    ht[s[w_start+1]] += 1
                    diff += 1
                w_start += 1

        return result


# solute = Solution()
# print(solute.findAnagrams("cbaebabacd", "abc"))
