"""
주소: https://leetcode.com/problems/burst-balloons/description/

내용
- 0 이상, 100 이하의 가치를 지닌 풍선이 최대 500개 주어진다
- i번째 풍선을 터뜨리면 arr[i-1]*arr[i]*arr[i+1] 의 스코어를 얻는다
  - i=-1,n 인 지점의 가치는 1이라 가정한다
- 풍선을 하나씩 다 터뜨렸을때 얻을수있는 최대의 가치를 구하라

예제
Input: [3,1,5,8] 
Output: 167 
Explanation: 
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []   
coins = 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167

풀이방법
- 주의: 아직 덜푼문제임 추후 수정 필요
- 가치가 감소했다가 증가하는 지점을 먼저 모드 터뜨린다
  - 순서는 신경쓸필요없다. 모두 독립적인 지점일테니
- 이후 전체중 2번째로 큰 지점부터 터뜨린다
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def findValley(nums):
            if len(nums)==1:
                return -1
            
            for i in range(-1, len(nums)-1):
                if i==-1:
                    if nums[0]==0:
                        return 0
                elif i==len(nums)-2:
                    if nums[i+1]==0:
                        return i+1
                elif nums[i]>nums[i+1] and nums[i+2]>nums[i+1]:
                    return i+1
            return -1
        
        def findMaxIdx(nums):
            if len(nums)==1:
                return 0
            elif len(nums)==2:
                if nums[0]>nums[1]:
                    return 1
                else:
                    return 0
            
            maxVal = -1
            maxLoc = -1
            
            for i in range(1, len(nums)-1):
                if nums[i]>maxVal:
                    maxVal = nums[i]
                    maxLoc = i
            
            return maxLoc
        
        res = 0
        while len(nums)>0:
            valley = findValley(nums)
                
            if valley == -1:
                valley = findMaxIdx(nums)
                
            print(valley)
            
            if len(nums)==1:
                res += nums[0]
            elif valley==0:
                res += (nums[0]*nums[1])
            elif valley==len(nums)-1:
                res += (nums[valley-1]*nums[valley])
            else:
                res += (nums[valley-1]*nums[valley]*nums[valley+1])
            del nums[valley]
        
        return res
                
