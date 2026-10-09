#GFG - Max Path Sum Between Two Leaves

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:        
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
                
            
class Solution:
    