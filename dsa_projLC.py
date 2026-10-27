#1541. Minimum Insertions to Balance a Parentheses String

class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        i=0
        stk=[]
        l=0
        ans=0
        while i<n:
            if s[i]=='(':
                stk.append(i)
                l += 1
                i += 1
            else:
                if l:
                    if (i+1)>=n or s[i+1]!=')':
                        ans += 1
                        i += 1
                    else:
                        i += 2
                    stk.pop()
                    l -= 1
                else:
                    if (i+1)>=n or s[i+1]!=')':
                        ans += 2
                        i += 1
                    else:
                        ans += 1
                        i += 2
        return ans + 2*l



#LC- 301. Remove Invalid Parentheses

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans=[]
        
        def get_min(s,n):
            stk=[]
            i=0
            while i<n:
                if s[i] not in '()':
                    i += 1
                    continue
                if stk==[] or s[i]=='(':
                    stk.append(s[i])
                else:
                    if stk[-1]=='(':
                        stk.pop()
                    else:
                        stk.append(s[i])
                i += 1
            return len(stk)
        
        def inValid(s,rem,n,d):
            if rem==0:
                m=get_min(s,n)
                if m==0 :
                    ans.append(s)

                return
            for i in range(n):
                if s[i] not in '()':
                    continue
                lft=s[:i]
                ryt=s[i+1:]
                if d.get(lft+ryt)==None:
                    inValid(lft+ryt,rem-1,n-1,d)
                    d[lft+ryt]=1
            return
        
        n=len(s)
        minrem=get_min(s,n)
        inValid(s,minrem,n,{})
        return ans


    #3727. Maximum Alternating Sum of Squares
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            nums[i] *= nums[i]
        nums.sort()
        s=sum(nums)
        sub=0
        for i in range(n//2):
            sub += nums[i]
        return s-2*sub

    #3723. Maximize Sum of Squares of Digits
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if 9*num<sum:
            return ''
        quotient = sum//9
        remainder = sum % 9
        if remainder:
            ans='9'*quotient + str(remainder)
            ans += '0'*(num-(quotient+1))
        else:
            ans='9'*quotient
            ans += '0'*(num-quotient)
        return ans
                
    
    #2913. Subarrays Distinct Element Sum of Squares I
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            d={}
            v=0
            for j in range(i,n):
                if d.get(nums[j],-1)==-1:
                    v += 1
                d[nums[j]]=1
                ans += v*v
        return ans


     #1569. Number of Ways to Reorder Array to Get Same BST
    def numOfWays(self, nums: List[int]) -> int:
        self.m=10**9+7
        n=len(nums)
        pascal=[[1 for j in range(i+1)]for i in range(n+1)]
        for i in range(2,n):
            for j in range(1,i):
                pascal[i][j]=(pascal[i-1][j]+pascal[i-1][j-1])%self.m
        

        def dfs(a,n):
            if n<=2:
                return 1
            a1,a2=[],[]
            l1,l2=0,0
            for i in a[1:]:
                if i>a[0]:
                    a1.append(i)
                    l1 += 1 
                else:
                    a2.append(i)
                    l2 += 1 
            val=pascal[n-1][l1]
            return ((val*dfs(a1,l1)%self.m)*dfs(a2,l2))%self.m

        ans=dfs(nums,n)
        return ans%self.m-1


    #3942. Minimum Operations to Sort a Permutation
    def minOperations(self, nums: List[int]) -> int:
        ind0=-1
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                ind0=i
                break
        prev,next=(n+(ind0-1))%n,(ind0+1)%n
        if nums[prev]==1:
            f=1
            val=1
        else:
            f=-1
            val=n-1
        for i in range(prev,-1,-1):
            if nums[i]!=val:
                return -1
            val += f
            val=(n+val)%n
        for i in range(n-1,next-1,-1):
            if nums[i]!=val:
                return -1
            val += f
            val=(n+val)%n
        if nums[0]-nums[n-1]==-n+1:
            return 0
        elif nums[0]-nums[n-1]==n-1:
            return 1
        if f==1:
            return min(ind0+2,n-ind0)
        return min(ind0,n-ind0+2)



    #3619. Count Islands With Total Value Divisible by K
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        def dfs(a,i,j,r,c):
            v=a[i][j]
            a[i][j]=0
            if (i+1)<r and a[i+1][j]:
                v += dfs(a,i+1,j,r,c)
            if (i-1)>=0 and a[i-1][j]:
                v += dfs(a,i-1,j,r,c)
            if (j+1)<c and a[i][j+1]:
                v += dfs(a,i,j+1,r,c)
            if (j-1)>=0 and a[i][j-1]:
                v += dfs(a,i,j-1,r,c)
            return v
                
        r=len(grid)
        c=len(grid[0])
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    v = dfs(grid,i,j,r,c)
                    if v%k==0:
                        count += 1
        return count