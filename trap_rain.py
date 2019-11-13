class Solution(object):
    
    # O(n^2)
    def trap2(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        
        res = 0
        
        for i in range(1, len(h)):
            
            max_l = max_r = 0
            
            #left
            for j in range(i-1, 0-1, -1):
                max_l = max(max_l, h[j])
                
            #right
            for j in range(i+1, len(h)):
                max_r = max(max_r, h[j])
            
            curTrap = max(0, min(max_l, max_r) - h[i])            
            
            res += curTrap
            
        return res
    
inp1 = [3,2,1,2,1,4,5,6,1,2] # 6
inp2 = [12,1,0,2] # 0
inp3 = [] # 0
#inp4 = [2,1,0,2] # 3
#inp5 = [2,0,2] # 2
#print inp
res = Solution().trap2(inp3)
print(res)

res = Solution().trap2(inp1)
print(res)

res = Solution().trap2(inp2)
print(res)

