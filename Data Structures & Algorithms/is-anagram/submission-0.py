class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_hash = {}

        for s_ch in s:
            my_hash[s_ch] = my_hash.get(s_ch, 0) + 1
        
        for t_ch in t:
            my_hash[t_ch] = my_hash.get(t_ch, 0) - 1

            if my_hash[t_ch] == 0:
                my_hash.pop(t_ch)
        
        if my_hash:
            return False
        else:
            return True