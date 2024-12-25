class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # in-place change
        k = 0  #  keeps track of the number of elements in nums not equal to val.
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # overwrite
                k += 1

        return k  # new length of the modified array.
