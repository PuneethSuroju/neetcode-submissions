class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        adarsh=set()

        for num in nums:
            if num in adarsh:
                return True
            adarsh.add(num)
        return False   

