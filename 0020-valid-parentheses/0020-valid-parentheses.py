class Solution:
    def isValid(self, s: str) -> bool:
        stack=[] # Initialize an empty stack
        mapping = {')':'(','}':'{',']':'['} #closingg brackets mapped to their opening brackets
    
        for char in s: # Iterate over each character in the input string
            if char in mapping: # If it's a closing bracket
                if stack and stack[-1] == mapping[char]: # Check if top of stack is the matching open bracket 
                    stack.pop() # Remove the matched opening bracket
                else:
                    return False # Mismatch found, return false
            else:
                stack.append(char) # if it's an opening bracket, push it onto the stack 
        return True if not stack else False # If stack is empty, return True; otherwise, False