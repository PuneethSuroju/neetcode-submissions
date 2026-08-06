class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = dict()
        out_arr = []
        freq = 0


        for num in nums:
            if num in hashmap:
                hashmap[num] = hashmap[num] + 1
            else:
                hashmap[num] = 1
        pairs = list(hashmap.items())

        while len(out_arr) < k:
            for i, v in enumerate(pairs):
                if v[1] > freq:
                    freq = v[1]
                    where = i
                    what = v[0]

            out_arr.append(what)
            freq = 0
            pairs.pop(where)
        return out_arr





