class Solution:  
    #GFG - Max Path Sum Between Two Leaves      
    def maxPathSum(self, root):
        # code here
        def maxleafsum(root):
            if root==None:
                return float('-inf'), float('-inf')
                
            if root.left==None and root.right==None:
                return float('-inf'), root.data
                
            ra,rytleaf=maxleafsum(root.right)
            la,lftleaf=maxleafsum(root.left)
            ans=max(ra,la,rytleaf+lftleaf+root.data)
            return ans, max(rytleaf+root.data, lftleaf+root.data)
            
        ans=maxleafsum(root)
        if ans[0]==float('-inf'):
            return -1
        return ans[0]
        
    #Maximum Frequency with K Increments

    def maxFrequency(self, arr, k):
        arr.sort()

        left = 0
        total = 0
        ans = 1

        for right in range(len(arr)):
            total += arr[right]

            # Cost to make all elements in the window equal to arr[right]
            cost = arr[right] * (right - left + 1) - total

            # If cost exceeds k, shrink the window
            while cost > k:
                total -= arr[left]
                left += 1
                cost = arr[right] * (right - left + 1) - total

            ans = max(ans, right - left + 1)

        return ans

    #Minimum Operations to Reach n

    def minOperation(self, n):
        return n.bit_length() + n.bit_count() - 1

    #Minimum Squares with Full Cuts
    def minSquares(self, n, m):
        def dfs(m=m,n=n):
            if m==0 or n==0:
                return 0
            if m==1 or n==1:
                return max(m,n)
            if n<m:
                m,n=n,m
            return dfs(m,n%m)+n//m
        return dfs()

    #Adding Ones
    def update(self, n: int, updates: list[int]) -> list[int]:
        ans=[0 for i in range(n)]
        for i in updates:
            ans[i-1] += 1
        for i in range(1,n):
            ans[i] += ans[i-1]
        return ans

    #Roll Characters of String
    def findRollOut(self, s, roll):
        n = len(s)
        changes = [0] * (n + 1)
        for i in roll:
            changes[i] -= 1
        arr = []
        r = len(roll)
        for c, d in zip(s, changes):
            r += d
            arr.append(chr(ord("a") + (ord(c) - ord("a") + r) % 26))
        return "".join(arr)

    #Maximum Without 3 Consecutive Set Bits
    def maxValue(self, n: int) -> int:
        def fun(n,i):
            if (1<<i)>n:
                return 0,0
            ans,c=fun(n,i+1)
            if n&(1<<i):
                c += 1
            else:
                c=0
            if c==3:
                c=0
            else:
                ans += ((1<<i)&n)
            return ans,c
            
        res=fun(n,0)
        return res[0]
            
    #Successful Binary Searches Irrespective of Pivot
    def countAlwaysFound(self, arr):
        from itertools import accumulate
        n = len(arr)
        prefix_max = list(accumulate(arr, max, initial = 0))
        suffix_min, count = arr[-1] + 1, 0
        for i in range(n - 1, -1, -1):
            if arr[i] < suffix_min:
                suffix_min = arr[i]
                if prefix_max[i] < arr[i]:
                    count += 1
        return count
        

    #Shortest Path From 1 To n
    def minimumStep (self, n):
        ret=-1
        while n:
            ret+=1
            if n%3==0:
                n//=3
            else:
                n-=1
        return ret


     #Palindrome with Replacement

    def minimumSum(self, s: str) -> int:
        s = list(s)
        low, high = 0, len(s) - 1
        total = 0

        while low < high:
            if s[low] != s[high]:
                if s[low] == '?':
                    s[low] = s[high]
                elif s[high] == '?':
                    s[high] = s[low]
                else:
                    return -1
            low += 1
            high -= 1

        prev = '?'
        for c in s:
            if c != '?':
                if prev != '?':
                    total += abs(ord(c) - ord(prev))
                prev = c

        return total
        

    #Minimize Max Min Diff with Subarray Removal
    def minDiff(self, k: int, arr: list[int]) -> int:
        from itertools import accumulate
        if k == 0:
            return max(arr) - min(arr)
        n = len(arr)
        if k == n - 1:
            return 0
        prefix_min = list(accumulate(arr[:n - k], min, initial=10**9))
        prefix_max = list(accumulate(arr[:n - k], max, initial=1))
        diff = prefix_max[-1] - prefix_min[-1]
        suffix_min = suffix_max = arr[-1]
        for i in range(n - 1, k - 1, -1):
            if arr[i] < suffix_min:
                suffix_min = arr[i]
            elif arr[i] > suffix_max:
                suffix_max = arr[i]
            diff = min(diff, max(prefix_max[i - k], suffix_max) - min(prefix_min[i - k], suffix_min))
        return diff

    
    #Maximum Weight Transformation of String
    def getMaxWeight(self, s):
        n = len(s)
        dp = [0]*(n+1)

        for i in range(n):
            dp[i+1] = dp[i] + 1
            if i == 0:
                continue

            dp[i+1] = max(dp[i+1], dp[i-1] + 4 - int(s[i] == s[i-1]))

        return dp[-1]
        