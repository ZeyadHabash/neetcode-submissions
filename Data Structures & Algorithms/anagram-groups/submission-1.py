class Solution:
    def getFreq(self, s: str) -> tuple[int, ...]:
        freqList = [0] * 27
        for char in s:
            index = ord(char) - ord('a')
            freqList[index] += 1
        return tuple(freqList)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Anagrams are strings that have the same number of each letter
        # We only have 27 letters 
        # (since strings are lowercase only? if that wasnt the case we can convert to lowercase easily)
        
        # naive Solution would be 
        # - loop over all strings
        # - for each string create an array of size 27 that contains the frequency of each letter
        # - compare it to all other strings 

        result = []
        # for i in range(len(strs) - 1):
        #     result.append([strs[i]])
        #     charFreq = self.getFreq(strs[i])
            # for j in range(i+1, len(strs)):
            #     if self.getFreq(strs[j]) == charFreq:
            #         result[-1].append(strs[j])

            # while doing this I was like why dont we just use a hashmap 
            # with the charfreq array as a key then compare that
        charFreqMap = {}
        for i in range(len(strs)):
            charFreq = self.getFreq(strs[i])
            if charFreq in charFreqMap:
                charFreqMap[charFreq].append(strs[i])
            else:
                charFreqMap[charFreq] = [strs[i]]
            # charFreqMap[charFreq] = charFreqMap.get(charFreq,[]).append(strs[i])
        
        for v in charFreqMap.values():
            result.append(v)


        return result