class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # Hashmap to store {char count tuple: list of anagrams}
        for s in strs:  # Loop through each word
            count = [0] * 26  # Array for 'a' to 'z'
            for c in s:  # Count frequency of each character
                count[ord(c) - ord("a")] += 1  # Convert char to index
            
            res[tuple(count)].append(s)  # Store words with same count together
        
        return list(res.values())  # Convert dictionary values to list