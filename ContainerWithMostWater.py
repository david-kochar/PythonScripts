"""

Given n non-negative integers a1, a2, ..., an , where each represents a point 
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints 
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis 
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

"""

class Solution:
    
    def maxArea(self, height):

        height_w_idx = []                                              #initialize list for height with indices
        
        areas = []                                                     #initialize list for areas from coordinates
        
        for i in range(0, len(height)):                                #append heights with indicies
            coord = [height[i], i]
            height_w_idx.append(coord)
            
        for i in range(0, len(height_w_idx)):                          #permute through height, take x and index of x
            x                = height_w_idx[i][0]
            idx_x            = height_w_idx[i][1]
            height_w_idx_rem = height_w_idx[:i] + height_w_idx[i + 1:] #take remainder of height
            for j in range(0, len(height_w_idx_rem)):                  #permute through remainder of eight, take x and index of x
                x2     = height_w_idx_rem[j][0]
                idx_x2 = height_w_idx_rem[j][1]
                area   = min(x, x2) * abs(idx_x - idx_x2)              #calculate area
                areas.append(area)
            
        return max(areas)                                              #find max area from areas

s = Solution()

s.maxArea([1,8,6,2,5,4,8,3,7])