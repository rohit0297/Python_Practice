class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return "" # Return empty string if list is empty

        strs.sort() #sort the list of strings

        #comparing the first and last string (which will be most different after sorting)
        first = strs[0]
        last = strs[-1]

        i = 0
        while i < len(first) and i < len(last) and first[i] == last [i]:
            i += 1  # Increment while characters match

        return first[:i] # Return the common prefix found