from hashlib import * 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() 
        for n in hashset:
            if n in hashset:
                return True
            hashset.add(n)
        
        return False