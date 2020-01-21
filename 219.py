class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #hash set
        hash_set = {}
        for i in range(0,len(nums)):
            if not nums[i] in hash_set:
                hash_set[nums[i]] = i
            else:
                if abs(hash_set[nums[i]] - i) <= k:
                    return True
                else:
                    hash_set[nums[i]] = i
        return False
