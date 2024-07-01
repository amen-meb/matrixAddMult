class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        min_freq = [float('inf')] * 26
    
        for word in words:
            char_freq = [0] * 26
            for char in word:
                char_freq[ord(char) - ord('a')] += 1
            for i in range(26):
                min_freq[i] = min(min_freq[i], char_freq[i])
    
        result = []
        for i in range(26):
            result.extend([chr(i + ord('a'))] * min_freq[i])
    
        return result

        
