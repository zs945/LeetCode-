class Solution( object ):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(0,len(nums)):
        #     nums.index(target-nums[i])
        #     # for j in range(i+1,len(nums)):
        #     #     if nums[j] == target-nums[i]:
        #     #         return [i,j]
        hashmap = {}
        for index, num in enumerate( nums ):
            another_num = target - num
            if another_num in hashmap.values():
                # return [hashmap.keys(another_num), index]
                return [list(hashmap.values()).index(another_num), index]
                # return [list(hashmap.keys())[list(hashmap.values()).index(another_num)], index]
                # print("y")
            hashmap[index] = num
            # print(hashmap)
        return None

if __name__ == "__main__":
    c= Solution()
    nums = [2, 7, 11, 15]
    target = 13
    # c.twoSum( nums, target )
    out = c.twoSum(nums,target)
    print(out)
    # c.twoSum([3,2,4],6)
    # c.twoSum([3,3],6)

