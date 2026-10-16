class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        d1 = {}
        for i in range(len(s1)):
            d1[s1[i]] = 1 + d1.get(s1[i], 0)

        for l in range(len(s2)-len(s1)+1):
            
            mc = 0

            window = list(s2[l:(l+len(s1))])

            if set(window) == d1.keys(): # if window charset matches s1 charset

                # build counts map from window
                w = {}
                for i in range(len(s1)):
                    w[window[i]] = 1 + w.get(window[i], 0)

                if w == d1:
                    return True 
                
        return False
