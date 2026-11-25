"""
anagrams have the same letter frequency

so for each word in strs, compute its letter frequency
use this frequency as the key to a hashmap
then convert the hashmap into a list
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = {}
        for word in strs:
            # frequency is stored in a list of size 26
            # each position represents one letter
            letter_freq = [0 for _ in range(26)]
            for letter in word:
                # each time a letter is seen in a word
                # the corresponding index in the list is incremented
                letter_freq[ord(letter) - ord('a')] += 1
            # then we convert the frequency list to a
            # string to use it as the key in a hashmap (python dict in this case)
            if str(letter_freq) in result_map:
                result_map[str(letter_freq)].append(word)
            else:
                result_map[str(letter_freq)] = [word]
        
        # finally the hashmap is transformed into a list before returning
        # to pass the test
        return [result_map[k] for k in result_map]
