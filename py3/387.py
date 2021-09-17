class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = {}

        for ch in s:
            char_map[ch] = char_map.get(ch, 0) + 1
        
        for i, ch in enumerate(s):
            if char_map[ch] == 1:
                return i
            
        return -1