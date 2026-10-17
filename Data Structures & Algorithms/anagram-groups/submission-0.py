class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = {}

        for word in strs:
            s_word = "".join(sorted(word))
            if s_word not in anagram_hash:
                anagram_hash[s_word] = []
            
            anagram_hash[s_word].append(word)
        
        return list(anagram_hash.values())

