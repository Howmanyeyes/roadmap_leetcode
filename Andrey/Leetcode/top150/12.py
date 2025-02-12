"""
380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was
not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was
present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at
least one element exists when this method is called). Each element must have the same probability of
being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.
"""

from random import choice

class RandomizedSet:

    def __init__(self):
        self.lenght = 0
        self.table = {}
        self.list_of_nums = []
        
    def insert(self, val: int) -> bool:
        if val in self.table:
            return False
        self.list_of_nums.append(val)
        self.lenght += 1
        self.table[val] = self.lenght - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.table:
            return False    
        last_val = self.list_of_nums[-1]  
        self.list_of_nums[self.table[val]] = self.list_of_nums[self.lenght - 1]
        self.table[last_val] = self.table[val]
        self.list_of_nums.pop()
        self.lenght -= 1
        self.table.pop(val)
        return True

    def getRandom(self) -> int:
        return choice(self.list_of_nums[:self.lenght]) 
