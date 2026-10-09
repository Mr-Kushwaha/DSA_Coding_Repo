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


