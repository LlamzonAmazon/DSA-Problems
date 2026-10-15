class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        
        for item in strs:

            key = "".join(sorted(item))

            if key not in anagrams:
                anagrams[key] = [item]
            else:
                anagrams[key].append(item)

        ret = []

        for key in anagrams:
            ret.append(anagrams[key])

        return ret