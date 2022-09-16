'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Examples: 
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = ""
        anagrams = {}
        result = [] 

        if not strs: 
            return [result]

        for word in strs: 
            # sort word into alphabetical order
            temp = ''.join(sorted(word)) 
            # if the anagram key doesn't exist, add it to anagrams{} 
            if temp not in anagrams:
                # make sure to add a list with the square bracket notation. 
                # Or else the interpreter assumes you added just a string and 
                # the append() function throws an error. 
                anagrams[temp] = [word] # create a new bucket for new word and its anagrams. 
            else: 
                anagrams[temp].append(word)

        for key in anagrams: 
            result.append(anagrams[key])

        return result 