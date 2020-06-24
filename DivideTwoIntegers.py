"""

Given two integers dividend and divisor, divide two integers without using 
multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its 
fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2

"""
class Solution:
    
    def divide(self, dividend, divisor):
        
        i = 0
        
        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
            dividend = abs(dividend)
            divisor  = abs(divisor)
            while divisor < dividend:
                dividend -= divisor
                i += 1
            print(-(i))
        else:
            while divisor < dividend:
                dividend -= divisor
                i += 1
            print(i)


s = Solution()

s.divide(21, 6) #3