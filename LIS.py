def lengthOfLIS(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        print(nums)
        dp = []
        for i in range(len(nums)):
            dp.append([1, i])
        for i in range(0, n):
            for j in range(0, i):
                if nums[i]>nums[j] and dp[i][0]<(dp[j][0]+1):
                    dp[i] = [dp[j][0]+1, j]
        print(dp)
        maxim = max(dp)
        maxo = -1
        for i in range(len(dp)):
            if dp[i]==maxim:
                maxo = i
        ans = []        
                
        while(maxo!=dp[maxo][1]):
            ans.append(maxo)
            maxo = dp[maxo][1]
        ans.append(maxo)
        ans1 = []
        for i in ans:
            ans1.append(nums[i])
        ans1.reverse()
        print(ans1)
        return maxim
        
print(lengthOfLIS([2,2, 2, 3, 4, 3]))
