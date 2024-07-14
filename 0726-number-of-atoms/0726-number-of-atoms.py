from collections import defaultdict
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse_formula(s):
            stack = []
            n = len(s)
            i = 0
            while i < n:
                if s[i] == '(':
                    stack.append('(')
                    i += 1
                elif s[i] == ')':
                    temp = defaultdict(int)
                    i += 1
                    start = i
                    while i < n and s[i].isdigit():
                        i += 1
                    multiplier = int(s[start:i] or 1)
                    
                    while stack and stack[-1] != '(':
                        elem, count = stack.pop()
                        temp[elem] += count * multiplier
                    stack.pop()  # Pop the '('
                    
                    for elem, count in temp.items():
                        stack.append((elem, count))
                else:
                    start = i
                    i += 1
                    while i < n and s[i].islower():
                        i += 1
                    elem = s[start:i]
                    
                    start = i
                    while i < n and s[i].isdigit():
                        i += 1
                    count = int(s[start:i] or 1)
                    
                    stack.append((elem, count))
            
            result = defaultdict(int)
            while stack:
                elem, count = stack.pop()
                result[elem] += count
            return result
        
        atom_counts = parse_formula(formula)
        result = ""
        for atom in sorted(atom_counts):
            count = atom_counts[atom]
            result += atom + (str(count) if count > 1 else "")
        return result
