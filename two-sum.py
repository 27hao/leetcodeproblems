class Solution(object):

    def twoSum(self, nums, target):

        """

        :type nums: List[int]

        :type target: int

        :rtype: List[int]

        """

        n=len(nums)

        i=0

        result=[]

        

        while i<n:

            j=i+1

            while j<n:

                if nums[i]+nums[j]==target:

                    result.append(i)

                    result.append(j)

                j+=1

            i+=1

        return result
