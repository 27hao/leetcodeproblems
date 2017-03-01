class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        re=[]
        twoList=[]
        i=0
        while i<n:
            j=i+1
            while j<n:
                twoList.append([nums[i],nums[j],i,j])
                j+=1
            i+=1
        i=0
        while i<n:
            for j in twoList:
                if i!=j[2] and i!=j[3] and nums[i]+j[0]+j[1]==0:
                    a=nums[i]
                    (a,j[0])=(a,j[0]) if a>j[0] else (j[0],a)
                    (a,j[1])=(a,j[1]) if a>j[1] else (j[1],a)
                    (j[1],j[0])=(j[1],j[0]) if j[1]>j[0] else (j[0],j[1])
                    re.append((j[0],j[1],a))
            i+=1
        re=list(set(re))
        return re
