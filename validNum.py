import re
class Solution:
    def validNum(self, s: str) -> bool:
        if len(s) < 1 or len(s) > 20:
            return 'Cannot tell'
        # single digit
        if len(s) == 1:
            try:
                int(s)
                return True
            except:
                return False
        
        # alphabets = set(A,a,B,b,C,c,D,d,F,f,G,g,H,h,I,i,J,j,K,k,L,l,M,m,N,n,O,o,P,p,Q,q,R,r,S,s,T,t,U,u,V,v,W,w,X,x,Y,y,Z,z)
        letters = re.compile('[a-dA-D][f-zF-Z]')


print(Solution().validNum('+8'))