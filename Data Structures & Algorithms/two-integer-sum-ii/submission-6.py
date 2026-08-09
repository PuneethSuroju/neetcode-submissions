class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hashmap = dict()
        out = []
        for i, v in enumerate(numbers):
            diff = target - numbers[i]   
            if diff in hashmap:
                out.append(hashmap[diff])
                out.append(i)
            hashmap[v] = i
        for index in range(len(out)):
            out[index] += 1
        return out
            

                

        


        