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