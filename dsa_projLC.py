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
                
